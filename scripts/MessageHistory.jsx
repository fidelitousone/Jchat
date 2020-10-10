import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';

export default function MessageHistory() {
    const [messageList, setMessage] = React.useState([])
    function new_message() {
        React.useEffect(() => {
            Socket.on("message receieved", (data) => {
                console.log("Server sent a message: " + data["message"]);
                setMessage(messageList => [...messageList, data["message"]]);
            })
        }, []);
    }

    new_message();

    return (
        <div className="MessageHistory">
            <ol>
                {messageList.map(messageList => (
                    <li key={messageList}>{messageList}</li>
                ))}
            </ol>
        </div>
    )
}