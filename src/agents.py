from llm import OllamaModel
from prompt import system_prompt 
class Agents():
    def __init__(self):
        self.messages = []
        self.system_prompt = system_prompt
        

    def create_agent(role, backstory):
        agent_prompt = f"Role: {role}\nBackstory: {backstory}\n\n" + self.system_prompt
        self.system_prompt = agent_prompt
        if self.system:
            self.messages.append({"role": "system", "content": system})


    def run_agent(task):
        

