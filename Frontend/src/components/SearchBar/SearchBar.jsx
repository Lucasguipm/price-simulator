import React from 'react'
import './SearchBar.css'

function SearchBar({url, setUrl, loading, onSearch}) {
  return (
    <>
        <form onSubmit={onSearch} className='url-container'>
          <input
            type="text"
            placeholder="Cole a URL do produto na Amazon Brasil..."
            value={url || ''}
            onChange={(e) => setUrl(e.target.value)}
          />
          
          <button type="submit" disabled={loading}>
            {loading ? 'Analisando...' : 'Buscar'}
          </button>
        </form>
    </>
  )
}

export default SearchBar