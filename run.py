# run.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sets this
    app.run(debug=False, host='0.0.0.0', port=port)


