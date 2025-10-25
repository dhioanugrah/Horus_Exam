from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate, jwt, cors
from .routes import users as users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

    # Blueprints
    app.register_blueprint(users_bp.bp, url_prefix="/users")

    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    return app
