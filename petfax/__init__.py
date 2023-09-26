from flask import Flask
from . import pet
from petfax import show_page

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def hello():
        return "Hello, petfax! from __init__"

    app.register_blueprint(pet.bp)
    app.register_blueprint(show_page.show_page_bp)

    return app
