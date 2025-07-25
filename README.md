# B.R.I.H.A. – Behavioral Response & Intelligent Human Assistant
Your own J.A.R.V.I.S.-like voice AI assistant designed to listen, understand, and act – phase by phase.

### Project vision :
B.R.I.H.A. is an evolving AI assistant built with Python. Inspired by Tony Stark's J.A.R.V.I.S., it’s designed to become a multi-functional, voice-controlled personal assistant. This is Phase 1: activating voice input, speech output, and basic response behavior.

### Features-phase 1 :
✅ Voice input via microphone  
✅ Voice output using TTS  
✅ Core module-based design (listener, speaker, responder)  
✅ Modular code for future expansion  
✅ Search + Timer support (core utilities)

### Tech stack :
- **Language**: Python 3.x  
- **Voice Input**: SpeechRecognition, pyaudio  
- **Transcription**: OpenAI Whisper (tiny/base models) — offline, chunked processing  
- **Command Parsing**: Rule-based logic (custom)  
- **Execution Layer**: Python modules (reminders, timers, web scraping)  
- **Voice Output**: pyttsx3 / gTTS  
- **Scheduler**: APScheduler / datetime

### Folder structure :
briha/
│
├── core.py                 # Main control loop
├── listener.py            # Handles microphone input
├── speaker.py             # Text-to-speech engine
├── memory.json            # Assistant memory (stub)
├── utils/
│   ├── time_utils.py      # Timer support
│   └── search_utils.py    # Basic search logic
├── README.md

## Usage

```bash
git clone https://github.com/roops-spec/briha.git
cd briha
pip install -r requirements.txt
python core.py
```
Then say, “What’s the time?”, “Search AI”, or “Exit”.

### Coming in Phase 2:
- Custom wake word
- GUI with voice command log
- Weather, alarms, and file access
- Contextual memory and smart reply logic

### Design Note:
Phase 1 is lean by design: low-complexity, offline-first, and modular. Prioritizes reliability and core user loop over streaming or ML-heavy features. Phase 2 will explore real-time duplex audio, async NLP, and LLM integration.
