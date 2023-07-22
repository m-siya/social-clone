import "./login.scss"

const Login = () => {
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
                    <button>Register</button>
                </div>
            </div>
            <div className = "card2">
                <div className="right">
                    <h1>Login</h1>
                    <form>
                        <input type="text" placeholder="Username"/>
                        <input type="password" placeholder="Password"/>
                        <button>Login</button>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login