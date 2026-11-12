from fastapi import FastAPI
from pydantic import BaseModel
import json

from src.simple_llm_call import chatbot
from src.langchain_chat import invoke_chat
from langchain_core.utils.uuid import uuid7



app = FastAPI()


class ChatbotRequest(BaseModel):
    message: str
    thread_id: str


class ChatbotResponse(BaseModel):
    response: dict
    thread_id: str

@app.post('/my-chatbot')
def my_chat_bot(request:ChatbotRequest):

    if not request.thread_id:
        thread_id = str(uuid7())
    else:
        thread_id = request.thread_id

    config = {"configurable": {"thread_id": thread_id}}

    response = invoke_chat(request.message, config)

    final_response = response[0]['text']
    
    final_response = json.loads(final_response)



    return ChatbotResponse(response=final_response, thread_id=thread_id)