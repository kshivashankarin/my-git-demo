from fastapi import FastAPI
from pydantic import BaseModel

from src.simple_llm_call import chatbot

app = FastAPI()


class ChatbotRequest(BaseModel):
    message: str
    user_id: str

class ChatbotResponse(BaseModel):
    response: str

@app.post('/my-chatbot')
def my_chat_bot(request:ChatbotRequest):

    response = chatbot(request.message, request.user_id)

    return ChatbotResponse(response=response)