
---
title: AI Skin Specialist
emoji: 🩺
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.30.0
app_file: app.py
pinned: false
---

# AI Skin Specialist

An AI-powered skin consultation assistant that accepts a patient's voice recording and a skin image, transcribes the patient's concern, generates general skin-care guidance using a vision-capable Groq model, and converts the response into audio using Deepgram text-to-speech.

## Features

- Voice recording or audio upload for describing skin concerns
- Skin image upload for visual analysis
- Speech-to-text transcription using Groq
- Image and text analysis using a Groq vision model
- Text-to-speech responses using Deepgram
- Interactive web interface built with Gradio

## Tech Stack

- Python
- Gradio
- Groq API
- Deepgram API
- Pillow
- python-dotenv
- uv for dependency management

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-SKIN-SPECIALIST
```

### 2. Create and activate a virtual environment

```powershell
uv venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
uv pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root with your API credentials:

```dotenv
GROQ_API_KEY=your_groq_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
WHISPER_MODEL=whisper-large-v3
DEEPGRAM_TTS_MODEL=aura-2-thalia-en
```

Replace the placeholder values with your own API keys. Never commit your real `.env` file.

### 5. Run the application

```powershell
python app.py
```

Open the local Gradio URL shown in the terminal.

## Medical Disclaimer

This project provides general informational skin-care guidance and is not a substitute for professional medical advice, diagnosis, or treatment. Consult a qualified dermatologist for medical concerns.

## Privacy

Avoid uploading sensitive personal information or identifiable images unless you understand how the configured AI services process submitted data.
