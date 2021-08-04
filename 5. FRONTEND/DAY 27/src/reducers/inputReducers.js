const InputReducers = (state = ["a","b"],action) => {
    if(action.type==="ADD_TODO"){
        console.log(state);
        return [ ...state,action.payload ];
    }
    else if(action.type==="DELETE_TODO"){
        // console.log(action);
        // console.log("email chng");
        return state.filter((item,index) => index != action.payload );
        
        // console.log(state,action);
    }
    return state;
};

export default InputReducers;