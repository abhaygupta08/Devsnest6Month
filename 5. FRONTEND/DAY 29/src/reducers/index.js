import placeReducer from "./placeReducer";
import placeDataReducer from "./placeDataReducer";
import { combineReducers } from "redux";
import toggleTheme from "./toggleTheme";
const rootReducers = combineReducers({
    place : placeReducer,
    placeData : placeDataReducer,
    theme : toggleTheme,
});

export default rootReducers;