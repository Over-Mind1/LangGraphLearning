import os
from dotenv import load_dotenv

#==========setup .env ===========
load_dotenv()

#==============GEMINI_API_KEY===================
if os.getenv("GEMINI_API_KEY") is None:
    raise ValueError("GEMINI_API_KEY environment variable not set. Please set it in your .env file.")
else:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    print("GEMINI_API_KEY environment variable is set.")
