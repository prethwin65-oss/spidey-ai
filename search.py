from flask import Flask, request, jsonify
from ai import get_ai_response

app = Flask(__name__)

@app.route("/")
def home():
    return "Spidy-AI Backend is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]
    reply = get_ai_response(user_message)

    return jsonify({
        "user": user_message,
        "reply": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)