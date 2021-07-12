function Counter({value}){
        if(!value){
            value = 0;
        }
    return(<>

        <button onClick= {(e) => {
            e.target.innerText = Number(e.target.innerText) + 1;
        }}>{value}</button>

    </>)
}
export default Counter;