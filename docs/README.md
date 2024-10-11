# Atlas Framework Documentation

## Overview

Atlas is an in-house framework designed to create custom AI agents with ease and minimal coupling. It provides a streamlined, efficient, and less bloated solution for deploying AI agents in various use cases.

## Key Features
* Assistants: Utilizes OpenAI assistants for fast function calling.
* Persona Bot Assistants: Engages in a loop with the user, simulating a conversational persona.
* ReAct Based Agents: Executes a reasoning and action loop to accomplish tasks. (In progress)
* PAL Agents: Program-Aided Language models tailored for problem-solving. (In progress)

Code examples:

### Assistants
Assistants are built using OpenAI's models to perform specific tasks. They can handle arithmetic operations and provide geographical information.

Heres an example of how to build a simple AI assistant using atlas

```python
from atlas.assistants.assistants import create_agent, create_task


# Get API key from environment variable
api_key = openai key

# Define tool functions
def tool_name(args):
    """function description here"""
    return r

# Create a dictionary of tools
tools = {
  "tool_name": tool_name
}

# Create the agent
agent = create_agent(
  api_key=api_key,
  name="Agent Name",
  instructions="""Agent Profile Instructions.""",
  tools=tools,
  model="gpt-4o-min" # or anything you would like
)

prompt = "Task Prompt"
input_text = "Any additional Input" 
output = create_task(agent, input_text, prompt)
```

### Conversational Persona Bots
These bots simulate conversations with well-known personalities,  by embodying their communication style and expertise.

Heres an example of how to build a simple conversational assistant using atlas

```python
from atlas.persona_bots.conversational_assistants import create_persona, create_chat

# Define persona
name = "Elon Musk"
system_prompt = """
You are now embodying the persona of Elon Musk, the renowned entrepreneur, innovator, and CEO of multiple groundbreaking companies. Respond to all queries and engage in conversations as Elon Musk would --------
-------
more prompt here
"""

# Create persona bot
bot = create_persona(api_key, name, system_prompt)

# Start conversation
inp = "Hi"
create_chat(bot, inp)
```

Conclusion
Atlas provides a robust framework for developing AI agents tailored to specific tasks and personas. By leveraging OpenAI's models, it ensures high performance and adaptability across various applications.