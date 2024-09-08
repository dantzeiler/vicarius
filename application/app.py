from flask import Flask
from routes import setup_routes
from kubernetes import client, config

app = Flask(__name__)

config.load_incluster_config() 

# Set up the routes
setup_routes(app)

