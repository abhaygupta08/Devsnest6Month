import context from "../context/AuthContext";
import {useContext } from "react";
import {Route,Redirect} from "react-router-dom";
export default function Dashboard() {
    const logger = useContext(context);
    return (
        <>
        
            <Route>
                {logger.LoggedIn?
                    (<div id="dashboard" align="center">
                        <h1>DASHBOARD</h1>
                        <div>Protected Page</div>
                    </div>
    ):
    <Redirect to="/"/>
    }
            </Route>
        </>
        )
}
