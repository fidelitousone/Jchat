import * as React from 'react';
import './myStyle.css';
import { Socket } from './Socket';

export default function ConnectedUsers() {
    const [userCount, setUserCount] = React.useState(0);
    
    function handle_user_presence() {
        React.useEffect(() => {
            Socket.on("user_connected", (data) => {
                setUserCount(data["user_count"]);
            });
        }, []);
        
        
        React.useEffect(() => {
            Socket.on("user_disconnected", (data) => {
                setUserCount(data["user_count"]);
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