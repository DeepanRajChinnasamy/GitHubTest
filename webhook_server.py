from flask import Flask, request, jsonify
import subprocess
import hmac
import hashlib
import os

app = Flask(__name__)

# Optional: GitHub secret for signature validation
GITHUB_SECRET = os.environ.get("GITHUB_SECRET", "").encode()

def verify_signature(payload, signature):
    if not GITHUB_SECRET or not signature:
        return True
    sha_name, sig = signature.split('=')
    mac = hmac.new(GITHUB_SECRET, msg=payload, digestmod=hashlib.sha1)
    return hmac.compare_digest(mac.hexdigest(), sig)

@app.route('/', methods=['POST'])
def github_webhook():
    signature = request.headers.get('X-Hub-Signature')
    if not verify_signature(request.data, signature):
        return "Signature mismatch", 403

    data = request.get_json()
    modified_files = []

    if data and 'commits' in data:
        for commit in data['commits']:
            modified_files.extend(commit.get('modified', []))

    # Trigger only if your JSON file was updated
    if 'Society.json' in modified_files:
        print("Detected change in Society.json. Running Robot test...")
        subprocess.Popen(["python3", "run_robot_test.py"])
        return jsonify({"status": "triggered"}), 200

    return jsonify({"status": "ignored"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
