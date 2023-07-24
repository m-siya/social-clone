import React, { useEffect, useState } from "react";
import {BiSolidHome, BiSolidUser, BiSolidSearch, BiSolidLogOut, BiArrowFromLeft, BiArrowFromRight} from 'react-icons/bi';
import "./navbar.scss"


const NavBar = () => {
    const [isNavOpen, setIsNavOpen] = useState(false);

    const toggleNav = () => {
        setIsNavOpen((prevIsNavOpen) => !prevIsNavOpen);
    };

    return (
        <div className={`navBar ${isNavOpen ? "open" : "closed"}`}>
            <button className="toggleButton" onClick={toggleNav}>
                {isNavOpen ? <BiArrowFromRight/> : <BiArrowFromLeft/>}
            </button>

            <nav className="navLinks">
                {isNavOpen ? (
                    <>
                        <a className="active" href="#home">
                            <BiSolidHome/> Home
                        </a>
                        <a href="#profile"> 
                            <BiSolidUser/> Profile
                        </a>
                        <a href="#search"> 
                            <BiSolidSearch/> Search
                        </a>
                        <a href="logout">
                            <BiSolidLogOut/> Logout
                        </a>
                    </>
                ) : (
                    <>
                        <a className="active" href="#home">
                            <BiSolidHome/>
                        </a>
                        <a href="#profile"> 
                            <BiSolidUser/>
                        </a>
                        <a href="#search"> 
                            <BiSolidSearch/>
                        </a>
                        <a href="logout">
                            <BiSolidLogOut/>
                        </a>
                    </>
                )}               
            </nav>           
        </div>
    )
}



export default NavBar