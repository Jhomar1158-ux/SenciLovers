from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

FLASK_APP_SECRET_KEY = os.getenv('FLASK_APP_SECRET_KEY')

print("INCIANDO __INIT__")
app = Flask(__name__)

app.secret_key = FLASK_APP_SECRET_KEY