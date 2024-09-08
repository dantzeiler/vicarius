from flask import Flask
from routes import setup_routes
from kubernetes import  config

app = Flask(__name__)

config.load_incluster_config() 

# Set up the relevant routes
setup_routes(app)

