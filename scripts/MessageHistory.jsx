import * as React from 'react'
import './myStyle.css'
import { Socket } from './Socket'
import Message from './Message'
import MessageUrl from './MessageUrl'
import MessageImage from './MessageImage'
import validator from 'validator'

export default function MessageHistory () {
  const [messageList, setMessage] = React.useState([])
  var ImageRegex = /^https?:\/\/(?:[a-z0-9-]+\.)+[a-z]{2,6}(?:\/[^/#?]+)+\.(?:jpe?g|gif|png|bmp)$/i

  function ListMessages () {
    var arry = []
    for (var message of messageList) {
      if (ImageRegex.test(message.message)) {
        arry.push(<MessageImage username={message.username} image_url={message.message} profile_picture={message.profile_picture} />)
      } else if (validator.isURL(message.message)) {
        arry.push(<MessageUrl username={message.username} message={message.message} profile_picture={message.profile_picture} />)
      } else {
        arry.push(<Message username={message.username} message={message.message} profile_picture={message.profile_picture} />)
      }
    }
    return arry
  }

  function NewMessages () {
    React.useEffect(() => {
      Socket.on('message receieved', (data) => {
        setMessage(data.messages)
      })
    }, [])
  }

  NewMessages()

  return (
    <div className="MessageHistory">
      {ListMessages()}
    </div>
  )
}
