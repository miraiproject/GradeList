import React, { Component } from 'react';

// Mock データ
const list = [
    {
	"id": 1,
        "text": "a@gn@ojfpr",
        "author": 1,
        "created_at": "2019-11-16T19:03:46.649899Z",
        "target": {
            "text": "naov@aihv@aiv@a",
            "author": {
                "username": "kazuki"
            },
            "created_at": "2019-11-15T09:44:55.063684Z"
        }
    }
]

class App extends Component {
    constructor (props) {
        super(props);
        this.state = { list };
    }

    render() {
        return (
            <div>
                {this.state.list.map(item => (
                    <div key={item.id}>
                        <h1>{item.author}が{item.created_at}に回答</h1>
                        <p>回答：{item.text}</p>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;
