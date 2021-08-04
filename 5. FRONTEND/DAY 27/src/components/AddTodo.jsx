import { useState} from "react";
import {AddTodozz} from "../actions";
import {useDispatch} from "react-redux";

export default function AddTodo() {
    const dispatch = useDispatch();
    const [toAdd,setToAdd] = useState("");
return(<>
        <input type="text" value={toAdd} onChange={(e) => {setToAdd(e.target.value);}}/> 
        <button onClick={() => {dispatch(AddTodozz(toAdd))}}>Add Todo</button>
    </>)
}