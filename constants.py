from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = '0.0.0.0'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = os.getenv("PORT")