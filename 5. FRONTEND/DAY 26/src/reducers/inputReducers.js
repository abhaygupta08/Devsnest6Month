const InputReducers = (state = {name : "", email : ""},action) => {
    if(action.type==="CHANGE_NAME"){
        // console.log("name chng");
        state = { ...state, name: action.payload };
    }
    else if(action.type==="CHANGE_EMAIL"){
        // console.log(action);
        // console.log("email chng");
        state = { ...state, email: action.payload };
        
        // console.log(state,action);
    }
    return state;
};

export default InputReducers;