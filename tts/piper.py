from piper import PiperVoice
import wave

class Piper:

    def __init__(self, model='', gpu=False) -> None:
        self.gpu = gpu
        self.model = model
        self.tts = PiperVoice.load (model_path=self.model, use_cuda=self.gpu)

    def create_speech_audio (self, text, filename='output.wav'):
        wav = wave.open(f=filename, mode='wb')
        self.tts.synthesize (text, wav_file=wav)
        wav.close()        
        return filename
