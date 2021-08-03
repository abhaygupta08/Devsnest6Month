import InputReducers from "./inputReducers";
import { combineReducers } from "redux";

const rootReducers = combineReducers({
    input : InputReducers,
});

export default rootReducers;