import * as React from 'react'
import './myStyle.css'
import { Socket } from './Socket'

export default function ConnectedUsers () {
  const [userCount, setUserCount] = React.useState(0)

  function HandleUserPresence () {
    React.useEffect(() => {
      Socket.on('user_connected', (data) => {
        setUserCount(data.user_count)
      })
    }, [])

    React.useEffect(() => {
      Socket.on('user_disconnected', (data) => {
        setUserCount(data.user_count)
      })
    }, [])
  }

  HandleUserPresence()
  return (
    <div className="ConnectedUsers">
      <p>Connected Users: {userCount}</p>
    </div>
  )
}
