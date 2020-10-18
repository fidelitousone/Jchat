import * as React from 'react';
import { Left } from 'react-bootstrap/lib/media';

export default function Message(props) {

    return (
        <div className="Message">
            <img src={props.profile_picture} width="25" height="25" style={{float: 'left', paddingRight: '10px'}}></img><p>{props.username}: {props.message}</p>
        </div>
    )
}