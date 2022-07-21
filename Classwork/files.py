import json
import pathlib

file_path = pathlib.Path("./json/twitter_users.json").resolve()
file_path.parent.mkdir(parents=True, exist_ok=True)
twitter_users = [{'name': 'Abang Dorcas', 'is married': True, 'age': 45},
                 {'name': 'John Doe', 'is married': False, 'age': 15}]
with file_path.open(mode="w", encoding="utf-8") as file:
    json.dump(twitter_users, file, indent=4)