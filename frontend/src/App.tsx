	import { useState } from 'react'
	import './App.css'

	function App() {
		const [roll, setRoll] = useState(null);
		const [rollMod, setRollMod] = useState(null);
		const [totalRoll, setTotalRoll] = useState(null) ;
		let setMod = 0;

		const fetchRoll = async () => {
			try {
				const response = await fetch(`http://127.0.0.1:8000/dice/roll/20?modifier=${setMod}`);
				const data = await response.json();
				setRoll(data.results[0]);
				setRollMod(data.modifier);
				setTotalRoll(data.total);
		} catch (error) {
			console.error('error fetching data:', error);
		}
	};


	const [cardName, setCard] = useState(null);
	const [cardDescription, setDescription] = useState(null);
	const fetchCard = async () => {
		try {
			const response = await fetch(`http://127.0.0.1:8000/decks/manyThings/1?size=22`);
			const data = await response.json();
			setCard(data.name);
			setDescription(data.description);
		} catch (error) {
			console.error('error fetching data:', error);
		}
	};


	const [illusionCard, setIllusion] = useState(null);
	const fetchIllusion = async () => {
		try {
			const response = await fetch(`http://127.0.0.1:8000/decks/illusions`);
			const data = await response.json();
			setIllusion(data.name)
		} catch (error) {
			console.error('error fecthing data:', error);
		}
	};



	const handleNumberInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		const numericValue = (e.target as HTMLInputElement).valueAsNumber;

		if (isNaN(numericValue)) {
			setMod = 0
		} else {
			setMod = numericValue
		}
	};


	

	return (
	<>
		<section id="tests">
			<br></br>
			<br></br>
			<div className="inputCenter">
				<label htmlFor="numberIn" className='numberInLabel'>Input modifier:</label>
				<input type='number' className='numberIn' onChange={handleNumberInputChange} name='numberIn' min="0"></input>
			</div>
			<br></br>
			<br></br>
			<button type="button" className="roller" onClick={fetchRoll}>Roll D20</button>
			<br></br>
			{roll !== null && <h2 className='fetchedOutput'>Rolled: <span className='outputFancy'>{roll}</span></h2>}
			{roll !== null && <h2 className='fetchedOutput'>Modifier: <span className='outputFancy'>{rollMod}</span></h2>}
			{roll !== null && <h2 className='fetchedOutput'>Total: <span className='outputFancy'>{totalRoll}</span></h2>}
		</section>
		<br></br>
		<br></br>
		<br></br>
		<section id='tests'>
			<button type='button' className='roller' onClick={fetchCard}>Draw Card</button>
			<br></br>
			{cardName !== null && <h2 className='fetchedOutput'>Card: <span className='outputFancy'>
				{cardName}</span></h2>}
			{cardName !== null && <h2 className='fetchedOutput'>Card Description: <span className='outputFancy'>
				{cardDescription}</span></h2>}
		</section>
		<br></br>
		<br></br>
		<br></br>
		<section id='tests'>
			<button type='button' className='roller' onClick={fetchIllusion}>Draw Illusion Card</button>
			<br></br>
			{illusionCard !== null && <h2 className='fetchedOutput'>Card: <span className='outputFancy'>
				{illusionCard}</span></h2>}
		</section>
	</>
	)
	}

	export default App
