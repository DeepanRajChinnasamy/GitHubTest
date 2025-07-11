import requests
import base64
import os

GITHUB_API = "https://github.com/DeepanRajChinnasamy/GitHubTest/blob/main/Institutional.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # Store your token in env
JSON_LOCAL_PATH = "test/Institutional.json"

def download_latest_json():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    res = requests.get(GITHUB_API, headers=headers)
    res.raise_for_status()
    content = base64.b64decode(res.json()["content"])
    with open(JSON_LOCAL_PATH, "wb") as f:
        f.write(content)
    print("Downloaded latest Institutional.json")

def run_robot():
    os.system("robot test/graphql_test.robot")

if __name__ == "__main__":
    download_latest_json()
    run_robot()
