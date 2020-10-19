import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';

export default function ConnectedUsers() {
    const [userCount, setUserCount] = React.useState(0);
    
    function handle_user_presence() {
        React.useEffect(() => {
            Socket.on("user_connected", (data) => {
                console.log("Server said: A user connnected")
                setUserCount(data["user_count"]);
                console.log("I updated user count to " + userCount);
            });
        }, []);
        
        
        React.useEffect(() => {
            Socket.on("user_disconnected", (data) => {
                console.log("Server said: A user disconnected")
                setUserCount(data["user_count"]);
                console.log("I updated user count to " + userCount);
            });
        }, []);
    }


    handle_user_presence();
    return(
        <div className="ConnectedUsers">
            <p>Connected Users: {userCount}</p>
        </div>
    );
}