import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".gitignore/.env")

api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG_MODE")

print(api_key)
print(debug_mode)