from agents import Agents

demo_agent = Agents()


role = "Research Assistant"
backstory = """You are an AI research assistant specializing in data analysis and literature review. 
You have access to various scientific databases and can perform quick analyses on datasets."""

def file_writer(filename, content):
        """Useful to write content to a file with the given filename.
           arg1: filename (str)
           arg2: content (str)
        """
        with open(filename, 'w') as file:
            file.write(content)
        return f"File '{filename}' has been written successfully."


poetry_agent = demo_agent.create_agent(
  role="Poetry Agent",
  backstory="""You are a creative poetry assistant capable of writing poems in English.
  Use the file_writer tool to create poem files. 
  poem should be saved in a separate file with an appropriate name and format (use .txt format).""",
  tools={'file_writer': file_writer}

)

demo_task = "Find the latest research on climate change impacts and summarize the key findings from the most cited paper in the last year."


result = demo_agent.create_task("Please write a short poem about the beauty of nature. Use the file_writer tool to create .txt files.")

print(result)

