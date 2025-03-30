from google import genai
import os

# Replace with your actual Gemini API key or get it from an environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    api_key = "YOUR_GEMINI_API_KEY" #Or assign directly, but not recommended for security
    print("Warning: GEMINI_API_KEY environment variable not set.  Using direct assignment (not recommended).")

# API key has been exported as a environment variable:
# export GEMINI_API_KEY="<KEY>"
#print("Using Key:"+api_key)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="How large is the universe?",
)

print(response.text)
