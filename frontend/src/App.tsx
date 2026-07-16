	import { useState } from 'react'
	import './App.css'

	function App() {
		const [roll, setRoll] = useState(null)
		const [rollMod, setRollMod] = useState(null)
		const [totalRoll, setTotalRoll] = useState(null) 
		let setMod = 0;

		const fetchRoll = async () => {
			try {
				const response = await fetch(`http://127.0.0.1:8000/dice/roll/20?modifier=${setMod}`);
				const data = await response.json();
				setRoll(data.results[0]);
				setRollMod(data.modifier);
				setTotalRoll(data.total);
		} catch (error) {
			console.error('error fetching data:', error)
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
		<section id="center">
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
			{roll !== null && <h2 className='rolledOutput'>Rolled: <span className='outputFancy'>{roll}</span></h2>}
			{roll !== null && <h2 className='rolledOutput'>Modifier: <span className='outputFancy'>{rollMod}</span></h2>}
			{roll !== null && <h2 className='rolledOutput'>Total: <span className='outputFancy'>{totalRoll}</span></h2>}
		</section>
	</>
	)
	}

	export default App
