import {useState} from "react";
const LoginPage = ({setIsLoggedIn}) => {

    const [formData, setFormData] = useState({
        "username" : "",
        "password" : ""
    });
    const handleFormDataChange = e => {
        setFormData(formData => ({...formData,[e.target.name]:e.target.value}));
    }
    const [error,setError] = useState("");
    const HandleSubmit =  e => {
        e.preventDefault();
        //empty validation
        if (formData.username === "") {setError("username cannot be empty"); return;}
        if (formData.password === "") {setError("password cannot be empty"); return;}

        //password length
        if(formData.password.length < 6) {setError("Min 6 len password"); return;}

        setIsLoggedIn(true);
    }
    return(<>
    <h2>LoginPage</h2>
    <form onSubmit={HandleSubmit}>
            <label>Username : <input type="text" placeholder="username here" name="username" value={formData.username} onChange={handleFormDataChange}/></label>
            <label>Password : <input type="password" placeholder="password here" name="password" value={formData.password} onChange={handleFormDataChange}/></label>
        <input type="submit" value="Login"/>
        <p id="error" style={{color:"red"}}>{error}</p>
    </form>
    
    </>)
}

export default LoginPage;