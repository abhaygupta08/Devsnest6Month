import {useSelector,useDispatch} from "react-redux";
import { DeleteTodozz} from "../actions";
export default function AllTodos(){
    const dispatch = useDispatch();
    const Todos = useSelector(state => state.input);
    console.log(Todos);
    return (<>
        {
        Todos.map((element,i) => {
            return <div key={i}>{element}<button data-key={i} onClick={(e) => {
                // console.log(e.target.dataset.key)
                dispatch(DeleteTodozz(e.target.dataset.key))}
            }>Delete</button></div>
        })
        }
   </>)
}