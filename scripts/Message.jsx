import * as React from 'react';

export default function Message(props) {

    return (
        <div className="Message">
            <img src={props.profile_picture} width="25" height="25"></img><p>{props.username}: {props.message}</p>
        </div>
    )
}