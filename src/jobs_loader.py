from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

def load_jobs():
    with open(BASE_DIR / "jobs.json", encoding="utf-8") as file:
        return json.load(file)