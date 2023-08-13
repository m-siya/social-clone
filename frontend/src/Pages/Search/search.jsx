import "./search.scss"
import SearchBar from "../../Components/SearchBar/searchBar"
import { useState } from "react"
import SearchResultList from "../../Components/SearchResultsList/searchResultList";

const Search = () => {
    const [results, setResults] = useState([]);

    return (
        <div className="search">
            <div className="searchBar">
                <SearchBar setResults={setResults}/>
            </div>
            <div className="searchResultList">
                <SearchResultList results={results}/>
            </div>
        </div>
    )
}

export default Search