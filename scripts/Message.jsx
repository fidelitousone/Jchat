import * as React from 'react';

export default function Message(props) {

    return (
        <div className="Message">
            <p>{props.username}: {props.message}</p>
        </div>
    )
}