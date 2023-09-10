from typing import Union
from datetime import date
from fastapi import FastAPI
from datetime import datetime
from datetime import datetime, timezone, timedelta

app = FastAPI()

@app.get("/{slack_name}/{track}")
def hng_get_request(slack_name:str,track:str):
    return {
        "slack_name":slack_name,
        "current_day":datetime.now().strftime("%A"),
        "utc_time":datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track":track,
        "github_file_url":"https://github.com/Tim1119/HNG-2023/blob/main/project_1/main.py",
        "github_repo_url":"https://github.com/Tim1119/HNG-2023"
    }

