import requests
import json


class OllamaModel():
    def ollama_completion(prompt, model="llama3.1"):
      """
      Generate a response from Ollama API.
      
      Args:
      prompt (str): The input prompt for the model.
      model (str): The name of the model to use. Defaults to "llama2".
      
      Returns:
      str: The generated response from the model.
      """
      url = "http://localhost:11434/api/generate"
      
      payload = {
          "model": model,
          "prompt": prompt
      }
      
      try:
          response = requests.post(url, json=payload, stream=True)
          
          if response.status_code == 200:
              full_response = ""
              for line in response.iter_lines():
                  if line:
                      decoded_line = line.decode('utf-8')
                      try:
                          json_line = json.loads(decoded_line)
                          if 'response' in json_line:
                              full_response += json_line['response']
                          if json_line.get('done', False):
                              break
                      except json.JSONDecodeError:
                          print(f"Error decoding JSON: {decoded_line}")
              
              return full_response
          else:
              return f"Error: {response.status_code}\n{response.text}"
      
      except requests.exceptions.RequestException as e:
          return f"Request failed: {str(e)}"

class AnthropicModel():
    def anthropic_completion():
        pass

class OpenaiModel():
    def openai_completion():
        pass
