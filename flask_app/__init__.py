from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

print("INCIANDO __INIT__")
print(access_token_secret)
app = Flask(__name__)

app.secret_key = ""