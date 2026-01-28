<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="90" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=30&duration=4000&color=6C63FF&center=true&vCenter=true&width=800&lines=Optimind;Advanced+Multi-Modal+AI+System;Locally-Hosted+Intelligent+Agent;Secure+and+Extensible+Architecture" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Core%20Engine-6366F1?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/AI-Hybrid%20Intelligence-8B5CF6?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Execution-Offline%20First-22C55E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Security-Zero%20Trust-EF4444?style=for-the-badge" />
</p>

---

## 🧠 What Is **Optimind**?

**Optimind** is a fully engineered **personal intelligence system** — not a chatbot.

It is designed to:

* 🖥️ Run **locally**
* 🔌 Work **offline-first**
* ☁️ Scale **online when needed**
* 🔐 Stay **fully under your control**

> **AI should be owned — not rented.**

---

## 🧬 Design Philosophy

```mermaid
flowchart LR
    Control --> Privacy --> Speed --> Intelligence --> Control
```

* **Control over execution**
* **Privacy by default**
* **Speed without compromise**
* **Modular intelligence**

---

## 🚀 Newly Added Features

### 🔧 Plugin System

* Dynamic plugin loading & management
* Voice-activated plugin triggers
* Interactive plugin manager (`p` key or voice)
* Hot-reload without restart
* Isolated execution per plugin

### 🎙️ Adaptive Whisper STT

* Smart model selection by audio length
* RAM-aware loading (8GB+ optimized)
* Real-time VAD & silence endpointing

### 🧠 Smart Parser & Automation

* Hybrid LLM routing (local + cloud)
* Automation task detection
* Automatic code execution
* Context-aware responses

### 🛡️ Enhanced Security Layers

* Password guard with secure validation
* Age verification system
* Content filtering
* Secure API session handling

### 📁 File & Data Processing

* CSV analysis & AI reports
* Word clouds with custom masks
* DOCX / PDF generation
* QR code generation

### 🎨 Media Creation Suite

* AI image generation (Pollinations)
* Audio generation (Melody)
* Screen & live camera analysis
* Object detection & recognition

---

## 🧠 System Architecture

```mermaid
flowchart TB
    User((Human)) --> Interface
    Interface --> STT[Whisper · Adaptive]
    Interface --> Vision[Camera · Screen]
    STT --> Brain[Smart Parser]
    Vision --> Brain
    Brain -->|Local| LocalLLMs[DeepSeek/Gemma]
    Brain -->|Fast| Groq[LLaMA 70B]
    
    subgraph "Plugin Ecosystem"
        P1[Media Plugins]
        P2[API Plugins]
        P3[Utility Plugins]
        P4[Custom Plugins]
    end
    
    LocalLLMs --> Memory[JSON Memory]
    Groq --> Memory
    Memory --> Decision[Task Router]
    
    Decision -->|Automation| Code[Auto‑Coder]
    Decision -->|Plugin| PluginSystem
    Decision -->|API| API[API Gateway]
    Decision -->|Chat| Response
    
    Code --> Output[Execution]
    PluginSystem --> Output
    API --> Output
    Response --> TTS[Typecast Voice]
    Response --> Media[Media Engine]
    
    Output --> Media
```

---

## ⚙️ Intelligence Stack

### 🎙️ Voice Layer

* Adaptive Whisper STT
* Typecast TTS
* Clap detection for hands-free activation

### 🧠 Language Models

**Cloud**

* Groq (LLaMA 70B)

**Local**

* DeepSeek 7B
* Gemma 7B
* LLaMA 8B
* Qwen 7B

Automatic routing based on task & connectivity.

---

## 🔌 Plugin Architecture

* Metadata-based plugins
* Trigger-driven activation
* Isolated execution
* Hot reload
* Plugin manager UI

---

## 🔐 Security Core

```mermaid
sequenceDiagram
    User->>Gateway: Request
    Gateway->>Security: Validate
    Security->>Database: Encrypt
    Database-->>Gateway: Verified
    Gateway-->>User: Access Granted
```

* Password protection
* Age verification
* Content filtering
* Local-first data storage


---
## 🏗️ Project Structure

```text
optimind/
├── main.py
├── auto_coder.py
├── memory.py
├── plugin.py
├── api_integrations.py
├── speak.py
├── clap.py
├── age.py
├── pwd_guard.py
├── conversation_memory.json
├── live_camera.py
├── live_screen.py
├── melody.py
├── triggers.py
├── local_llm_exec.py
├── requirements.txt
├── security_db
|   ├── age_guard.db
|   ├── sys_guard.db
├── whisper-cpp
|   ├── whisper-cpp-downloads
└── plugins/
    ├── calculator_plugin.py
    ├── joke_plugin.py
    ├── sample_weather_plugin.py

```

---

## 🔧 Plugin Development

```python
plugin_info = {
    "name": "My Plugin",
    "version": "1.0.0",
    "author": "You",
    "triggers": ["my command"]
}

def plugin_function(text, speak):
    speak("Plugin executed")
    return text
```

---

## 🛠️ Troubleshooting

* **Whisper not found** → Check model paths
* **No audio input** → Verify mic permissions
* **Slow performance** → Use smaller models

---

## 📄 License

Custom License

---

## 🏴 Final Words

This repository is **not a demo**.

It is a **foundation for personal AI sovereignty** — intelligence you own, control, and evolve.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366F1,100:8B5CF6&height=200&section=footer" />
</p>
