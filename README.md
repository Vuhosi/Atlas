# Atlas
Atlas - Yet Another (AI) Agentic Framework

Our Inhouse Framework to create custom AI Agents with ease and zero coupling

### Assistants:
![demo](./assets/demo.png)

### Conversational Persona Bots:
![demo](./assets/persona.png)

> So the thing is, Crewai is underwhelming when I had to deploy crews to prod. They were "unreliable" and dissapointing. Same goes for other abstractions created by other organisations. So I decided to create my own low coupling abstraction (on top of openai assistants and function calling), trying to create a simplified, less bloated framework which we will use internally for our usecase.


The goal is simple: Keep the flow of mutliple agents pipeline sequential.


## Outline:
4 Different types of AI Agents
* Assistants: Uses openai assistants under the hood. Function calling + Fast
* Persona Bot Assistants: Assistants in a loop with the user
* ReAct based Agents: Run a Reasoning and Action loop to get things done
* PAL Agents: Program-Aided Language models built for problem solving


## Todo:
- [ ] Completely different way to prompt: 
objective, context, instruction, output, examples

- [ ] Collaboration vs Sequential work flow:
Sequential is easy to implement, collaborative is something which will help

- [ ] Feedback mechanism:
naive way implementation
