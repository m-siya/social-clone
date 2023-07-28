import React, { useEffect, useState } from "react";
import {BiSolidHome, BiSolidUser, BiSolidSearch, BiSolidLogOut, BiArrowFromLeft, BiArrowFromRight, BiMoon} from 'react-icons/bi';
import "./navbar.scss"
import { DarkModeContext } from "../../Context/darkmodecontext";
import { useContext } from "react";


const NavBar = () => {

    const {toggle} = useContext(DarkModeContext)

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
                        <a>
                            <BiMoon onClick={toggle}/> Change Theme
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
                        <a>
                            <BiMoon/>
                        </a>
                    </>
                )}               
            </nav>           
        </div>
    )
}



export default NavBar