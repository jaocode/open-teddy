import os.path
import time

import sounddevice as sd
import soundfile as sf

import tts.tts_factory

def speak(text, TTS):

    print ("Processing response.\n")
    # Take a time stamp for use in benchmarking the response time.
    bench_start = time.time()

    audio_file = TTS.create_speech_audio (text)
    
    # Displays the time  
    print(f'Response Time: {(time.time() - bench_start):.2f} secs\n')

    print ("Speaking.")
    data, fs = sf.read(audio_file)
    sd.play(data, fs, blocking=True)

if __name__ == '__main__':
    
    # See tts_factory.py file for available options.  
    TTS = tts.tts_factory.use_elevenlabs()

    go = True
    while go:
        print ("Enter text to speak:\n")
        query = input()

        # Exit script if the following text is entered.
        if query == "!exit":
            go = False
            continue
        
       
        speak (query, TTS)
        print ("Done!")