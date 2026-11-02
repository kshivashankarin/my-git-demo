from openai import OpenAI
import os

from dotenv import load_dotenv


load_dotenv()


key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = key
)

history = []

while True:

    user_input = input("User: ")

    if user_input == "stop":
        print("Exiting here.......")
        break

    history.append({
        "role" : "user",
        "content" : user_input
    })

    print(history)
    
    response = client.responses.create(
        model = 'gpt-5.4-mini',
        input = history
    )

    res = response.output_text

    history.append({
        "role" : "assistant",
        "content" : res
    })

    print("AI : " + response.output_text)