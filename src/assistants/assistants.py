import openai
import time
from dotenv import load_dotenv
import os
import json
import inspect
from typing import get_type_hints
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint


class AIAssistantFramework:
    def __init__(self, api_key, model):
      openai.api_key = api_key
      self.assistant = None
      self.model = model
      self.tools = {}

    def create_assistant(self, name, instructions, tools):
        tool_definitions = []
        for tool_name, tool_func in tools.items():
          tool_definition = {
              "type": "function",
              "function": {
                  "name": tool_name,
                  "description": tool_func.__doc__ or f"Function to {tool_name}",
                  "parameters": {
                      "type": "object",
                      "properties": {},
                      "required": []
                  }
              }
          }

          # Get function signature
          signature = inspect.signature(tool_func)
          type_hints = get_type_hints(tool_func)

          for param_name, param in signature.parameters.items():
              param_type = type_hints.get(param_name, str).__name__
              tool_definition["function"]["parameters"]["properties"][param_name] = {
                  "type": self._get_json_type(param_type),
                  "description": f"Parameter: {param_name}"
              }
              # Check if the parameter is required
              if param.default == inspect.Parameter.empty:
                  tool_definition["function"]["parameters"]["required"].append(param_name)

          tool_definitions.append(tool_definition)
          self.tools[tool_name] = tool_func

        self.assistant = openai.beta.assistants.create(
          name=name,
          instructions=instructions,
          model=self.model,
          tools=tool_definitions
        )
        return self.assistant

    def _get_json_type(self, python_type):
      type_mapping = {
          'str': 'string',
          'int': 'integer',
          'float': 'number',
          'bool': 'boolean',
          'list': 'array',
          'dict': 'object'
      }
      return type_mapping.get(python_type, 'string')

    def create_thread(self):
      return openai.beta.threads.create()

    def add_message(self, thread_id, content):
      openai.beta.threads.messages.create(
          thread_id=thread_id,
          role="user",
          content=content
      )

    def run_assistant(self, thread_id):
      run = openai.beta.threads.runs.create(
          thread_id=thread_id,
          assistant_id=self.assistant.id
      )
      while True:
          run_status = openai.beta.threads.runs.retrieve(
              thread_id=thread_id,
              run_id=run.id
          )
          if run_status.status == 'completed':
              break
          elif run_status.status == 'requires_action':
              self.handle_tool_calls(thread_id, run.id, run_status.required_action.submit_tool_outputs.tool_calls)
          time.sleep(1)

    def handle_tool_calls(self, thread_id, run_id, tool_calls):
      tool_outputs = []
      for tool_call in tool_calls:
          if tool_call.function.name in self.tools:
              func = self.tools[tool_call.function.name]
              args = json.loads(tool_call.function.arguments)

              try:
                  result = func(**args)
                  tool_outputs.append({
                      "tool_call_id": tool_call.id,
                      "output": json.dumps(result)
                  })
              except Exception as e:
                  print(f"Error calling {tool_call.function.name}: {str(e)}")
                  tool_outputs.append({
                      "tool_call_id": tool_call.id,
                      "output": json.dumps({"error": f"Failed to execute {tool_call.function.name}: {str(e)}"})
                  })

      openai.beta.threads.runs.submit_tool_outputs(
          thread_id=thread_id,
          run_id=run_id,
          tool_outputs=tool_outputs
      )

    def get_response(self, thread_id):
      messages = openai.beta.threads.messages.list(thread_id=thread_id)
      return messages.data[0].content[0].text.value

    def generate_output(self, input_text, prompt):
      thread = self.create_thread()
      self.add_message(thread.id, f"Input: {input_text}")
      self.add_message(thread.id, prompt)
      self.run_assistant(thread.id)
      return self.get_response(thread.id)

def create_agent(api_key, name, instructions, tools, model="gpt-4o-mini"):
    framework = AIAssistantFramework(api_key, model)
    framework.create_assistant(name, instructions, tools)
    console = Console()
    message = (
          f":brain: [bold magenta]{name}[/bold magenta] "
          f"[green]initialized[/green]\n"
          f"[yellow]Model:[/yellow] [blue]{model}[/blue]\n"
          f"[yellow]Tools:[/yellow] [blue]{', '.join(tools)}[/blue]"
      )
    panel = Panel(
      message,
      title="[bold red]Agent Profiling Successful[/bold red]",
      border_style="green",
      expand=False
    )
    console.print(panel)
    return framework

def create_task(agent, input_text, prompt, output_dir=None, output_file=None):
    output = agent.generate_output(input_text, prompt)
    console = Console()
    output_panel = Panel(
      output,
      title="[bold green]Initiating Task[/bold green]",
      border_style="blue",
      expand=False
    )
    console.print(output_panel)
    if output_dir and output_file:
        # Create the directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Construct the full file path
        output_file_path = os.path.join(output_dir, output_file)

        # Write the output to the file
        with open(output_file_path, 'w') as file:
            file.write(output)
            rprint(f"[bold green]✅ Output saved:[/bold green] [blue underline]{output_file_path}[/blue underline]")
    return output


