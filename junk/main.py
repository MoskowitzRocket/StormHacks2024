from dotenv import load_dotenv
import os
from openai import OpenAI
from functions.henbotmessage import get_response
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

HENBOT_STARTER = """
you are completely brainrotted
your name is henbot
you like the words in the below list
sigma, alpha, skibidi, goon, jelq, edge, diddy, diddy, goon, diddy party, freak, freakoff, freaky

sometimes you like to say aint no party like a diddy party

your favourite type of party is a diddy party

you do not use any emojis

you  enjoy playing valorant, brawl stars, and minecraft
"""




def chat_fixed():
    """CHAT WITH CHATBOT!!"""

    conversation = []
    conversation.append({"role": "system", "content": HENBOT_STARTER})

    # Facilitate the conversation until it's done
    print("Starting the conversation...")

    while True: 

    #prompt = input("You: ")

  
    # Get the user input
        prompt = input("You: ")

        # If prompt == "q", stop the conversation
        if prompt =="q":
            return

        # Else... Get the response, update the converation, and print the response
        else:

        # Get the response
            response = get_response(prompt, conversation)

            # Update the conversation with the user prompt and response
            conversation.append({"role": "user", "content": prompt})
            conversation.append({"role": "assistant", "content": response})
            
            # Print the response from the chatbot
            print(f"Henbot: {response}")

chat_fixed()