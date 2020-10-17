import * as React from 'react';

export default function MessageUrl(props) {

    return (
        <div className="MessageUrl">
            <p>{props.username}: <a href={props.message}>{props.message}</a></p>
        </div>
    )
}