from flask import Flask

app = Flask(__name__)

app.config.from_object("settings.ProductionConfig")

@app.route("/")
@app.route("/hi")
def hello():
    return "Hello"
