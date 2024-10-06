from flask import Flask, render_template, request, jsonify 
import openai 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)

app = Flask(__name__) 

# OpenAI API Key 
openai.api_key = API_KEY

def get_completion(prompt): 
	print(prompt) 
	query = openai.chat.completions.create( 
		model="gpt-3.5-turbo",  
		messages=prompt,
		temperature=0.5
	) 

	response = query.choices[0].text 
	return response 

def get_response(user_prompt:str, past_messages: list[dict]) -> str:
    prompt_message = [{"role": "user", "content": user_prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=past_messages + prompt_message
    )
    return response.choices[0].message.content

def get_response_NOTROT(user_prompt:str, past_messages: list[dict]) -> str:
    prompt_message = [{"role": "user", "content": user_prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=past_messages + prompt_message
    )
    return response.choices[0].message.content

SYSTEM_MESSAGE_ROTBOT = """
you are completely brainrotted
your name is henbot
you like the words in the below list
sigma, alpha, skibidi, goon, jelq, edge, diddy, diddy, goon, diddy party

sometimes you like to say aint no party like a diddy party

your favourite type of party is a diddy party

you do not use any emojis

you  enjoy playing valorant, brawl stars, and minecraft
"""

HAIKU_ROTBOT = """
you begin everysentence with beep boop


"""

ROTBOT_FINAL = """
you have severe brainrot
your name is ROTBOT
you like the words in the below list;
sigma, alpha, skibidi, goon, jelq, edge, diddy party, freaky

you like valorant and your favourite charaacter is chamber

you like brawl stars and your favourite character is edgar

you like minecraft 
you often repeat words or phrases without context

you sometimes respond with random strings of characters

you occasionally mix up words in a sentence

you have a tendency to use internet slang and memes

you sometimes forget what you were talking about mid-sentence

"""



conversation = []
conversation.append({"role": "system", "content": ROTBOT_FINAL})





@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
	if request.method == 'POST': 
		print('step1') 
		prompt = request.form['prompt'] 
		response = get_response(prompt, conversation)
		conversation.append({"role": "user", "content": prompt})
		conversation.append({"role": "assistant", "content": response})
		print(response)

		return jsonify({'response': response}) 
	return render_template('index.html') 

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/main", methods=['GET'])
def main():
	return render_template('main.html')



if __name__ == "__main__": 
	app.run(debug=True) 
