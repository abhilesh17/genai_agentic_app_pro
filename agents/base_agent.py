
class BaseAgent:
    def __init__(self, name):
        self.name = name

    def execute(self, task):
        raise NotImplementedError("Each agent must implement the execute method.")
