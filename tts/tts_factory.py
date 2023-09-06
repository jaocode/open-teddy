# tts_factory.py - Copyright 2023 Okunarium Labs
# Helper script to make it easier to choose a voice provider.
# Edit existing functions or add additional ones to customize voices. 

def use_fakeyou ():
    from tts.fakeyou import FakeYou
    return FakeYou ()

def use_elevenlabs ():
    from tts.elevenlabs import ElevenLabs
    return ElevenLabs ()