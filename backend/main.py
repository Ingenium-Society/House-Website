from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a route for the API and data sent to the frontend
@app.get("/api/hello")
def hello():
    return jsonify({
        "message": "P mabar"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
