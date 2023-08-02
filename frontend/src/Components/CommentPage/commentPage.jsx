import Comment from "../Comment/comment";

import {useState} from 'react';

import "./commentPage.scss";


const CommentPage = ({comments}) => {
    const renderedComments = [];

    for (const comment of comments) {
        renderedComments.push(
            <Comment 
                username={comment.username}
                commentText={comment.commentText}
                timeStamp={comment.timeStamp}
            />
        );
    }

    return (
        <div className="commentPage"> {renderedComments} </div>
    );
}

export default CommentPage
