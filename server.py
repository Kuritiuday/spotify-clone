from waitress import serve
from app import app  # Import the 'app' object from your 'app.py'

if __name__ == "__main__":
    # Run the app using Waitress on localhost with port 5000
    serve(app, host='127.0.0.1', port=5000)
