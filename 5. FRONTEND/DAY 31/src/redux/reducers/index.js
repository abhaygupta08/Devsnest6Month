import {combineReducers} from "redux";
import { productReducer, selectedProductReducer } from "./productReducer";

const rootReducer = combineReducers({
    allProducts: productReducer,
    selectedProduct: selectedProductReducer,
});

export default rootReducer;