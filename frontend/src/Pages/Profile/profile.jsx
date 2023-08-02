import Post from "../../Components/Post/post";
import CommentPage from "../../Components/CommentPage/commentPage";
import "./profile.scss"

const Profile = () => {
    const username = "siya";
    const postText = "Lorem ipsum dolor sit amet, id volutpat nisi. Ut interdum vehicula mi, eu fermentum felis luctus vitae. Duis augue urna, venenatis sit amet tincidunt quis, finibus a nibh. Sed tincidunt eros sit amet nulla gravida scelerisque. Praesent sem nunc, elementum ut commodo ac, finibus quis arcu. Nullam eget ultricies risus, mollis commodo eros. Integer rutrum nisi purus, rhoncus congue mi pretium ut. Sed nec bibendum felis, sit amet hendrerit diam.";
    const timeStamp = "26-07-2023"
    const comments = [
        {
            username: "user1",
            commentText: "This is the first comment.",
            timeStamp: "2023-08-02",
        },
        {
            username: "user2",
            commentText: "This is the second comment.",
            timeStamp: "2023-08-02",
        },
        {
            username: "user2",
            commentText: "This is the third comment.",
            timeStamp: "2023-08-02",
        }
    ]

    return (
        <>
            <div className="profile">
                <div className="feed">
                <Post
                username={username}
                postText={postText}
                timeStamp={timeStamp}
                comments={comments}
                />
                </div>
            {/* <CommentPage comments={comments} /> */}
        </div>
        </>

    )
}

export default Profile