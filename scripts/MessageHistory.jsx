import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';
var URL = require('url').URL;

export default function MessageHistory() {
    const [messageList, setMessage] = React.useState([]);
    var regex = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/;
    
    function check_url(message) {
        try {
            new URL(message)
        } catch (_) {
            return false;
        }
        return true;
    }
    
    function new_messages() {
        React.useEffect(() => {
            // Fills all the messages in the state from the database
            Socket.on("message receieved", (data) => {
                setMessage(data["messages"]);
            });
            
        }, []);
    }
    
    new_messages();
    
    for (var message of messageList) {
        var message_without_user = message.split("User: ")[1]
        if (regex.test(message_without_user)) {
            console.log("This is a URL");
        } else {
            console.log("This is not a URL")
        }
    }
    
    return (
        <div className="MessageHistory">
            {messageList.map(message => (
                <p key={message}>{message}</p>
            ))}
        </div>
    );
}