from llm import OllamaModel
from prompt import system_prompt 
import json

class Agents():
    def __init__(self):
        self.messages = []
        self.system_prompt = system_prompt
        
    def create_agent(self, role, backstory, tools):
        agent_prompt = f""" Role: {role}\nBackstory: {backstory}\n\n
        """ + f"""Available tools: {tools}""" + self.system_prompt
        self.system_prompt = agent_prompt
        self.messages.append({"role": "system", "content": self.system_prompt})

    def create_task(self, task):
        max_iterations = 3 
        i = 0
        self.messages.append({"role": "user", "content": task})
        while(i < max_iterations):
            result = OllamaModel.ollama_completion(self.messages)

            print(result)
            i = i + 1

