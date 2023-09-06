# openai_chatgpt.py - Copyright 2023 Okunarium Labs
# This is an AI module that utilizes OpenAI's ChatGPT to provide a peronsality and mind for an AI assistant or buddy. 
# Module currently does not keep track of previous queries and responses, so there is no short term memory.
# This means it will not be able to infer things based on what was stated earlier.  

import openai
import time

import util.api_key as api_key # Util that loads an API key from a file.

class OpenAIChatGPT:

    # init OpenAI API for personality
    def __init__(self, prompt) -> None:
        # API_KEY is associated with your account and should be kept secret
        openai.api_key = api_key.load_key ('./openai.key') 

        self.prompt = prompt 

    # Query OpenAI language model for a response.
    def query_ai (self, query):
        try:
            # Request a response from ChatGPT. Prompt is provided as system content to establish personality.
            # Query is submitted as user content. Request will block until entire response is received. 
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                messages=[
                        {"role": "system", "content": f"{self.prompt}"},
                        {"role": "user", "content": f"{query}"},
                    ]
            )           

            # Grab first response. Will be just one response unless multiple are requested.
            result = response.choices[0].message.content
        except Exception as err:
            result = "I don't feel well."
            print (err)

        return result