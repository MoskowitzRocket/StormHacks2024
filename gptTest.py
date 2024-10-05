import openai

openai.ai_key = "Needs a working key"
def testing(input):
     response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[{"role":"user","content": "input"}]
     )

     return response.choices[0].message.content.strip()

if __name__ == "__main__":
     
    while True:
         user_input = input("You: ")
         if user_input.lower() in ["quit","exit","bye"]:
             break
    response = testing(user_input)
    print("Saffat: ", response)