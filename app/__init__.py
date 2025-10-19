from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        # ❌ 故意的錯誤：201 狀態碼 + 錯字鍵名
        return {"sttaus": "ok"}, 201

    @app.route('/users')
    def users():
        return {"users": [
            {"id": 1, "name": "Ada"},
            {"id": 2, "name": "Linus"}
        ]}, 200

    return app