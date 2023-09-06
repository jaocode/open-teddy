# fakeyou.py - Copyright 2023 Okunarium Labs
# Utilizes FakeYou (https://fakeyou.com/) API to synthesize speech from text.
# FakeYou is a Cloud based TTS provider. 

import os

import util.api_key as api_key
import fakeyou

class FakeYou:

    # Model token is taken from "Share this TTS model" link
    def __init__(self, model_token='TM:24nz88eyawr3') -> None:
        api_credentials = api_key.load_credentials ('./fakeyou.key') 

        # init fakeyou API for voice synthesis
        self.fy=fakeyou.FakeYou()
        self.fy.login(api_credentials[0], api_credentials[1])
        self.model_token = model_token

    # Turn the text to speech.
    def create_speech_audio (self, text, filename='output.wav'):
        tempfile = self.fy.say(text=text,ttsModelToken=self.model_token).save()
        os.rename (tempfile, filename)
        return filename
        