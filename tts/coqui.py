# coqui.py - Copyright 2023 Okunarium Labs
# Utilizes Coqui API to synthesize speech from text.

from TTS.api import TTS
from TTS.utils.synthesizer import Synthesizer

class Coqui:

    def __init__(self, model='tts_models/en/ljspeech/glow-tts', gpu=False) -> None:
        self.gpu = gpu
        self.model = model #Multilinguel model
        self.speaker_wav = None
        self.language_name = "en"
        self.tts = TTS(model_name=self.model, progress_bar=False, gpu=self.gpu)

    # Use voice cloning to synthesize speech.
    def use_cloned_voice (self, speaker_audio):
        self.model='tts_models/multilingual/multi-dataset/your_tts'
        self.speaker_wav = speaker_audio
        self.tts = TTS(model_name=self.model, progress_bar=False, gpu=self.gpu)

    # Use a custom trained model to synthesize speech  
    def use_custom_model (self, custom_model, custom_model_config):
        self.speaker_wav=None
        self.tts.synthesizer = Synthesizer(
            tts_checkpoint=custom_model,
            tts_config_path=custom_model_config,
            tts_speakers_file=None,
            tts_languages_file=None,
            vocoder_checkpoint=None,
            vocoder_config=None,
            encoder_checkpoint=None,
            encoder_config=None,
            use_cuda=self.gpu,
        )

    def create_speech_audio (self, text, filename='output.wav'):     
        wav = self.tts.synthesizer.tts(
            text=text,
            speaker_name=None,
            language_name=self.language_name,
            speaker_wav=self.speaker_wav,
            reference_wav=None,
            style_wav=None,
            style_text=None,
            reference_speaker_name=None,
        )

        self.tts.synthesizer.save_wav(wav=wav, path=filename)
        
        return filename
