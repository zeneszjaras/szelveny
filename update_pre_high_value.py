# update_pre_high_value.py
import os, json
from github import Github

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME    = "zeneszjaras/szelveny"
FILE_PATH    = "pre_high_value.json"
COMMIT_MSG   = "Automatikus frissítés: új bejegyzés"

if not GITHUB_TOKEN:
    raise RuntimeError("Állítsd be a GITHUB_TOKEN környezeti változót!")

gh   = Github(GITHUB_TOKEN)
repo = gh.get_repo(REPO_NAME)

contents = repo.get_contents(FILE_PATH, ref="main")
lines    = [l for l in contents.decoded_content.decode().splitlines() if l.strip()]

new_entry = {
    "szelvenyszam": "X" + os.urandom(3).hex().upper(),
    "alaptet": 50,
    "odds": 2.25
}
lines.append(json.dumps(new_entry))

new_content = "\n".join(lines) + "\n"
repo.update_file(FILE_PATH, COMMIT_MSG, new_content, contents.sha, branch="main")
print("pre_high_value.json frissítve és push-olva.")
