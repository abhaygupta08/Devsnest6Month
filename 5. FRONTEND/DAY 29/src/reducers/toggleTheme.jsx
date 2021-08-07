const ToggleTheme = (state=true,action) => {
    if (action.type === "TOGGLE_THEME"){
        // console.log(action.payload);
        return !state;
    }
    return state;
}

export default ToggleTheme;