from flask import Flask
from .routes.contacts import contacts_bp

app=Flask(__name__)

app.register_blueprint(contacts_bp)