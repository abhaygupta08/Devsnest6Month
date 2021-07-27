import './App.css';
import React, {useState, useEffect} from "react";
import LoginPage from "./components/login.js";
import Posts from "./components/Posts.js";
function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    return (
        <div className="App">
		<header>
            <h1>DAY 21 - THA</h1>
        </header>
        {(!isLoggedIn)?(
        <main id="loginPage">
                    <LoginPage setIsLoggedIn={setIsLoggedIn}/>
        </main>):(
            <main id="LoggedIn">
                <div>You are logged in.</div>
                        <Posts setIsLoggedIn={setIsLoggedIn}/>
            </main>
        )}
        </div>
        
    )
}
export default App;