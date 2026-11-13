
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel
from pypdf import PdfReader

from pathlib import Path
 
class ModelResponse(BaseModel):
    response: str
    confidence: float

information = """
Sachin : Sachin full name is anish bala sachin. He is my collage friend. We studied together in our UG on 2016 to 2019
Bennu : Bennu is my previous company friend, we both worked  together in exalogic consulting.
"""

path = Path("data")

file = path / "research.pdf"

reader = PdfReader(file)

information = ""

for page in reader.pages:
    information += page.extract_text()


agent = create_agent(
    model="openai:gpt-4.1",
    system_prompt=f"""
    You are a help assistant chatbot.

    Use only the below information to answer.
    {information}
    """,
    checkpointer=InMemorySaver(),
    response_format=ModelResponse
)


def invoke_chat(user_msg: str, config):
        
    result = agent.invoke(
        {
            "messages" : [
                {
                    "role" : "user",
                    "content" : user_msg
                }
            ]
        },
        config=config
    )

    return result["messages"][-1].content_blocks