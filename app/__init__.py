from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return {"status": "ok"}, 200

    @app.route('/users')
    def users():
        return {"users": [
            {"id": 1, "name": "Ada"},
            {"id": 2, "name": "Linus"}
        ]}, 200

    return app