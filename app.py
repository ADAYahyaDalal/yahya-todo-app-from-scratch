from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Flask TODO App — Step 1</h1>"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
