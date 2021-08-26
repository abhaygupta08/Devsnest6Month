import React, { useState } from "react";

import { PostType } from "../Day35";

const Post = ({ post }: { post: PostType }) => {
  const [isLiked, setIsLiked] = useState<boolean>(false);

  return (
    <div className="card post">
      <div className="card-header">
        <div className="user">
          <img className="user-img" src={post.profilePicture} alt="" />
          <h5 className="mb-0 card-title">{post.username}</h5>
        </div>
        <i className="bi bi-three-dots"></i>
      </div>
      <img src={post.post} className="card-img-top" alt="" />
      <div className="buttons">
        <i
          className={isLiked ? "bi bi-heart-fill liked" : "bi bi-heart "}
          onClick={() => setIsLiked(!isLiked)}
        ></i>
        <i className="bi bi-chat"></i>
        <i className="bi bi-share"></i>
      </div>
    </div>
  );
};

export default Post;
