import {useState, useEffect} from "react";
import Post from "./Post.js";
const Posts = ({setIsLoggedIn})=> {
    const [posts,setPosts] = useState([]);
    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/posts')
        .then(res => res.json())
        .then(res => setPosts(res))
    
    }, [])
    return(<>
        <button onClick={() => setIsLoggedIn(false)}>Logout</button>
    {posts.map((post,index) => {
        return(
            <Post key="{index}" title={post.title} body={post.body}/>
        )
    })}
    </>)
}
export default Posts;