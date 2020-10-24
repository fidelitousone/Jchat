import * as React from 'react'

export default function MessageImage (props) {
  return (
    <div className="MessageImage">
      <img src={props.profile_picture} width="25" height="25" style={{ float: 'left', paddingRight: '10px' }}></img><p>{props.username}: <img src={props.image_url} width="250" height="250"></img></p>
    </div>
  )
}
