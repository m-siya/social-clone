import { Link } from "react-router-dom"
import "./signup.scss"

const Signup = () => {
    return (
        <div className="signup">
            <div className="card1">
                <div className="left">
                    <h1>Beinvenido.</h1>
                    <p>
                        Placeholder paragraph text about 
                        the website or something else.
                    </p>
                    <span>Already have an account?</span>
                    <Link to="/login">
                    <button>Login</button>
                    </Link>
                </div>
            </div>
            <div className = "card2">
                <div className="right">
                    <h1>Sign Up</h1>
                    <form>
                        <input type="text" placeholder="Username"/>
                        <input type="email" placeholder="Email"/>
                        <input type="text" placeholder="Username"/>
                        <input type="password" placeholder="Password"/>
                        <button>Sign Up</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Signup