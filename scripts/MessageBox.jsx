import * as React from 'react';
import './myStyle.css';

export default function MessageBox() {


    return (
        <form style={{marginLeft: "20%"}}>
            <input type="text"></input>
            <button>Send</button>
        </form>
    )
}