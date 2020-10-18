import * as React from 'react';

export default function MessageUrl(props) {

    return (
        <div className="MessageUrl">
            <img src={props.profile_picture} width="25" height="25"></img><p>{props.username}: <a href={props.message}>{props.message}</a></p>
        </div>
    )
}