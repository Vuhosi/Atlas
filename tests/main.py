import os
from dotenv import load_dotenv
from yaaf import create_agent, create_task

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Define tool functions
def add_numbers(a: float, b: float) -> float:
  """Add two numbers and return the result."""
  return a + b

def multiply_numbers(a: float, b: float) -> float:
  """Multiply two numbers and return the result."""
  return a * b

def get_country_info(country: str) -> str:
  """Get basic information about a country."""
  # This is a mock function. In a real scenario, you might want to use an API or database.
  countries = {
      "France": "Capital: Paris, Language: French, Population: 67 million",
      "Japan": "Capital: Tokyo, Language: Japanese, Population: 126 million",
      "Brazil": "Capital: Brasília, Language: Portuguese, Population: 211 million"
  }
  return countries.get(country, f"Sorry, I don't have information about {country}.")

# Create a dictionary of tools
tools = {
  "add_numbers": add_numbers,
  "multiply_numbers": multiply_numbers,
  "get_country_info": get_country_info
}

# Create the agent
agent = create_agent(
  api_key=api_key,
  name="Math and Geography Assistant",
  instructions="""You are an assistant that can perform basic arithmetic operations and provide information about countries. 
  Use the add_numbers function for addition, multiply_numbers for multiplication, and get_country_info for country information.""",
  tools=tools,
  model="gpt-4-0613"  # or whichever model you prefer
)

# Test the agent with some tasks
tasks = [
  ("What is 15 + 27?", "Please calculate 15 + 27."),
  ("What is 8 * 9?", "Please calculate 8 * 9."),
  ("Tell me about France.", "Provide information about France."),
  ("What's the capital of Japan?", "Provide information about Japan and extract its capital.")
]

for input_text, prompt in tasks:
  print(f"\nTask: {input_text}")
  output = create_task(agent, input_text, prompt)
  print(f"Response: {output}")
