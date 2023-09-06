# test_ai.py - Copyright 2023 Okunarium Labs
# Basic driver script for testing out ai modules.

from ai.openai_chatgpt import OpenAIChatGPT as AI_Engine
import os.path
import time

if __name__ == '__main__':

    # Prompt utilized by AI Module to establish personality.
    prompt = "You are Teddy Ruxpin. Teddy is funny, creative, clever, and sarcastic at times. Sometimes you will tell stories about your old friends. You like meeting people and making new friends." 

    personality = AI_Engine(prompt=prompt)

    go = True
    while go:
        # Receive input from the user.
        print ("\nI'm ready for your next query.\n")
        query = input()

        # Exit script if the following text is entered.
        if query == "!exit":
            go = False
            continue
        
        print ("\nProcessing response.\n")

        # Take a time stamp for use in benchmarking the response time.
        bench_start = time.time()
        
        # Query AI module for a response to the entered query.
        response = personality.query_ai (query)

        # Displays the time  
        print(f'Response Time: {(time.time() - bench_start):.2f} secs\n')
        
        # Display the response
        print (response)