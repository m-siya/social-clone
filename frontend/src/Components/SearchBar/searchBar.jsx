import { BiSearch} from "react-icons/bi";
import React, {useState} from 'react';

import "./searchBar.scss";

const SearchBar = ({setResults}) => {
    const [input, setInput] = useState("");

    const fetchData = (value) => {
        fetch("http://localhost:8000")
            .then((response) => response.json())
            // .then(data => {
            //     console.log(data);
            // })
            .then((json) => {
                const results = json.filter((user) => {
                    return (
                            value && 
                            user &&
                            user.username && 
                            user.username.toLowerCase().includes(value)
                    );
                });
                //console.log(results);
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