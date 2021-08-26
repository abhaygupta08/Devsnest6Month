import { User } from "../actions/index";

const initialUser = {
  userName: "",
  profilePicture: "",
};

export interface actionType {
  type: "UPDATE_USER";
  payload: User;
}

const userReducer = (state: User = initialUser, action: any) => {
  switch (action.type) {
    case "UPDATE_USER":
      return action.payload;
    default:
      return state;
  }
};

export default userReducer;
