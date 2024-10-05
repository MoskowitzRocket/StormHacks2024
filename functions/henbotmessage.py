from dotenv import load_dotenv
import os
from openai import OpenAI
from functions.henbotmessage import *

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)
 

def henbotmessage(system_message: str, user_input: str, num_responses) -> str:
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        # Provide the context to the system
        {"role": "system", "content": system_message},

        # Provide the text from the user
        {"role": "user", "content": user_input},
      ],

      # Tell the model to generate `num_suggestions` suggestions
      n=num_responses,

      # Higher temperature = more random results
      temperature=1.5
    )
    return [suggestion.message.content for suggestion in completion.choices]