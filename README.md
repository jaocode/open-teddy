# open-teddy
This repository implements a basic example of an AI buddy using Python and ChatGPT. It is based on my first iteration of the interactive teddy bear shown at my [YouTube channel](https://www.youtube.com/@okunariumlabs). 

Currently, ChatGPT and voice provider code is available. Additional code will be added to complete the implementation to coincide with the release of future videos. 

An overview of the project is presented in this [video](https://www.youtube.com/watch?v=4XS8u6wuXDQ&t=100s). 

## Dependencies

### Python 3.10
The example was tested using Python 3.10 on Windows, Linux, and MacOS platforms. 

### OpenAI package
To install:
pip3 install openai

An OpenAI API key is required. It is obtained by creating an account with OpenAI. Add the key to the openai.key.  

### Speech Providers
The project supports a variety of speech provider options. Choose one that best meets your requirements. 

Coqui and Piper are recommended for on device speech synthesis. ElevenLabs is the recommended for situations where Cloud based speech synthesis is preferred. 

#### FakeYou package
[FakeYou](https://fakeyou.com/) is a Cloud based speech provider with a large library of voices to choose from. The results are good, but the service response times can be slow.  

To install:
pip3 install fakeyou

Notes:
- An FakeYou login and password are required. Create them by registering an account at [FakeYou](https://fakeyou.com/). Add them to the fakeyou.key file. 

#### ElevenLabs package
[ElevenLabs](https://elevenlabs.io/) is a Cloud based speech provider service that clones voices from recorded samples. It is fast and produces high quality output. 

To install:
pip3 install elevenlabs

Notes:
- An ElevenLabs API key is required. Obtain a key by creating an account with [ElevenLabs](https://elevenlabs.io/). Add the key to the elevenlabs.key file.

#### TortoiseTTS package
TortoiseTTS is an on device text to speech provider that clones voices from recorded samples. It provides high quality results but requires a powerful Nvidia GPU to achieve "reasonable" performance.  

To use Tortoise-TTS as a text to speech provider. 

To install:
pip3 torch torchaudio tortoise-tts 

Notes: 
- TortoiseTTS and Coqui can't coexist in the same python environment because of a dependency conflict with the transformers package.

#### Coqui package
Coqui is an on device text to speech provider that can clone voices or utilize custom trained voice models. It offers good quality results and is efficent enough to run on modest hardware, with or without a Nvidia GPU.  

To install:
pip3 install tts

#### Piper-tts package
Piper is an on device text to speech provider that can utilize custom trained voice models. It offers good quality while being extremely fast. It is efficient enough to run on small single board computers, such as Raspberry Pi 4.

Install with 'pip3 install piper-tts'.

Notes:
- Additional effort is required to get Piper working on MacOS and Windows.

### Other dependencies
To install other required packages:
pip3 install sounddevice soundfile

## Executables

test_ai.py - This is a basic script for testing the ChatGPT functionality. It takes in input from the console and outputs ChatGPT's response. It benchmarks and displays the time it took to receive the response. The elapsed time is an important consideration for an engauging interactive experience. 

test_tts.py - This is a basic script for testing voice provider functionality. It takes in input from the console and synthesizes it into speech. It benchmarks and displays the time it took to receive the response. The elapsed time is an important consideration for an engauging interactive experience.

open_teddy.py - This will take in a request entered at the console, send it to ChatGPT for a response, and then speak the response. 
