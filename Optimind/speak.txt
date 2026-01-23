from data import API_KEY_TYPECAST as API_KEY
from typecast.client import Typecast
from typecast.models import TTSRequest, Output
from playsound import playsound
import os

# -----------------------
# Configuration
# -----------------------
VOICE_ID = "tc_62baac399b316e5fec036a26"  # Joshua - strong, youthful male
OUTPUT_FILE = "tts_output.mp3"

cli = Typecast(api_key=API_KEY)

# -----------------------
# Generate TTS
# -----------------------
def speak(text: str):
    response = cli.text_to_speech(TTSRequest(
        text=text,
        model="ssfm-v21",
        voice_id=VOICE_ID,
        output=Output(
            audio_format="mp3",
            audio_tempo=1.1
        )
    ))

    with open(OUTPUT_FILE, "wb") as f:
        f.write(response.audio_data)

    try:
        playsound(OUTPUT_FILE)
    finally:
        # Ensure deletion even if playback errors
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)

