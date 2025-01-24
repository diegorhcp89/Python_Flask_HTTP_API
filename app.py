from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_word():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)