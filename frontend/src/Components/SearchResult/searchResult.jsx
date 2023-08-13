import React from 'react'
import "./searchResult.scss";

const SearchResult = ({result}) => {
  return (
    <div className="searchResult">{result.username}</div>
  )
}

export default SearchResult