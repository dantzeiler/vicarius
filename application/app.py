from flask import Flask
from routes import setup_routes

app = Flask(__name__)

# Set up the routes
setup_routes(app)

