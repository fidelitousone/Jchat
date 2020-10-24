import * as React from 'react'
import ChatBox from './ChatBox'
import MessageBox from './MessageBox'
import ConnectedUsers from './ConnectedUsers'

export default function ChatApp () {
  return (
    <div className="ChatApp">
      <ConnectedUsers />
      <ChatBox />
      <MessageBox />
    </div>
  )
}
