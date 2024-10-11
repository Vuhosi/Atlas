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
from src.assistants.assistants import AIAssistantFramework



class ConversationalAssistant(AIAssistantFramework):
  def __init__(self, api_key, model, name, system_prompt):
      super().__init__(api_key, model)
      self.name = name
      self.system_prompt = system_prompt
      self.thread = None

  def initialize(self):
      instructions = self.system_prompt

      self.create_assistant(self.name, instructions, {})
      self.thread = self.create_thread()

  def chat(self, user_input):
      self.add_message(self.thread.id, user_input)
      self.run_assistant(self.thread.id)
      response = self.get_response(self.thread.id)
      return response


def create_persona(api_key, name, system_prompt, model="gpt-4o"):
  chat_bot = ConversationalAssistant(api_key, model, name, system_prompt)
  chat_bot.initialize()
  console = Console()
  message = (
      f":brain: [bold magenta]{name}[/bold magenta] "
      f"[green]initialized[/green]\n"
      f"[yellow]Domain:[/yellow] [blue]{system_prompt}[/blue]\n"
  )
  panel = Panel(
      message,
      title="[bold red]Conversational Agent Profiling Successful[/bold red]",
      border_style="green",
      expand=False
  )
  console.print(panel)
  return chat_bot

def create_chat(chat_bot, initial_input):
    console = Console()
    console.print(f"[bold green]Chat with {chat_bot.name} started. Type 'exit' to end the conversation.[/bold green]")

    # Handle the initial input
    response = chat_bot.chat(initial_input)
    console.print(f"[bold magenta]{chat_bot.name}:[/bold magenta] {response}")

    while True:
      user_input = console.input("[bold cyan]You:[/bold cyan] ")
      
      if user_input.lower() == 'exit':
          break
      
      response = chat_bot.chat(user_input)
      console.print(f"[bold magenta]{chat_bot.name}:[/bold magenta] {response}")

    console.print("[bold green]Chat ended.[/bold green]")
