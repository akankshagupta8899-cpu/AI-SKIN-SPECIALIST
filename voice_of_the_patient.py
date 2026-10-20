
import os
import logging

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def transcribe_patient_voice(audio_filepath: str) -> str:
    """
    Transcribe a recorded audio file using Groq Whisper.

    audio_filepath: Path to an audio file recorded or uploaded
                    through the Gradio interface.
    """
    if not audio_filepath or not os.path.isfile(audio_filepath):
        raise FileNotFoundError("A valid patient audio file is required.")

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY environment variable.")

    client = Groq(api_key=groq_api_key)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=os.getenv("WHISPER_MODEL", "whisper-large-v3"),
        )

    text = transcription.text.strip()
    logger.info("Patient audio transcribed successfully.")
    return text
