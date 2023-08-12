import "./search.scss"
import SearchBar from "../../Components/SearchBar/searchBar"
import { useState } from "react"
import SearchResultList from "../../Components/SearchResultsList/searchResultList";

const Search = () => {
    const [results, setResults] = useState([]);

    return (
        <div className="search">
            <SearchBar setResults={setResults}/>
            <SearchResultList results={results}/>
        </div>
    )
}

export default Search