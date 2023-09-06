# open-teddy
This repository implements a basic example of an AI buddy using Python and ChatGPT. It is based on my first iteration of the interactive teddy bear shown at my [YouTube channel](https://www.youtube.com/@okunariumlabs). 

Currently, ChatGPT and voice provider code is available. Additional code will be added to complete the implementation to coincide with the release of future videos. 

An overview of the project is presented in this [video](https://www.youtube.com/watch?v=4XS8u6wuXDQ&t=100s). 

## Dependencies

### Python 3.10
The example was tested using Python 3.10 on Windows, Linux, and MacOS platforms. 

### OpenAI package
Install with 'pip3 install openai'. 

An OpenAI API key is required. It is obtained by creating an account with OpenAI. Add the key to the openai.key.  

### FakeYou package
To use FakeYou as a text to speech provider, install with 'pip3 install fakeyou'.

An FakeYou login and password are required. Create them by registering an account at [FakeYou](https://fakeyou.com/). Add them to the fakeyou.key file. 

### ElevenLabs package
To use ElevenLabs as a text to speech provider, install with 'pip3 install elevenlabs'.

An ElevenLabs API key is required. It is obtained by creating an account with [ElevenLabs](https://elevenlabs.io/). Add the key to the elevenlabs.key file.

### Other dependencies
Run this command to install other required packages.
'pip3 install sounddevice soundfile'

## Executables

test_ai.py - This is a basic script for testing the ChatGPT functionality. It takes in input from the console and outputs ChatGPT's response. It benchmarks and displays the time it took to receive the response. The elapsed time is an important consideration for an engauging interactive experience. 

test_tts.py - This is a basic script for testing voice provider functionality. It takes in input from the console and synthesizes it into speech. It benchmarks and displays the time it took to receive the response. The elapsed time is an important consideration for an engauging interactive experience.

open_teddy.py - This will take in a request entered at the console, send it to ChatGPT for a response, and then speak the response. 
