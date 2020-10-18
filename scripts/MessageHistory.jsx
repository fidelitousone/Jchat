import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';
import Message  from './Message';
import MessageUrl  from './MessageUrl';
import MessageImage  from './MessageImage';
import validator from 'validator';

export default function MessageHistory() {
    const [messageList, setMessage] = React.useState([]);
    var image_regex = /^https?:\/\/(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:\/[^\/#?]+)+\.(?:jpe?g|gif|png|bmp)$/i

    function list_messages() {
        var arry = [];
        for (var message of messageList) {
            arry.push(<Message username={message["username"]} message={message["message"]}/>)
        }
        return arry;
    }
    
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
            {list_messages()}
        </div>
    );
}