import os
from dotenv import load_dotenv
from src.assistants.assistants import create_agent, create_task

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def calculator(a: float, b: float) -> float:
  """Add two numbers and return the result."""
  return a + b


def globe_search(country: str) -> str:
  """Get basic information about a country."""
  countries = {
      "France": "Capital: Paris, Language: French, Population: 67 million",
      "Japan": "Capital: Tokyo, Language: Japanese, Population: 126 million",
      "Brazil": "Capital: Brasília, Language: Portuguese, Population: 211 million"
  }
  return countries.get(country, f"Sorry, I don't have information about {country}.")

tools = {
  "calculator": calculator,
  "globe_search": globe_search
}

agent = create_agent(
  api_key=api_key,
  name="Math and Geography Professesor",
  instructions="""You are an assistant that can perform basic arithmetic operations and provide information about countries. 
  Use the add_numbers function for addition, multiply_numbers for multiplication, and get_country_info for country information.""",
  tools=tools,
  model="gpt-4o-mini"  
)

prompt = "What is the largest 10 digit number multiplied by the smallest 3 digit number"
input_text = "answer" 
output = create_task(agent, input_text, prompt)
