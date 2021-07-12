import './App.css';
import "./counter";
import Counter from './counter';

function App() {
    return (< div className="App" >

        <div> There are 4 counter component instances that each manage their own state.</div>
        {/* <br/> */}
        <div>
            <Counter />
            <Counter />
            <Counter />
            <Counter />
        </div>


    </div>)
}
export default App;