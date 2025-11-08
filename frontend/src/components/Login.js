import React, { useState } from 'react'

export default function Login(){
  const [user, setUser] = useState('')
  const [pass, setPass] = useState('')

  const handleSubmit = e => {
    e.preventDefault()
    // placeholder: wire up to /api/auth/login
    alert('Will call login for ' + user)
  }

  return (
    <form onSubmit={handleSubmit} style={{marginBottom:20}}>
      <input placeholder="username" value={user} onChange={e=>setUser(e.target.value)} />
      <input placeholder="password" type="password" value={pass} onChange={e=>setPass(e.target.value)} />
      <button type="submit">Login</button>
    </form>
  )
}
