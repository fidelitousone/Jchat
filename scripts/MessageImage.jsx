import * as React from 'react';

export default function MessageImage(props) {

    return (
        <div className="MessageImage">
            <p>{props.username}: <img src={props.image_url} width="250" height="250"></img></p>
        </div>
    )
}