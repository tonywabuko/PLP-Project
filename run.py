# run.py
from dotenv import load_dotenv
import os

load_dotenv()  # This loads variables from your .env file

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

