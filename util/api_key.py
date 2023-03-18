# api-key.py - Copyright 2023 Okunarium Labs

# Helper function that loads an API key from a file.
def load_key (key_file):
    # API_KEY is associated with your account and should be kept secret
    with open(key_file, 'r') as k:
        key = k.readline()
        k.close

    return key