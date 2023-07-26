import { useState, useEffect, useRef } from "react";
import "./post.scss"

const Post = ({username, postText, timeStamp}) => {
    const postRef = useRef(null);
    const [postHeight, setPostHeight] = useState(null);

    useEffect(() => {
        if (postRef.current) {
            const height = postRef.current.scrollHeight + 97;
            setPostHeight(height);
        }
    }, [postHeight]);

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
                <a href="#comments">
                    Comments
                </a>
            </div>
        </div>
    )
}

export default Post