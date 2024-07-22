from flask import Flask
from flask_mongoengine import MongoEngine

#set db
db = MongoEngine()


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile("settings.py")

    # apply override for tests
    app.config.update(config_overrides)

    # initialize db
    db.init_app(app)

    # import app
    import app

    # register blueprints
    app.register_blueprint(app)

    return app
