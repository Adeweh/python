import json
from pathlib import Path

db = Path.cwd() / "db.json" #or Path(__file)
db.touch()

def read_db():
    with db.open(mode="r", encoding="utf-8") as file:
        return json.load(file)