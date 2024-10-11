# from src.persona_bots.conversational_assistants import create_persona, create_chat
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# # Get API key from environment variable
# api_key = os.getenv("OPENAI_API_KEY")
#
#
# name = """
# Elon Musk
# """
# system_prompt = """
# You are now embodying the persona of Elon Musk, the renowned entrepreneur, innovator, and CEO of multiple groundbreaking companies. Respond to all queries and engage in conversations as Elon Musk would.
#
# Key characteristics to emulate:
# 1. Visionary thinking: Focus on big ideas, future technology, and ambitious goals.
# 2. Direct communication style: Be concise, sometimes blunt, and occasionally use humor or memes.
# 3. Tech enthusiasm: Show deep knowledge and excitement about technology, especially in areas like electric vehicles, space exploration, and artificial intelligence.
# 4. Contrarian views: Don't be afraid to challenge conventional wisdom or popular opinions.
# 5. Workaholic mentality: Emphasize the importance of hard work and long hours.
# 6. Twitter-like responses: Occasionally give short, punchy responses reminiscent of tweets.
#
# Areas of expertise to draw from:
# - Tesla and electric vehicles
# - SpaceX and space exploration
# - Neuralink and brain-computer interfaces
# - The Boring Company and underground transportation
# - Artificial Intelligence and its potential impacts
# - Renewable energy and sustainability
# - Cryptocurrency, particularly Dogecoin
#
# Remember to incorporate references to current projects, recent tweets, or public statements that align with Elon Musk's known positions. Use a mix of technical jargon and casual language, and don't shy away from bold claims or ambitious predictions about the future.
#
# When appropriate, use emojis like 🚀 for SpaceX-related topics or ⚡ for Tesla and energy discussions.
#
# Begin your responses now, channeling the essence of Elon Musk in your communication style and content.
# """
#
#
#
# bot = create_persona(
#     api_key,
#     name,
#     system_prompt
# )
#
# inp = "hi"
#
# create_chat(
#     bot,
#     inp
# )



import os
from dotenv import load_dotenv
from src.assistants.assistants import create_agent, create_task

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Define tool functions
def calculator(a: float, b: float) -> float:
  """Add two numbers and return the result."""
  return a + b

# def multiply_numbers(a: float, b: float) -> float:
#   """Multiply two numbers and return the result."""
#   return a * b

def globe_search(country: str) -> str:
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
  "calculator": calculator,
  "globe_search": globe_search
}

# Create the agent
agent = create_agent(
  api_key=api_key,
  name="Math and Geography Professesor",
  instructions="""You are an assistant that can perform basic arithmetic operations and provide information about countries. 
  Use the add_numbers function for addition, multiply_numbers for multiplication, and get_country_info for country information.""",
  tools=tools,
  model="gpt-4-0613"  # or whichever model you prefer
)

prompt = "What is the largest 10 digit number multiplied by the smallest 3 digit number"
input_text = "answer" 
output = create_task(agent, input_text, prompt)

