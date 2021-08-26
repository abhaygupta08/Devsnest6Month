import React, { useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap";

import { Provider } from "react-redux";
import store from "./store";

import { updateUser } from "./actions/index";
import { useDispatch } from "react-redux";

import Navbar from "./components/Navbar";
import Landing from "./components/Landing";

import "./day35.css";

export interface PostType {
  username: string;
  post: string;
  profilePicture: string;
}

const Day35Comp = () => {
  const [posts, setPosts] = React.useState<PostType[]>([]);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(updateUser());
    fetch(process.env.PUBLIC_URL + "/data/post.json")
      .then((res) => res.json())
      .then((data) => setPosts(data));
    //eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <Provider store={store}>
      <div className="day35">
        <Navbar />
        <Landing posts={posts} />
      </div>
    </Provider>
  );
};

export default Day35Comp;
