import WeatherInput from "./WeatherInput";
import WeatherInfo from "./WeatherInfo";
import { useSelector, useDispatch} from "react-redux";
import {ToggleTheme} from "../actions";

const Display = () => {
    const theme = useSelector(state => state.theme);
    const dispatch = useDispatch();
    return (<>
    <h1>WEATHER APP</h1>
    <p>Async Redux - using Fetch </p>
        <br />
        <br />
        <button id="toggleTheme" className={`${theme ? ("") : "dark"}`} onClick={() => dispatch(ToggleTheme())}>Dark</button>
        <WeatherInput/>
        <WeatherInfo/>
    </>)
}

export default Display;