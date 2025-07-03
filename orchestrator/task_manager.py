
from agents.langchain_agent import create_langchain_agent

class TaskManager:
    def __init__(self):
        self.agent = create_langchain_agent()

    def handle_task(self, query):
        return self.agent.run(query)
