from fastapi import FastAPI
from pydantic import BaseModel
import json

# 1.	cd frontend
# 2.	npm run dev
# 3.	cd ../backend
# 4.	.venv/Scripts/activate
# 5.	uvicorn app.main:app --reload


app = FastAPI(title="Adventurers Nexus API", version="1.0.0")



@app.get("/")
def get_status():
	return "Welcome to the Adventurers Nexus API!"

@app.get("/characters/load/{character_id}")
def load_character(character_id: int):
	with open(f"database/{character_id}.json", "r") as f:
		characters_data = json.load(f)

	if character_id not in characters_data or character_id is None:
		return {"error": "Character not found."}

	return characters_data


