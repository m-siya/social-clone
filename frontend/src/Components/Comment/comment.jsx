import { useEffect, useState, useRef} from "react";
import "./comment.scss";

const Comment = ({username, commentText, timeStamp}) => {
    const commentRef = useRef(null);
    const [commentHeight, setCommentHeight] = useState(null);
    
    useEffect(() => {
        if (commentRef.current) {
            const height = commentRef.current.scrollHeight + 97;
            setCommentHeight(height);
        }
    }, [commentHeight]);

    return (
        <div className="comment" style={{ height: commentHeight}}>
            <div className="commentHeader">
                <div className="username">
                    {username}
                </div>
                <div className="timeStamp">
                    {timeStamp}
                </div>
            </div>
        
            <div className="commentText" ref={commentRef}>
                {commentText}
            </div>
    </div>
    )
}

export default Comment