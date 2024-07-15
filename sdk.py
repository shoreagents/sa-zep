import os
from zep_python import ZepClient
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('ZEP_API_KEY')

# Replace with Zep API URL and (optionally) API key
zep = ZepClient("https://app.getzep.com", api_key=API_KEY)
