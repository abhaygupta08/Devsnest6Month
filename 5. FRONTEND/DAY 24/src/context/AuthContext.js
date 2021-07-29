import React,{useState,createContext} from "react";
const context = React.createContext();

export default context;

export function AuthContext({children}){
    const [LoggedIn, setLoggedIn] = useState(false);
    const [Loading, setLoading] = useState(false);

    const logger= {
        LoggedIn:LoggedIn,
        Loading: Loading,
        toogleLogin: () => {
            setLoggedIn(!LoggedIn);
        }
    }
    return(
        <context.Provider value={logger}>
        {children}
        </context.Provider>
    )
};