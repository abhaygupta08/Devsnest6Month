import { changeName, changeEmail} from "../actions";
import { useSelector, useDispatch} from "react-redux";
import AllTodos from "./AllTodos";
import AddTodo from "./AddTodo";
const Display = () => {
    const formData = useSelector(state => state.input);
    const dispatch = useDispatch();
    return (<>
    <h1>TODO MANAGER</h1>
    <p>Redux based State management</p>
        <br></br>
        <br></br>
    <AddTodo />
    <br/>
    <AllTodos />

    </>)
}

export default Display;