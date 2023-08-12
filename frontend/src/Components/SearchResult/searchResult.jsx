import React from 'react'
import "./searchResult.scss";

const SearchResult = ({result}) => {
  return (
    <div className="searchResult">{result.name}</div>
  )
}

export default SearchResult