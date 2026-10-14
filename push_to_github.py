"""
Automated GitHub Repository Creator and Pusher for CardioScan AI
Student: Vivek Vardhan | Machine Learning & AI Capstone
"""

import sys
import os
import subprocess
import urllib.request
import json

GIT_DIR = r"C:\Users\VIVEK VARDHAN\AppData\Local\Programs\Git\cmd"
os.environ["PATH"] = GIT_DIR + os.pathsep + os.environ.get("PATH", "")

def create_and_push(token, repo_name="cardioscan-ai-capstone", private=False):
    print(f"Connecting to GitHub API to create repository '{repo_name}'...")
    req_data = json.dumps({
        "name": repo_name,
        "description": "CardioScan AI: End-to-End Clinical Heart Disease Risk Prediction System (ML & AI Week 4 Capstone)",
        "private": private,
        "auto_init": False
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.github.com/user/repos",
        data=req_data,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "CardioScan-AI"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            res_json = json.loads(response.read().decode())
            clone_url = res_json["clone_url"]
            html_url = res_json["html_url"]
            username = res_json["owner"]["login"]
            print(f"[SUCCESS] Repository created on GitHub: {html_url}")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode()
        if e.code == 422 and "already exists" in err_msg:
            # Fetch user info to get username
            u_req = urllib.request.Request(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Accept": "application/vnd.github+json",
                    "User-Agent": "CardioScan-AI"
                }
            )
            with urllib.request.urlopen(u_req) as u_res:
                user_data = json.loads(u_res.read().decode())
                username = user_data["login"]
            clone_url = f"https://github.com/{username}/{repo_name}.git"
            html_url = f"https://github.com/{username}/{repo_name}"
            print(f"[NOTE] Repository '{repo_name}' already exists: {html_url}")
        else:
            print(f"[ERROR] GitHub API returned status {e.code}: {err_msg}")
            return False

    # Configure authenticated remote URL
    auth_url = clone_url.replace("https://", f"https://{username}:{token}@")

    print(f"Setting git remote origin...")
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", auth_url], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)

    print("Pushing all files and models to GitHub main branch...")
    push_res = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
    
    # Remove token from remote origin url for security
    subprocess.run(["git", "remote", "set-url", "origin", clone_url], capture_output=True)

    if push_res.returncode == 0:
        print("\n" + "="*70)
        print(f"SUCCESS! Project is published to your GitHub:")
        print(f"URL: {html_url}")
        print("="*70)
        return True
    else:
        print(f"[ERROR] Git push failed:\n{push_res.stderr}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        token = sys.argv[1].strip()
        repo = sys.argv[2].strip() if len(sys.argv) > 2 else "cardioscan-ai-capstone"
        create_and_push(token, repo)
    else:
        tok = input("Enter your GitHub Personal Access Token (PAT): ").strip()
        repo = input("Enter repository name [default: cardioscan-ai-capstone]: ").strip() or "cardioscan-ai-capstone"
        create_and_push(tok, repo)
