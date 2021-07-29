import context from "../context/AuthContext";
import {useContext} from "react";

export default function About() {
    const logger = useContext(context);
    return (

        <div id="about" align="center">
            <h1>ABOUT</h1>
            <div>Public Page</div>
        </div>
    )
}