from fastapi import FastAPI
from pydantic import BaseModel
from app.core import roll_dice, adv_or_dis
import json

# 1.	cd AdventurersNexus/frontend
# 2.	npm run dev
# 3.	cd ../backend
# 4.	.venv/Scripts/activate
# 5.	uvicorn app.main:app --reload

rolledDice = []


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




@app.get('/dice/roll/{die_number}')
def roll(die_number: int, amount: int, modifier: int | None=0):
	return roll_dice(die_number, amount, modifier)





@app.get('/dice/advantage')
def advantage(modifier: int | None=0):
	return adv_or_dis(modifier, False)





@app.get('/dice/disadvantage')
def disadvantage(modifier: int | None=0):
	return adv_or_dis(modifier, True)






