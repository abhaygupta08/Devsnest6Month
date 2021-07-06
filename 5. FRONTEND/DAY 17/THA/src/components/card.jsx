function Card({food,calorie}) {
    return (<>
        <div className="foodCalorie">
            <h2>{food}</h2>
            <p>You have consumed {calorie} cals today</p>
        </div>
    </>)
    
}

export default Card;