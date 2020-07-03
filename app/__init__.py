from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

#Previously we had here - from app import views
import views
