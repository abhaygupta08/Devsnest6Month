import {useState,useContext} from "react";
import context from "../context/AuthContext";

export default function HomePage(){
    
    const logger = useContext(context);
    
    return(
        <div id="home" align="center"> 
            <h1>HOME</h1>
            {
            logger.LoggedIn?
            (<div>You are Logged In...</div>)
            :
            (<div>Login to access Profile/Dashboard</div>)
            }
        {
            logger.LoggedIn?
                    (<button onClick={() => { logger.toogleLogin()}}>Log Out</button>)
        :
                    (<button onClick={() => { logger.toogleLogin() }}>Login</button>)
        }
        </div>
    )
}