from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Flask Page</title>
    </head>
    <body style='font-family: Arial; text-align: center; padding: 40px;'>
        <h1>Hello from Flask!</h1>
        <p>This is a simple webpage served from a Python Flask server.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
