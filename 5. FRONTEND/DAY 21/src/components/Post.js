import {useState} from "react";
const Post = ({key,title,body}) => {
    const [isEditMode, setIsEditMode] = useState(false);
    const [EditPost,setEditPost] = useState({
        title : title,
        body : body 
    });
    const inputHandleChange = (e) => {
        setEditPost({...EditPost,[e.target.name] : e.target.value});
    }
    return(
    <div className="post" data-key="{key}">
        
        {
        (isEditMode)?(<input type="text" name="title" value={EditPost.title} onChange={(e) => inputHandleChange(e)}/>)
        :(<h3>{EditPost.title}</h3>)
        }

        {
                (isEditMode) ? (<input type="text" name="body" value={EditPost.body} onChange={(e) => inputHandleChange(e)}/>)
        :(<p>{EditPost.body}</p>)
        }
        {
            isEditMode?
            (<button onClick={() => setIsEditMode(false)}>Save</button>):
            (<button onClick={()=> setIsEditMode(true)}>Edit</button>)
        }

        <br/><br/>
    </div>);
}
export default Post;