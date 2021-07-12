function Card({ food, calorie }) {
	return (
		<>
			<div className="foodCalorie">
				<div>
					<h2>{food}</h2>
					<button
						onClick={(e) => {
							e.target.parentNode.parentNode.remove();
						}}>
						Delete
					</button>
				</div>
				<p>You have consumed {calorie} cals today</p>
			</div>
		</>
	);
}

export default Card;
