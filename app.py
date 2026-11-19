
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hi Sanjib</h1>
    <h2>Welcome to DevOps!</h2>
    <p>This is my first cloud-ready application.</p>
    <p>Application Status: Running</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "application": "DevOps Cloud Demo",
        "status": "Healthy"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
