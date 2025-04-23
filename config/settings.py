import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
host = os.getenv("host")
password = os.getenv("password")
db_name = os.getenv("bd_name")
user = os.getenv("user")