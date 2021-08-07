import React from "react";
import "./App.css";
import Display from "./components/Display";
import { useSelector } from "react-redux";

export default function App() {
    const theme = useSelector(state => state.theme);
    return (
        <div className={`App ${theme?(""):"dark"}`} >
            <Display/>
       </div>
    );
}