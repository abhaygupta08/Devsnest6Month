import logo from './logo.svg';
import './App.css';
import Box from "./box";

function App() {
  return (<>

      <div id="chess">
        {Array.apply(null, Array(121)).map((i)=>
      <Box />
      )}
        
      </div>

  </>  
  );
}

export default App;
