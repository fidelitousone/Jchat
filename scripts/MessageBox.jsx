/* eslint-disable no-return-assign */
import * as React from 'react'
import './myStyle.css'
import { Socket } from './Socket'
import { GoogleLogin } from 'react-google-login'

export default function MessageBox () {
  const [text, setText] = React.useState('')
  const [disabled, setDisabled] = React.useState(true)
  const [email, setEmail] = React.useState('')
  const [profilePicture, setProfilePicture] = React.useState('')

  function handleChange (event) {
    setText(event.target.value)
    console.log(text)
  }

  function handleSubmit (event) {
    Socket.emit(
      'new message',
      {
        username: email,
        message: text,
        profile_picture: profilePicture
      }
    )

    console.log(text)
    setText('')
    event.preventDefault()
  }

  const responseGoogle = (response) => {
    setDisabled(prevState => prevState = false)
    setEmail(prevState => prevState = response.profileObj.email)
    setProfilePicture(prevState => prevState = response.profileObj.imageUrl)
    Socket.emit(
      'user_logged_in',
      {
        add_user: email
      }
    )
  }

  return (
    <div>
      <form style={{ marginLeft: '27.5%' }} onSubmit={handleSubmit}>
        <input type="text" value={text} onChange={handleChange} disabled={disabled}></input>
        <button disabled={disabled}>Send</button>
      </form>
      <GoogleLogin
        clientId="285282648119-fijvnrjed7qt8da3etodcr0dtajarn0k.apps.googleusercontent.com"
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={'single_host_origin'}
      />
    </div>
  )
}
