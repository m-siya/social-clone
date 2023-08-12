import React from 'react'
import "./searchResultList.scss";
import SearchResult from '../SearchResult/searchResult';

const SearchResultList = ({results}) => {
  return (
    <div className='resultsList'>
        {
            results.map((result, id) => {
                return <SearchResult result={result} key={id}/>
            })
        }
    </div>
  )
}

export default SearchResultList