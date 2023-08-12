import { BiSearch} from "react-icons/bi";
import React, {useState} from 'react';

import "./searchBar.scss";

const SearchBar = ({setResults}) => {
    const [input, setInput] = useState("");

    const fetchData = (value) => {
        fetch("https://jsonplaceholder.typicode.com/users")
            .then((response) => response.json())
            .then((json) => {
                const results = json.filter((user) => {
                    return (
                            value && 
                            user &&
                            user.name && 
                            user.name.toLowerCase().includes(value)
                    );
                });
                setResults(results);
            });

    };

    const handleChange = (value) => {
        setInput(value);
        fetchData(value);
    };

    return (
        <div className="inputWrapper">
            <BiSearch id="searchIcon"/>

            <input placeholder="Type to Search.." 
            value={input} 
            onChange={(e) => handleChange(e.target.value)}/>
        </div>
    )
}

export default SearchBar