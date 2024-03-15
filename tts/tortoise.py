# Make sure custom voices are imported to the Tortoise voice folder of the python environment's lib folder.

import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

import IPython

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

class Tortoise:

    def __init__(self) -> None:
        # This will download all the models used by Tortoise from the HF hub.
        self.tts = TextToSpeech()

        # Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
        self.preset = "ultra_fast"

         # Pick one of the voices from the output above
        self.voice = 'tom'

        # Load it and send it through Tortoise.
        self.voice_samples, self.conditioning_latents = load_voice(self.voice)

    def create_speech_audio (self, text, filename='output.wav'):
        gen = self.tts.tts_with_preset(text, voice_samples=self.voice_samples, conditioning_latents=self.conditioning_latents, 
                                preset=self.preset)
        torchaudio.save(filename, gen.squeeze(0).cpu(), 24000)
        return filename
