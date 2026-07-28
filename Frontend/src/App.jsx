import { useState } from 'react'
import './App.css'
import axios from 'axios';
import PriceChart from './components/PriceChart/PriceChart.jsx';
import SearchBar from './components/SearchBar/SearchBar.jsx';
import ProductCard from './components/ProductCard/ProductCard.jsx';

function App() {
  const [url, setUrl] = useState('');
  const [productData, setProductData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!url) return;

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('/api/analyze', { url });
      setProductData(response.data);
    } catch (err) {
      console.error(err);
      setError('Erro ao buscar informações. Verifique a URL e tente novamente.');
    } finally {
      setLoading(false);
    }
  };


  return (
    <>
      <div className='app-container'>
        
        {/* 1. TOPO: INPUT DA URL */}
        <SearchBar
          url={url}
          setUrl={setUrl}
          loading={loading} 
          onSearch={handleSearch}
        />

        {error && <p style={{ color: '#dc2626', textAlign: 'center' }}>{error}</p>}

        {/* 2. CONTEÚDO PRINCIPAL (DASHBOARD EM 2 COLUNAS) */}
        {productData && (
          <div className='main-container'>

            {/* COLUNA ESQUERDA: CARD DO PRODUTO */}
            <div className='column-card'>
              <ProductCard 
                productTitle={productData.title}
                productImage={productData.image_url}
                currentPrice={productData.current_price?.toFixed(2)}
              />
            </div>
            

            {/* COLUNA DIREITA: OS 3 GRÁFICOS */}
            <div className='column-charts'>
              <PriceChart title="Últimos 7 dias" data={productData.history['7_days']} />
              <PriceChart title="Últimos 30 dias" data={productData.history['30_days']} />
              <PriceChart title="Últimos 90 dias" data={productData.history['90_days']} />
            </div>

          </div>
        )}
      </div>
    </>
  )
}

export default App
