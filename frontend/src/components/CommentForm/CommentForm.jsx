import axios from "axios";
import { useState } from "react";
// import useAuth from "../../hooks/useAuth";

const CommentForm = ({ videoId, user, token, config }) => {

  // const { user, token, config } = useAuth();
  const [comment, setComment] = useState('')
    
  async function addNewComment(newComment) {
    let url = "http://127.0.0.1:8000/api/" + videoId + "/comments/add_comment/";
    let response = await axios.post(url, newComment, config);
    console.log(response)
  }

  function handleNewComment(event) {
    if (token){
      event.preventDefault();
      let newComment = {
          username: user,
          text: comment,
          likes: 0,
          dislikes: 0,
      };
      addNewComment(newComment);
    }
    else{
      alert('Must be signed in to comment.')
    }
  }

  
  return (
        <form onSubmit={handleNewComment}>
          <label>Comment</label>
          <input placeholder="Must be signed in to comment." value={comment} onChange={(event) => setComment(event.target.value)}/>
          <button type='submit'>Post</button>
        </form>
      );
  
}
 
export default CommentForm;