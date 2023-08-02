import { useState, useEffect, useRef } from "react";
import "./post.scss"
import CommentPage from "../CommentPage/commentPage";

const Post = ({username, postText, timeStamp, comments}) => {
    const postRef = useRef(null);
    const [postHeight, setPostHeight] = useState(null);

    const [openComments, setOpenComments] = useState(false);

    useEffect(() => {
        if (postRef.current) {
            const height = postRef.current.scrollHeight + 97;
            setPostHeight(height);
        }
    }, [postHeight]);


    const handleCommentsButtonClick = () => {
        setOpenComments(!openComments);
    }

    return (
        <div className="post" style={{ height: postHeight}}>
            <div className="postHeader">
                <div className="username">
                    {username}
                </div>
                <div className="timeStamp">
                    {timeStamp}
                </div>
            </div>
            
            <div className="postText" ref={postRef}>
                {postText}
            </div>
            <div className="commentLink">
                <button onClick={handleCommentsButtonClick}> Comments </button>            
            </div>

            {openComments && (
                <CommentPage comments={comments}/>
            )}

        </div>
    )
}

export default Post