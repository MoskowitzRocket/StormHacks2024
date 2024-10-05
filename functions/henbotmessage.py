from dotenv import load_dotenv
import os
from openai import OpenAI

import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)




def get_response(user_prompt:str, past_messages: list[dict]) -> str:
    prompt_message = [{"role": "user", "content": user_prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=past_messages + prompt_message
    )
    return response.choices[0].message.content