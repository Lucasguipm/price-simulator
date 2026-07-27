import React from 'react'
import './ProductCard.css'

function ProductCard({productTitle, productImage, currentPrice}) {
  return (
    <>
        <div className='card-container'>
            <h2>
                {productTitle}
            </h2>
              
            {productImage && ( <img src={productImage} alt={productTitle}/> )}

            <div className='price-container'>
                <span> Preço Atual </span>
                <p> R$ {currentPrice} </p>
            </div>
        </div>
    </>
  )
}

export default ProductCard