import requests
import json
import os

# Replace with your actual Gemini API key or get it from an environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    api_key = "YOUR_GEMINI_API_KEY" #Or assign directly, but not recommended for security
    print("Warning: GEMINI_API_KEY environment variable not set.  Using direct assignment (not recommended).")

'''
the key can be exported using:
    MAC: export GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"
    Windows: set GEMINI_API_KEY=YOUR_ACTUAL_API_KEY
'''

# Check that the api_key is set
if api_key == "YOUR_GEMINI_API_KEY" or not api_key:
  raise ValueError("Please set your GEMINI_API_KEY environment variable or replace 'YOUR_GEMINI_API_KEY' with your actual API key.")


url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

headers = {'Content-Type': 'application/json'}

data = {
  "contents": [{
    "parts":[{"text": "Explain how AI works"}]
    }]
   }

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    json_response = response.json()
    #print(json.dumps(json_response, indent=2)) # Pretty-print the JSON response


    # Extract and print the 'text' content
    if 'candidates' in json_response and len(json_response['candidates']) > 0:
        if 'content' in json_response['candidates'][0] and 'parts' in json_response['candidates'][0]['content']:
            parts = json_response['candidates'][0]['content']['parts']
            if len(parts) > 0 and 'text' in parts[0]:
                text = parts[0]['text']

                # Pretty-print the text by splitting on newlines
                for line in text.splitlines():
                    print(line)


except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON response: {e}")
    print(f"Raw response text: {response.text}") # Print the raw response for debugging
except Exception as e:
    print(f"An unexpected error occurred: {e}")
