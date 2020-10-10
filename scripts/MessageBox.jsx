import * as React from 'react'
import './myStyle.css';
import { Socket } from './Socket'

export default function MessageBox() {
    const [text, setText] = React.useState("");
    const [messageList, setMessageList] = React.useState([])

    function handleChange(event) {
        setText(event.target.value);
        console.log(text)
    }

    function handleSubmit(event) {

        Socket.emit(
            "new message",
            {
                "message": text
            }
        );

        console.log(text);
        setText("");
        event.preventDefault();

    }
    
    return (
        <form style={{marginLeft: "20%"}} onSubmit={handleSubmit}>
            <input type="text" value={text} onChange={handleChange}></input>
            <button>Send</button>
        </form>
    );
}