import {useState} from "react";

export default function MainPage() {
    const [theme, setTheme] = useState<boolean>(false);
    const [todos,setTodos] = useState<string[]>([]);
    const [newTodo, setNewTodo] = useState<string>("");    
    return <div className={`mainPage ${(theme) ? 'dark' : ('')}`} >
        <h1> TODO list App with Typescript </h1>
        <button className="toggle-theme" onClick={() =>{setTheme(!theme)}}> {(theme)?"Dark":"Light"}</button>
        <form>
            <input className={`formOptions ${(theme) ? 'dark' : ('')}`}  type="text" value={newTodo} onChange={(e) => {
                setNewTodo(e.target.value);
            }}/><br/>
            <button className={`formOptions ${(theme)?'dark':('')}`} onClick={(e)=> {
                e.preventDefault();
                if (newTodo === "") return;
                setTodos([...todos,newTodo]);
                setNewTodo("");
            }}> Add TODO </button>
        </form>
        <div> 
            {
                (!todos.length)?("Enter new Todo and then click on Add button to add a todo..."):(
                    todos.map(todo => (
                        <li>{todo}</li>
                    ))
                )}
        </div>
    </div>
}