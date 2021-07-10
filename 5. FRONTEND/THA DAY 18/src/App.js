import './App.css';
import './Card.js';
import Card from './Card.js';

let array = [...Array(72).keys()];

function App() {
    return ( < div className = "App" >
    
        {array.map(e => {
            if(e%2)
            return(<Card color="white"/>)
            else return(<Card color="black"/>)
        })}
        
     
            </div>)
}
export default App;