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
response = client.models.generate_content_stream(
    model='gemini-2.0-flash-thinking-exp',
    contents='Who was the youngest author listed on the transformers NLP paper?',
)

buf = io.StringIO()
for chunk in response:
    buf.write(chunk.text)
    # Display the response as it is streamed
    print(chunk.text, end='')


# This is generating an error at the end but anyways

# And then render the finished response as formatted markdown.
#clear_output()
#print(buf.getvalue())
