import React, { useState } from "react";
import "./navbar.scss"

function openNav() {
    document.getElementById("navBar").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("navBar").style.width = "0";
}


const NavBar = () => {
    const [isNavOpen, setIsNavOpen] = useState(false);

    const openNav = () => {
        setIsNavOpen(true);
    };

    const closeNav = () => {
        setIsNavOpen(false);
    };

    const toggleNav = () => {
        setIsNavOpen((prevIsNavOpen) => !(prevIsNavOpen))
    }

    return (
        <div className={`navBar ${isNavOpen ? "open" : "closed"}`}>
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

        </div>
    )
}



export default NavBar