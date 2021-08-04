const AddTodozz = todo => {
    return {
        type: "ADD_TODO",
        payload : todo
    }
}
const DeleteTodozz = index => {
    return {
        type : "DELETE_TODO",
        payload : index,
    }
}
export {AddTodozz, DeleteTodozz};