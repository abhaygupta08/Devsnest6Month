const changeName = (txt) => {
    return {
        type: "CHANGE_NAME",
        payload : txt
    }
}
const changeEmail = (...args) => {
    console.log(args);
    return {
        type: "CHANGE_EMAIL",
        payload: args[0],
    }
}

export {changeName, changeEmail};