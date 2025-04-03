from google import genai
import os
import io
from IPython.display import Markdown, clear_output

from google.genai import types

# Replace with your actual Gemini API key or get it from an environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    api_key = "YOUR_GEMINI_API_KEY" #Or assign directly, but not recommended for security
    print("Warning: GEMINI_API_KEY environment variable not set.  Using direct assignment (not recommended).")

# API key has been exported as a environment variable:
# export GEMINI_API_KEY="<KEY>"
#print("Using Key:"+api_key)

client = genai.Client(api_key=api_key)

# Gemini generates code and the execute it

from pprint import pprint

config = types.GenerateContentConfig(
    tools=[types.Tool(code_execution=types.ToolCodeExecution())],
)

code_exec_prompt = """
Generate the first 14 odd prime numbers, then calculate their sum.
generate a .py file I can execute
"""

response = client.models.generate_content(
    model='gemini-2.0-flash',
    config=config,
    contents=code_exec_prompt)

for part in response.candidates[0].content.parts:
  pprint(part.to_json_dict())
  print("-----")


