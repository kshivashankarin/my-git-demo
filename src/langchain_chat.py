
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel

 
class ModelResponse(BaseModel):
    response: str
    confidence: float

agent = create_agent(
    model="openai:gpt-4.1",
    system_prompt="You are a help assistant chantbot.",
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