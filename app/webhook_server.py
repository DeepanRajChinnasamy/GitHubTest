# app/webhook_server.py

from flask import Flask, request, jsonify
from robot import run
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running", 200

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON payload"}), 400

    # Optionally inspect the payload here
    print("Received push:", data.get("head_commit", {}).get("message", "No message"))

    try:
        # Ensure log dir exists
        os.makedirs("logs", exist_ok=True)

        # Run Robot Framework test
        result = run("app/call_api_on_yaml_change.robot", log='logs/log.html', report='logs/report.html', output='logs/output.xml')

        return jsonify({"status": "Test run complete", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
