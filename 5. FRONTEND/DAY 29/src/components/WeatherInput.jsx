import {useSelector,useDispatch} from "react-redux";
import { UpdatePlace,UpdatePlaceData } from "../actions";
const WeatherInput = () => {
    const theme = useSelector(state => state.theme);

    const place = useSelector(state => state.place);
    const dispatch = useDispatch();
    return(<>
        <form>
            <input type="text" placeholder="e.g. Delhi" className={`${theme ? ("") : "dark"}`} value={place} onChange={e => dispatch(UpdatePlace(e.target.value))}/>
            <button className={`${theme ? ("") : "dark"}`} type="submit" onClick={ e => {
                e.preventDefault();
                dispatch(UpdatePlaceData(place))
            }
            }>GET WEATHER</button>
        </form>
    </>)
}
export default WeatherInput;