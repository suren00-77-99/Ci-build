from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Python Frontend</title>
        </head>
        <body>
            <h1>Python Frontend Application</h1>
            <p>Frontend is running successfully.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return "Frontend Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)