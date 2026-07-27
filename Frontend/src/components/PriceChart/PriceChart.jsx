import React from 'react'
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import './PriceChart.css'

function PriceChart({title, data}) {
  return (
    <>
      <div className='chart-container'>
        <h3 >{title}</h3>
        <div className='chart-layout'>
          <ResponsiveContainer>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="date" tick={{ fontSize: 12 }} />
              <YAxis domain={['auto', 'auto']} tick={{ fontSize: 12 }} unit=" R$" />
              <Tooltip formatter={(val) => [`R$ ${val.toFixed(2)}`, 'Preço']} />
              <Line type="monotone" dataKey="price" stroke="#799c4b" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </>
  )
}

export default PriceChart