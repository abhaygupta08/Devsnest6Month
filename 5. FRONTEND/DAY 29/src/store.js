import rootReducers from "./reducers";
import { createStore, applyMiddleware} from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from 'redux-devtools-extension';


const store = createStore(rootReducers,
    composeWithDevTools(
    applyMiddleware(thunk),
));

export default store;