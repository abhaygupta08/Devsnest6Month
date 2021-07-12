import './App.css';
import Card from "./components/card.jsx";
function App() {
  return (
    <div className="App">
      <h1>Calorie Read Only</h1>
      <div className="container">
        <Card food="Pizza" calorie="56" />
        <Card food="Burger" calorie="69" />
        <Card food="Coke" calorie="500" />
        <Card food="Browne" calorie="180" />
        <Card food="Fried Rice
" calorie="90" />
        <Card food="Pani Puri
" calorie="16" />
      </div>
    </div>
  );
}

export default App;
