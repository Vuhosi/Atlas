from llm import OllamaModel
from prompt import system_prompt 
class Agents():
    def __init__(self):
        self.messages = []
        self.system_prompt = system_prompt
        
    def create_agent(role, backstory, tools_json):
        agent_prompt = f""" Role: {role}\nBackstory: {backstory}\n\n
        """ + f"""Available tools: {tools_json}""" + self.system_prompt
        self.system_prompt = agent_prompt
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def create_task(task):
        max_iterations = 3
        i = 0
        while(i < max_iterations):
            self.messages.append({"role": "user", "content": task})
            result = OllamaModel(self.messages)
            print(result)
