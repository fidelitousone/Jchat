import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';

export default function MessageBox() {
    const [text, setText] = React.useState("");
    const [disabled, setDisabled] = React.useState(true);

    function handleChange(event) {
        setText(event.target.value);
        console.log(text);
    }

    function handleSubmit(event) {
        
        Socket.emit(
            "new message",
            {
                "message": text,
            }
        );

        console.log(text);
        setText("");
        event.preventDefault();

    }
    
    return (
        <div>
            <form style={{marginLeft: "27.5%"}} onSubmit={handleSubmit}>
                <input type="text" value={text} onChange={handleChange} disabled={disabled}></input>
                <button>Send</button>
            </form>
        </div>
    );
}