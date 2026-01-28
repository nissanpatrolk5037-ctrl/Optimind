import cv2
import torch
import numpy as np
import os
import urllib.request
from pathlib import Path
import time
from typing import Optional, Tuple, List, Dict

# ============================================================================
# SIMPLE FUNCTIONS TO USE IN YOUR CODE
# ============================================================================

def image_obj_detect_and_recognition(image_path: str, 
                                    output_path: Optional[str] = None,
                                    model_name: str = "yolov10n",
                                    confidence: float = 0.25,
                                    show_result: bool = True) -> Tuple[np.ndarray, List[dict]]:
    """
    Detect and recognize objects in an image file
    
    Args:
        image_path: Path to input image (required)
        output_path: Path to save output image (optional)
        model_name: Model to use: 'yolov10n', 'yolov10s', 'yolov10m', 'yolov10l', 'yolov10x'
        confidence: Confidence threshold (0.0 to 1.0)
        show_result: Show the result in a window
    
    Returns:
        Tuple of (annotated_image, detections_list)
    
    Example:
        result_img, detections = image_obj_detect_and_recognition("test.jpg")
    """
    print(f"\n🔍 Starting image detection...")
    print(f"   Image: {image_path}")
    print(f"   Model: {model_name}")
    
    # Force CPU usage
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    
    # Create detector
    detector = YOLOv10Detector(model_name=model_name, conf_threshold=confidence, device='cpu')
    
    # Detect
    result_image, detections = detector.detect_image(image_path)
    
    # Print results
    print(f"\n✅ Detection complete!")
    print(f"   Found {len(detections)} objects")
    
    if len(detections) > 0:
        print("\n📋 Detected objects:")
        # Show unique classes with counts
        class_counts = {}
        for det in detections:
            class_name = det['class_name']
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
        
        for class_name, count in sorted(class_counts.items()):
            print(f"   • {class_name}: {count}")
        
        # Show top 5 by confidence
        sorted_dets = sorted(detections, key=lambda x: x['confidence'], reverse=True)
        print("\n🏆 Top detections by confidence:")
        for i, det in enumerate(sorted_dets[:5]):
            print(f"   {i+1}. {det['class_name']} ({det['confidence']:.1%})")
    
    # Save if requested
    if output_path:
        cv2.imwrite(output_path, result_image)
        print(f"\n💾 Saved result to: {output_path}")
    
    # Show if requested
    if show_result:
        window_name = f"YOLOv10 Detection - {model_name}"
        cv2.imshow(window_name, result_image)
        print("\n👀 Press any key to close result window...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    return result_image, detections


def live_camera(model_name: str = "yolov10n",
                camera_id: int = 0,
                confidence: float = 0.25) -> None:
    """
    Start live camera object detection
    
    Args:
        model_name: Model to use: 'yolov10n', 'yolov10s', 'yolov10m', 'yolov10l', 'yolov10x'
        camera_id: Camera ID (0 for default webcam)
        confidence: Confidence threshold (0.0 to 1.0)
    
    Example:
        live_camera()  # Starts live detection with default webcam
        live_camera(model_name="yolov10s", camera_id=0, confidence=0.3)
    """
    print(f"\n📹 Starting live camera detection...")
    print(f"   Camera: {camera_id}")
    print(f"   Model: {model_name}")
    print(f"   Confidence: {confidence}")
    print(f"\n🎮 Controls:")
    print("   • Press 'q' to quit")
    print("   • Press 's' to save screenshot")
    print("   • Press 'p' to pause/resume")
    print("   • Press '+' to increase confidence")
    print("   • Press '-' to decrease confidence")
    
    # Force CPU usage
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    
    # Create detector
    detector = YOLOv10Detector(model_name=model_name, conf_threshold=confidence, device='cpu')
    
    # Start live detection
    detector.live_camera_detection(camera_id=camera_id)
    
    print("\n✅ Live detection stopped.")


# ============================================================================
# DETECTOR CLASS (Internal implementation)
# ============================================================================

class YOLOv10Detector:
    def __init__(self, model_name: str = "yolov10n", conf_threshold: float = 0.25, 
                 iou_threshold: float = 0.45, device: str = None):
        self.model_name = model_name.lower()
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold
        self.model = None
        
        # Force CPU if specified or auto-detect
        if device == 'cpu' or device is None:
            self.device = 'cpu'
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        else:
            self.device = device
        
        print(f"⚙️ Using device: {self.device}")
        
        # Create directories for models and data
        self.base_dir = Path.home() / ".yolov10_detector"
        self.models_dir = self.base_dir / "models"
        self.data_dir = self.base_dir / "data"
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Load COCO class names (auto-creates if not exists)
        self.coco_names = self._load_coco_names()
        
        # Install ultralytics if needed
        self._install_ultralytics()
        
        # Download and load model
        self.model_path = self._download_model()
        self._load_model()
    
    def _install_ultralytics(self):
        """Install ultralytics package if not available"""
        try:
            from ultralytics import YOLO
            self.ultralytics_available = True
        except ImportError:
            print("📦 Installing ultralytics...")
            try:
                import subprocess
                import sys
                subprocess.check_call([sys.executable, "-m", "pip", "install", "ultralytics"])
                from ultralytics import YOLO
                self.ultralytics_available = True
                print("✅ Ultralytics installed successfully")
            except:
                print("❌ Failed to install ultralytics")
                print("💡 Please install manually: pip install ultralytics")
                import sys
                sys.exit(1)
    
    def _download_model(self) -> Path:
        """Download YOLOv10 model if not already present"""
        model_file = self.models_dir / f"{self.model_name}.pt"
        
        # Check if model already exists
        if model_file.exists():
            print(f"✅ Model already exists: {model_file}")
            return model_file
        
        print(f"📥 Downloading {self.model_name}...")
        
        # YOLOv10 model URLs
        model_urls = {
            "yolov10n": "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt",
            "yolov10s": "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10s.pt",
            "yolov10m": "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10m.pt",
            "yolov10l": "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10l.pt",
            "yolov10x": "https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10x.pt",
        }
        
        if self.model_name not in model_urls:
            print(f"⚠️ Model {self.model_name} not found. Available: {list(model_urls.keys())}")
            self.model_name = "yolov10n"
            model_file = self.models_dir / f"{self.model_name}.pt"
        
        url = model_urls[self.model_name]
        
        try:
            # Download model
            print(f"⬇️ Downloading from: {url}")
            urllib.request.urlretrieve(url, model_file)
            
            # Verify download
            if model_file.stat().st_size < 1000000:  # Less than 1MB = error
                model_file.unlink()
                raise Exception("Downloaded file too small")
            
            print(f"✅ Model downloaded: {model_file}")
            return model_file
            
        except Exception as e:
            print(f"❌ Download error: {e}")
            print("🔄 Trying YOLOv5 fallback...")
            
            # Try YOLOv5 as fallback
            try:
                model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
                torch.save(model.state_dict(), model_file)
                print(f"✅ YOLOv5 fallback saved: {model_file}")
                return model_file
            except:
                print("❌ All download methods failed")
                print("💡 Please download manually from GitHub")
                import sys
                sys.exit(1)
    
    def _load_coco_names(self) -> Dict[int, str]:
        """Load COCO class names (80 classes) - auto-creates if not exists"""
        coco_names_file = self.data_dir / "coco.names"
        
        # If file exists, load it
        if coco_names_file.exists():
            with open(coco_names_file, 'r') as f:
                lines = f.readlines()
            coco_classes = [line.strip() for line in lines]
            print(f"✅ Loaded COCO names: {len(coco_classes)} classes")
        else:
            # Create COCO class names (80 classes)
            coco_classes = [
                "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
                "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
                "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
                "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
                "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
                "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
                "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
                "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
                "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
            ]
            
            # Save to file
            with open(coco_names_file, 'w') as f:
                for name in coco_classes:
                    f.write(f"{name}\n")
            print(f"✅ Created COCO names file: {len(coco_classes)} classes")
        
        # Create mapping
        return {i: name for i, name in enumerate(coco_classes)}
    
    def _load_model(self):
        """Load the YOLOv10 model"""
        try:
            from ultralytics import YOLO
            
            print(f"🔄 Loading model: {self.model_path}")
            self.model = YOLO(self.model_path)
            
            # Test model
            dummy_input = torch.zeros((1, 3, 640, 640))
            _ = self.model(dummy_input)
            
            print(f"✅ Model loaded successfully")
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            print("🔄 Loading YOLOv5 fallback...")
            self._load_yolov5_fallback()
    
    def _load_yolov5_fallback(self):
        """Load YOLOv5 as fallback"""
        try:
            self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
            self.model.to(self.device)
            print("✅ Loaded YOLOv5s as fallback")
        except Exception as e:
            print(f"❌ Failed to load fallback: {e}")
            import sys
            sys.exit(1)
    
    def detect_image(self, image_path: str) -> Tuple[np.ndarray, List[dict]]:
        """Detect objects in an image file"""
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image not found: {image_path}")
        
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not read image: {image_path}")
        
        return self.detect_frame(image)
    
    def detect_frame(self, frame: np.ndarray) -> Tuple[np.ndarray, List[dict]]:
        """Detect objects in a frame"""
        if self.model is None:
            raise ValueError("Model not loaded")
        
        original_frame = frame.copy()
        detections = []
        
        # Convert BGR to RGB for YOLO
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        try:
            # Perform inference
            if hasattr(self.model, 'predict'):  # Ultralytics YOLO
                results = self.model(frame_rgb, 
                                    conf=self.conf_threshold,
                                    iou=self.iou_threshold,
                                    device=self.device,
                                    verbose=False)
                
                if len(results) > 0 and results[0].boxes is not None:
                    boxes = results[0].boxes.xyxy.cpu().numpy()
                    scores = results[0].boxes.conf.cpu().numpy()
                    class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
                    
                    for box, score, class_id in zip(boxes, scores, class_ids):
                        x1, y1, x2, y2 = map(int, box)
                        
                        # Get class name
                        class_name = self.coco_names.get(class_id, f"class_{class_id}")
                        
                        detections.append({
                            'bbox': [x1, y1, x2, y2],
                            'confidence': float(score),
                            'class_id': int(class_id),
                            'class_name': class_name
                        })
                        
                        # Draw bounding box
                        self._draw_detection(frame, x1, y1, x2, y2, class_name, score, class_id)
            
            else:  # YOLOv5 fallback
                results = self.model(frame_rgb)
                
                for *box, conf, cls_id in results.xyxy[0]:
                    x1, y1, x2, y2 = map(int, box)
                    class_id = int(cls_id)
                    class_name = self.coco_names.get(class_id, f"class_{class_id}")
                    
                    detections.append({
                        'bbox': [x1, y1, x2, y2],
                        'confidence': float(conf),
                        'class_id': class_id,
                        'class_name': class_name
                    })
                    
                    # Draw bounding box
                    self._draw_detection(frame, x1, y1, x2, y2, class_name, conf, class_id)
        
        except Exception as e:
            print(f"⚠️ Inference error: {e}")
        
        return frame, detections
    
    def _draw_detection(self, frame, x1, y1, x2, y2, class_name, score, class_id):
        """Draw detection on frame"""
        h, w = frame.shape[:2]
        
        # Get color for this class
        color = self._get_color(class_id)
        
        # Draw rectangle
        thickness = max(1, int(min(h, w) / 400))
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
        
        # Prepare label
        label = f"{class_name}: {score:.2f}"
        
        # Draw label background
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = max(0.4, min(h, w) / 1000)
        (text_width, text_height), baseline = cv2.getTextSize(label, font, font_scale, 1)
        
        # Label background rectangle
        cv2.rectangle(frame, 
                     (x1, y1 - text_height - baseline - 5),
                     (x1 + text_width, y1),
                     color, -1)
        
        # Label text
        cv2.putText(frame, label, 
                   (x1, y1 - baseline - 5),
                   font, font_scale, (255, 255, 255), 1)
    
    def _get_color(self, class_id: int) -> tuple:
        """Get color for class ID"""
        colors = [
            (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
            (255, 0, 255), (0, 255, 255), (255, 128, 0), (128, 255, 0),
            (0, 128, 255), (255, 0, 128), (128, 0, 255), (0, 255, 128),
            (255, 128, 128), (128, 255, 128), (128, 128, 255)
        ]
        return colors[class_id % len(colors)]
    
    def live_camera_detection(self, camera_id: int = 0, window_name: str = "YOLOv10 Live Detection"):
        """Live camera object detection"""
        cap = cv2.VideoCapture(camera_id)
        
        if not cap.isOpened():
            print(f"❌ Could not open camera {camera_id}")
            # Try to find available cameras
            for i in range(3):
                test_cap = cv2.VideoCapture(i)
                if test_cap.isOpened():
                    print(f"   Try camera ID: {i}")
                    test_cap.release()
            return
        
        # Get camera info
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        print(f"📸 Camera {camera_id}: {w}x{h} @ {fps:.1f} FPS")
        
        frame_count = 0
        fps_display = 0
        prev_time = time.time()
        paused = False
        
        print("\n▶️ Starting live detection...")
        
        while True:
            if not paused:
                ret, frame = cap.read()
                if not ret:
                    print("❌ Could not read frame")
                    break
                
                # Perform detection
                start_time = time.time()
                detected_frame, detections = self.detect_frame(frame.copy())
                inference_time = time.time() - start_time
                
                # Calculate FPS
                current_time = time.time()
                frame_count += 1
                
                if current_time - prev_time >= 1.0:
                    fps_display = frame_count
                    frame_count = 0
                    prev_time = current_time
                
                # Display info
                y_offset = 30
                line_h = 25
                
                info_lines = [
                    f"FPS: {fps_display}",
                    f"Inference: {inference_time*1000:.1f}ms",
                    f"Detections: {len(detections)}",
                    f"Confidence: {self.conf_threshold:.2f}",
                    f"Model: {self.model_name}",
                    f"Device: {self.device}"
                ]
                
                for i, text in enumerate(info_lines):
                    cv2.putText(detected_frame, text, (10, y_offset + line_h * i),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                # Show top detections
                if len(detections) > 0:
                    sorted_dets = sorted(detections, key=lambda x: x['confidence'], reverse=True)
                    top_n = min(3, len(sorted_dets))
                    
                    for i in range(top_n):
                        det = sorted_dets[i]
                        text = f"{det['class_name']}: {det['confidence']:.2f}"
                        y_pos = y_offset + line_h * (6 + i)
                        cv2.putText(detected_frame, text, (10, y_pos),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            
            else:
                # Show paused screen
                detected_frame = frame.copy() if 'frame' in locals() else np.zeros((h, w, 3), dtype=np.uint8)
                cv2.putText(detected_frame, "PAUSED", (w//2 - 50, h//2),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Show frame
            cv2.imshow(window_name, detected_frame)
            
            # Handle keys
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = self.base_dir / f"detection_{timestamp}.jpg"
                cv2.imwrite(str(filename), detected_frame)
                print(f"💾 Saved screenshot: {filename}")
            elif key == ord('p'):
                paused = not paused
                print(f"{'⏸️ Paused' if paused else '▶️ Resumed'}")
            elif key == ord('+') or key == ord('='):
                self.conf_threshold = min(0.95, self.conf_threshold + 0.05)
                print(f"🔺 Confidence: {self.conf_threshold:.2f}")
            elif key == ord('-'):
                self.conf_threshold = max(0.05, self.conf_threshold - 0.05)
                print(f"🔻 Confidence: {self.conf_threshold:.2f}")
        
        cap.release()
        cv2.destroyAllWindows()


