import json, typing
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.core import roll_dice, adv_or_dis
from app.core.cards import deck_of_many_things
from app.core.cards import deck_of_illusions
from starlette.responses import Response



# 1.	cd AdventurersNexus/frontend
# 2.	npm run dev
# 3.	cd AdventurersNexus/backend
# 4.	.venv/Scripts/activate (or on linux: source .venv/bin/activate)
# 5.	uvicorn app.main:app --reload



class PrettyJSONResponse(Response):
	media_type = "application/json"
	def render(self, content: typing.Any):
		return json.dumps(content, indent=4).encode("utf-8")



app = FastAPI(default_response_class=PrettyJSONResponse, title="Adventurers Nexus API", version="1.0.0")



origins = [
	"http://localhost:5173",
	"http://127.0.0.1:5173"
]



app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)



@app.get("/")
def get_status():
	return "Welcome to the Adventurers Nexus API!"



@app.get("/api/data")
def get_data():
	return "Welcome to API Backend"



@app.get("/characters/load/{character_id}")
def load_character(character_id: int):
	with open(f"database/{character_id}.json", "r") as f:
		characters_data = json.load(f)

	if character_id not in characters_data or character_id is None:
		return {"error": "Character not found."}

	return characters_data



@app.get('/dice/roll/{die_number}')
def roll(die_number: int, amount: int | None=1, modifier: int | None=0):
	return roll_dice(die_number, amount, modifier)



@app.get('/dice/advantage')
def advantage(modifier: int | None=0):
	return adv_or_dis(modifier, False)



@app.get('/dice/disadvantage')
def disadvantage(modifier: int | None=0):
	return adv_or_dis(modifier, True)



@app.get('/decks/manyThings/{amount}')
def draw_domt(amount: int | None=1, size: int | None=13):
	domt = deck_of_many_things.DeckOfManyThings(size)

	if amount is None:
		amount = 1

	
	card = domt.draw()
	if card.returnToDeck:
		domt.add_card(card)
	else:
		pass
	
	return card


@app.get('/decks/illusions')
def draw_doi():
	doi = deck_of_illusions.DeckOfIllusions()

	card = doi.draw()

	return card


