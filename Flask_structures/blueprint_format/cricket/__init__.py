from flask import Flask
from cricket.batsman import batsman
from cricket.bowler import bowler
from cricket.main import main


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(batsman)
    app.register_blueprint(bowler)

    return app

