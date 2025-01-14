Atlas is an in-house framework designed to create custom AI Agents with ease and zero coupling. Built by Vuhosi, Atlas aims to provide a simplified, less bloated alternative to existing AI agent frameworks.



## Overview

Atlas was born out of the need for a more reliable and efficient AI agent framework. After experiencing underwhelming results with existing solutions like Crewai in production environments, we decided to create our own low-coupling abstraction on top of OpenAI's assistants and function calling capabilities.

The primary goal of Atlas is to maintain a sequential flow of multiple agents in a pipeline, providing a streamlined approach to AI agent development and deployment.

## Features

- Zero coupling design for flexibility and ease of use
- Built on top of OpenAI's assistants and function calling
- Simplified, less bloated framework
- Sequential flow of multiple agents in a pipeline
- Four different types of AI Agents to suit various use cases
- Customizable prompting system

## Installation
`pip install vuhosi-atlas`

## Agent Types

Atlas supports four different types of AI Agents:

1. **Assistants**: Utilizes OpenAI assistants under the hood, combining function calling for fast and efficient operations.

   ![Assistants Demo](./assets/demo.png)

2. **Conversational Persona Bots**: Assistants in a loop with the user, designed for interactive conversations.

   ![Persona Bots Demo](./assets/persona.png)

3. **ReAct-based Agents**: Implements a Reasoning and Action loop to accomplish tasks effectively.

4. **PAL Agents**: Program-Aided Language models built for complex problem-solving scenarios.


## Quick Start
Build an agent in just 4 lines of code

```python
from vuhosi_atlas.assistants.assistants import create_agent, create_task

api_key = "OPENAIAPIKEY"

agent = create_agent(api_key, name, instructions, tools)
create_task(agent, input, prompt)
```




## Roadmap

- [ ] Implement ReAct based agents

- [ ] Implement PAL based agents

- [ ] Implement a new prompting system:
  - Objective
  - Context
  - Instruction
  - Output
  - Examples

- [ ] Develop collaboration workflow:
  - Current focus is on sequential workflows
  - Future plans to implement collaborative agent interactions

- [ ] Integrate feedback mechanism:
  - Initial implementation of a naive feedback system

## Why Atlas?

Atlas addresses the reliability issues faced with other frameworks when deploying AI crews to production environments. By creating a custom, low-coupling abstraction, we aim to provide a more dependable and efficient solution for AI agent development and deployment.

---

Built with ❤️ by Vuhosi
