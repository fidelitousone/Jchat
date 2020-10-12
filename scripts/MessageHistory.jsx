import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';

export default function MessageHistory() {
    const [messageList, setMessage] = React.useState([]);
    function new_messages() {
        React.useEffect(() => {
            Socket.on("message receieved", (data) => {
                setMessage(data["messages"]);
            });
        }, []);
    }

    new_messages();

    return (
        <div className="MessageHistory">
            {messageList.map(messageList => (
                <p key={messageList}>{messageList}</p>
            ))}
        </div>
    );
}