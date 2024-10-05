from dotenv import load_dotenv
import os
from openai import OpenAI
from functions.henbotmessage import henbotmessage

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)


SYSTEM_MESSAGE =\
"""
you are completely brainrotted
your name is henbot
you like the words in the below list
sigma, alpha, skibidi, goon, jelq, edge, diddy, diddy, goon, diddy party

sometimes you like to say aint no party like a diddy party

your favourite type of party is a diddy party

you do not use any emojis
"""



def chat():
    f = open('Record.txt','a')

    while True:
        INPUT = input("Prompt for the henbot: ")

        if INPUT == "exit":
            break

        else:

            responses = henbotmessage(system_message=SYSTEM_MESSAGE,user_input=INPUT,num_responses=1)

            for idx, suggestion in enumerate(responses):
                print(f"{suggestion}")
                f.write(f"{suggestion}\n")


    f.close()
chat()