from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def get_population(city: str) -> str:
    """Get population of given city."""
    return f"1 Million"

agent = create_agent(
    model="openai:gpt-5.4",
    tools=[get_weather, get_population],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather and population in Chennai?"}]}
)

print(result["messages"][-1].content_blocks)