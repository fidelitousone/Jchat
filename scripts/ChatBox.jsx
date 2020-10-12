import * as React from 'react';
import MessageHistory  from './MessageHistory';
import './myStyle.css';

export default function ChatBox() {

    return (
        <div className="ChatBox">
            <h3 style={{textAlign: "center"}}>Chat App</h3>
            <MessageHistory />
        </div>
    )
}