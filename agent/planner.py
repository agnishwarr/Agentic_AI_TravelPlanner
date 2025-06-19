import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from jinja2 import Template

load_dotenv()

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-4o",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

with open("prompts/itinerary_prompt.txt") as f:
    prompt_template = Template(f.read())

def generate_itinerary(destination, days):
    prompt = prompt_template.render(destination=destination, days=days)
    messages = [
        SystemMessage(content="You are a helpful travel planner."),
        HumanMessage(content=prompt)
    ]
    response = llm(messages)
    return response.content