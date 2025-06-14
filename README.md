# B.R.I.H.A. – Behavioral Response & Intelligent Human Assistant
Your own J.A.R.V.I.S.-like voice AI assistant designed to listen, understand, and act – phase by phase.

B.R.I.H.A. is an evolving AI assistant built with Python. Inspired by Tony Stark's J.A.R.V.I.S., it’s designed to become a multi-functional, voice-controlled personal assistant. This is Phase 1: activating voice input, speech output, and basic response behavior.

✅ Voice input via microphone  
✅ Voice output using TTS  
✅ Core module-based design (listener, speaker, responder)  
✅ Modular code for future expansion  
✅ Search + Timer support (core utilities)

- Python 3.x
- SpeechRecognition
- pyttsx3
- Modular file structure with utils, core logic, and I/O separation

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

### Coming in Phase 2:
- Custom wake word
- GUI with voice command log
- Weather, alarms, and file access
- Contextual memory and smart reply logic
