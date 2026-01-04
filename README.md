# Micky AI

Micky AI is a lightweight, text-based AI assistant built with Python and DialoGPT. It is designed to run on low-end hardware (like i3 processors) and provides intelligent responses using free AI models and web sources.

---

## Features

- **Text-to-Text AI Assistant**: Interact with Micky AI by typing your messages.
- **Wake Word Support**: Say "Hey Micky" to start conversations (text version for now).
- **Knowledge Sources**:
  - Wikipedia
  - Google
  - Reddit
  - Quora
  - Free online GPTs for additional insights
- **Slack Monitoring**: Receives notifications if someone messages or huddles you (personal notifications only).
- **WhatsApp Integration**: Can send and read messages when prompted.
- **CPU Friendly**: Optimized for low-end hardware using DialoGPT-medium.

---

## Getting Started

### Prerequisites
- Python 3.10+
- Pip

### Installation
1. Clone the repository or download the files.
2. Install required packages:

```bash
pip install transformers torch requests beautifulsoup4 slack_sdk pywhatkit

run the ai
python micky.py

Launch the AI with:

python micky.py
Type your messages.

Start a conversation with "Hey Micky" to get a response.
To exit, type exit.

project structure
micky-ai/
│
├── micky.py        # Main AI code
├── requirements.txt # Python dependencies
└── README.md       # Project explanation (this file)

Contact

Koushik Reddy – [koushikreddyofc@gmail.com]

Feel free to reach out for collaboration, feedback, or questions!
