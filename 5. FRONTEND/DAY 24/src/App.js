import React, { useContext, createContext, useState } from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
} from "react-router-dom";

import "./App.css";
import HomePage from "./router/home";
import Profile from "./router/profile";
import Dashboard from "./router/dashboard";
import About from "./router/about";

import {AuthContext} from "./context/AuthContext";

export default function App() {
    
    return (
        <div className="App">
            <Router>
                <nav>
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/profile">Profile</Link></li>
                        <li><Link to="/dashboard">Dashboard</Link></li>
                        <li><Link to="/about">About</Link></li>
                    </ul>
                </nav>
                <main>
                    <Switch>
                        <AuthContext>
                        <Route exact path="/" component={HomePage} />
                        <Route exact path="/about" component={About} />
                        <Route exact path="/dashboard" component={Dashboard} />
                        <Route exact path="/profile" component={Profile} />
                        </AuthContext>
                    </Switch>
                </main>
            </Router>
        </div>
    );
}