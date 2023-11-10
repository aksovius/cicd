from fastapi import FastAPI, Request, Header, HTTPException, BackgroundTasks
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC
import json
from urllib.parse import parse_qs, unquote_plus
import subprocess
import os

app = FastAPI()

git_executable = "C:/Program Files/Git/cmd/git.exe"

env = os.environ.copy() # env variables 
def run_shell_commands(commands: list, work_dir: str):
    result = subprocess.run(" && ".join(commands), shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

async def execute_deployment_commands():
    work_dir = "project path"
    commands = [
        f'"{git_executable}" stash',
        f'"{git_executable}" pull',
        f'"{git_executable}" stash pop',
        "docker-compose up --build -d"
    ]
    result = run_shell_commands(commands, work_dir)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)

@app.post("/webhook")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    payload = await request.json()
    ref = payload.get("ref", "")
    # Check if the push is to the "demo" branch
    if "refs/heads/cornerstone3d" in ref:
        background_tasks.add_task(execute_deployment_commands)
        return {"message": "Deployment started"}
    else:
        return {"message": "Push to non-demo branch received"}
