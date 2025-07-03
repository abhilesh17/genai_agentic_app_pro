
from langchain.chat_models import ChatGroq
from langchain.agents import initialize_agent, Tool
from tools.web_search_tool import WebSearchTool
from tools.summarizer_tool import SummarizerTool
from tools.memory_tool import get_memory
import os

def create_langchain_agent():
    llm = ChatGroq(
        temperature=0,
        model_name="mixtral-8x7b-32768",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    tools = [
        Tool.from_function(
            func=WebSearchTool().search,
            name="Web Search",
            description="Searches the web for a given topic"
        ),
        Tool.from_function(
            func=SummarizerTool().summarize,
            name="Summarizer",
            description="Summarizes a given block of text"
        )
    ]

    memory = get_memory()

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="chat-conversational-react-description",
        memory=memory,
        verbose=True
    )
    return agent
