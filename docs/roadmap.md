Adventurer's Nexus ROADMAP

---------------------------------------------------
PHASE 0 - Foundation

	Project Management
		[X] Private Github Repository Created
		[X] README Started
		[X] Development Guidelines Written
		[X] Roadmap Documented

	Development Enviroment
		[X] React + TypeScript + Vite installed
		[X] Python Backend Enviroment Created
		[X] VSCode Workspace Configured




---------------------------------------------------
PHASE 1 - Skeletal Backend

	Structure
		backend/
		|
		|- app/
		|	|- main.py
		|	|- api/
		|	|- core/
		|	|- database/
		|	|	|- migrations/
		|	|- models/
		|	|- schemas/
		|	|- services/
		|
		|
		|- tests/

	Build
		API Checks



---------------------------------------------------
PHASE 2 - D&D Rules Engine Structure  (CURRENT)

	Python (not yet web)
		backend/
		|
		|- core
			|- dice.py			{Completed Dice Rolling}
			|- abilities.py		{NOT STARTED}
			|- modifiers.py		{NOT STARTED}
			|- skills.py		{HAS BEGUN: List of all Skills}
			|- combat.py		{HAS BEGUN: List of all armors & weapons, without ac/dmg}

	Implement
		Dice
			d4, d6, d8, d10, d12, d20, d100
			modifiers
			advantage
			disadvantage
			critical results (fail / success)



---------------------------------------------------
PHASE 3 - Character System (THE FIRST BIG ONE)

	models/character.py
		Add:
			Name
			Race
			Class
			Level
			Ability Scores
			HP
			Inventory
			Spells

	frontend/src/
		components/
			characterCard.tsx
			abilityScore.tsx
			characterSheet.tsx

		pages/
			characterCreator.tsx

	Needs to be able to:
		create & save new
		load & view existing



---------------------------------------------------
PHASE 4 - Database Integration

	Add:
		PostgreSQL
		SQLAlchemy
		Alembic

	Database:
		Users
		Characters
		Campaigns
		Items
		Spells
		Monsters


---------------------------------------------------
PHASE 5 - User Accounts
	Allow multiple users
	Implement:
		Registration
		Login
		Permissions
	
	Structure:
		User
			Characters
			Campaigns
			Groups


---------------------------------------------------
PHASE 6 - DM Campaign Manager

	Campaign
		Players
		Sessions
		Notes
		Locations
		NPCs
	
	NPC Manager
		Name
		Description
		Location
		Relationships
		Notes

	Quest System
		EXAMPLE:
			Quest Name: "The Test One"
			Status: ACTIVE
			Objectives:
				[X] Find the map
				[ ]	Defeat 3 goblins
				[ ] Return treasure


---------------------------------------------------
PHASE 7 - Monster & Encounter System

	Add:
		Monster
			Stats
			Actions
			Abilities
			CR (if applicable)

	Encounter Builder
		Party:
			Number of players
			Level of players

		OUTPUT
			Difficulty: Hard
			Enemies:
				3x Hobgoblins
				1x Captain



---------------------------------------------------
PHASE 8 - Combat Tracker

	Initiative Tracking
	Additional Tracking:
		HP
		Conditions
		Concentration
		Spell Slots
		AOE Effects



---------------------------------------------------
PHASE 9 - Virtual Tabletop (A MASSIVE ONE)

	Maps
	Tokens
	Movement
	Fog of War
	Real-time Updates

	Frontend
		React
		Additional

	Backend
		WebSockets


---------------------------------------------------
PHASE 10 - Discord Bot Integration (Surprisingly Easy)

	Command Prefix: #
	Commands:
		#roll
		#character sheet
		#initiative
		#attack

	Basically another frontend
	
