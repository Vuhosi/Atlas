import requests
import json
from openai import OpenAI

class OllamaModel():
    def ollama_completion(prompt, model="nemotron-mini"):
      """
      Generate a response from Ollama API.
      
      Args:
      prompt (str): The input prompt for the model.
      model (str): The name of the model to use. Defaults to "llama2".
      
      Returns:
      str: The generated response from the model.
      """
      client = OpenAI(
        base_url = 'http://localhost:11434/v1',
        api_key='ollama', # required, but unused
      )
      
      try:
          response = client.chat.completions.create(
        model="llama3.2:3b",
              messages= prompt
          ) 
          # print(response.choices[0].message.content.thought)
          return response.choices[0].message.content
      except Exception as e:
          return f"Error: {str(e)}"

class AnthropicModel():
    def anthropic_completion():
        pass

class OpenaiModel():
    def openai_completion():
        pass
