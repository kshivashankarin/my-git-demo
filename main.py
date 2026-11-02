from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatbotRequest(BaseModel):
    message: str

class ChatbotResponse(BaseModel):
    response: str

@app.post('/my-chatbot')
def my_chat_bot(request:ChatbotRequest):

    return ChatbotResponse(response="Hello")
    return {
        "message" : "My Simple chatbot"
    }