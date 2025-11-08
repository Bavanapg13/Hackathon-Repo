import React, { useState } from 'react'
import Login from './components/Login'
import { extractEntities } from './api'

export default function App(){
  const [text, setText] = useState('')
  const [entities, setEntities] = useState([])

  const handleExtract = async () => {
    const res = await extractEntities(text)
    setEntities(res.entities || [])
  }

  return (
    <div style={{padding:20}}>
      <h1>NER Demo</h1>
      <Login />
      <textarea value={text} onChange={e=>setText(e.target.value)} rows={6} cols={80} />
      <br />
      <button onClick={handleExtract}>Extract Entities</button>

      <h2>Entities</h2>
      <ul>
        {entities.map((en,i)=> (
          <li key={i}>{en.text} — {en.label} ({en.start}-{en.end})</li>
        ))}
      </ul>
    </div>
  )
}
