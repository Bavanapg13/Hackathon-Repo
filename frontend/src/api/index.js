const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:8000/api'

export async function extractEntities(text){
  const res = await fetch(`${API_BASE}/ner/extract`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  })
  if (!res.ok) throw new Error('NER request failed')
  return await res.json()
}

export async function login(username, password){
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  })
  return await res.json()
}
