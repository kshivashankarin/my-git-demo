from openai import OpenAI
import os

from dotenv import load_dotenv


load_dotenv()


key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = key
)

history = []

def chatbot(user_input):

    print(history)

    history.append({
        "role" : "user",
        "content" : user_input
    })

    
    response = client.responses.create(
        model = 'gpt-5.4-mini',
        input = history
    )

    res = response.output_text

    history.append({
        "role" : "assistant",
        "content" : res
    })


    return res