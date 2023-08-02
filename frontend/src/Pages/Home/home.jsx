import Post from "../../Components/Post/post";
import Comment from "../../Components/Comment/comment";
import "./home.scss"

const Home = () => {
    return(
        <div className="Home">
            <Post/>
            <Comment/>
        </div>
    )
}

export default Home