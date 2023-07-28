import { Link } from "react-router-dom"
import "./login.scss"
import { AuthContext } from "../../Context/authentication";
import { useContext } from "react";

const Login = () => {

    const {login} = useContext(AuthContext);

    const handleLogin = ()=>{
        login();
    }

    return (
        <div className="login">
            <div className="card1">
                <div className="left">
                    <h1>Bonjour.</h1>
                    <p>
                        Placeholder paragraph text about 
                        the website or something else.
                    </p>
                    <span>Don't have an account?</span>
                    <Link to="/signup">
                    <button>Sign Up</button>
                    </Link>
                </div>
            </div>
            <div className = "card2">
                <div className="right">
                    <h1>Login</h1>
                    <form>
                        <input type="text" placeholder="Username"/>
                        <input type="password" placeholder="Password"/>
                        <button onClick={handleLogin}>Login</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login