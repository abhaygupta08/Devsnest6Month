export interface User {
  userName: string;
  profilePicture: string;
}

const updateUser = () => {
  return (dispatch: any) => {
    fetch(process.env.PUBLIC_URL + "/data/user.json")
      .then((res) => res.json())
      .then((data) => {
        dispatch({
          type: "UPDATE_USER",
          payload: data,
        });
      });
  };
};

export { updateUser };
