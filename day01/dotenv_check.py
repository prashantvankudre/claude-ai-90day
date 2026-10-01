import os
from dotenv import load_dotenv # type: ignore

# Load variables from the .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key:
    print("✅ Success! API Key securely loaded.")
    # Proceed with your API client initialization here
else:
    print("❌ Error: API Key not found. Check your .env file.")
