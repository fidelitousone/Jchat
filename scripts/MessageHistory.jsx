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
            if (message.startsWith("BOT")) {
                var message_without_user = message.split("BOT: ")[1]
            } else if (message.startsWith("User: ")) {
                var message_without_user = message.split("User: ")[1]
            } else {
                arry.push(<Message username="User: (DEFFERED EXCEPTION) " message={message} />)
                continue
            }
            var user = message.split(":")[0]
            if (image_regex.test(message_without_user)) {
                arry.push(<MessageImage username={user} image_url={message_without_user} />);
            } else if (validator.isURL(message_without_user)) {
                arry.push(<MessageUrl username={user} message={message_without_user} />);
            } else {
                arry.push(<Message username={user} message={message_without_user} />);
            }
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