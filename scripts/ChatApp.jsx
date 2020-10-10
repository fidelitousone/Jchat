import * as React from 'react';
import  ChatBox from './ChatBox';
import MessageBox  from './MessageBox';

export default function ChatApp() {


    return (
        <div className="ChatApp">
            <ChatBox />
            <MessageBox />
        </div>
    )
}