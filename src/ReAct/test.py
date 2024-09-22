from agents import Agents



# Create a demo agent
demo_agent = Agents()

# Define the role, backstory, and tools for the demo agent
role = "Research Assistant"
backstory = """You are an AI research assistant specializing in data analysis and literature review. 
You have access to various scientific databases and can perform quick analyses on datasets."""

tools_json = """{
  "Internet Access": {
      "description": "Search the internet for recent information",
      "params": {
          "query": "string"
      }
  },
  "analyze_dataset": {
      "description": "Perform basic statistical analysis on a given dataset",
      "params": {
          "dataset_url": "string",
          "analysis_type": "string"
      }
  },
  "summarize_paper": {
      "description": "Provide a summary of a scientific paper",
      "params": {
          "paper_url": "string"
      }
  }
}
"""

# Create the agent with the defined role, backstory, and tools
demo_agent.create_agent(role, backstory, tools_json)

# Define a demo task for the agent
demo_task = "Find the latest research on climate change impacts and summarize the key findings from the most cited paper in the last year."

# Execute the task
demo_agent.create_task(demo_task)
