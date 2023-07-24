import React, { useEffect, useState } from "react";
import "./navbar.scss"


const NavBar = () => {
    const [isNavOpen, setIsNavOpen] = useState(false);

    const toggleNav = () => {
        setIsNavOpen((prevIsNavOpen) => !prevIsNavOpen);
    };

    return (
        <div className={`navBar ${isNavOpen ? "open" : "closed"}`}>
            <button className="toggleButton" onClick={toggleNav}>
                {isNavOpen ? "<<" : ">>"}
            </button>

            <nav className="navLinks">
                <a className="active" href="#home">
                    Home
                </a>
                <a href="#profile"> 
                    Profile
                </a>
                <a href="#search"> 
                    Search
                </a>
                <a href="logout">
                    Logout
                </a>
            </nav>
            

        </div>
    )
}



export default NavBar