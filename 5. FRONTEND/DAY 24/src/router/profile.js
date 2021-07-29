import context from "../context/AuthContext";
import { useContext } from "react";
import { Route,Redirect} from "react-router-dom";

export default function Profile() {
    const logger = useContext(context);
    return (
        <>
        <Route>
            {logger.LoggedIn?
            (
            <div id="profile" align="center">
                <h1>PROFILE</h1>
                <div>Protected Page</div>
            </div>
                    )
            :
            (
                <Redirect to="/">
                </Redirect>
            )

            
            }
        </Route>
        </>
    )
}