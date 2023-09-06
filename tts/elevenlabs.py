# elevenlabs.py - Copyright 2023 Okunarium Labs
# Utilizes ElevenLabs (https://elevenlabs.io/) API to synthesize speech from text.
# ElevenLabs is a Cloud based TTS provider. 

import util.api_key as api_key # Util that loads an API key from a file.
from elevenlabs import generate, save

class ElevenLabs:

    def __init__(self, model='eleven_monolingual_v1', voice='Rachel') -> None:
        self.model = model
        self.voice = voice

    def create_speech_audio (self, text, filename='output.wav'):
        
        audio = generate (
            api_key = api_key.load_key ('./elevenlabs.key'),
            text=text,
            voice=self.voice,
            model=self.model
        )

        save(audio, filename=filename)

        return filename