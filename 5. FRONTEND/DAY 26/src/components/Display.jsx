import { changeName, changeEmail} from "../actions";
import { useSelector, useDispatch} from "react-redux";

const Display = () => {
    const formData = useSelector(state => state.input);
    // const formEmail = useSelector(state => state.input);
    const dispatch = useDispatch();
    return (<>
    <h1>DAY 26</h1>
    <p>Redux based State management</p>
        <br></br>
        <br></br>
    <form>
        <label>Name : <input type="text" onChange={ 
            (e) => {
                dispatch(changeName(e.target.value));
        }}></input></label>
            <label>Email : <input type="text" onChange={
                (e) => {
                    dispatch(changeEmail(e.target.value))
                }}></input></label>
    </form>
    <div align="left">
            Your Name Here : {formData.name}
            <br/>
            Your Email Here : {formData.email}
    </div>
    </>)
}

export default Display;