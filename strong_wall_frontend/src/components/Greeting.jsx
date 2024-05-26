import React, {useState} from "react";
import axios from "axios";

const Greeting = function(props) {

    const [name, setName] = useState('')

    const ResponseHandler = (status) => {
        props.ResponseHandler(status, name)
    }

    const btnAction = (e) => {
        const url = '/api/v1/greeting/';

        let data = {'name': name}

        axios.post(
            url,
            data
        )
        .then((response) => {
            ResponseHandler(response.status)
        })
        .catch((error) => {
            console.log(error)
        })
    }


    return (
        <div className="wrap-form">
            <div className="form">
                <span className="title">Вітання</span>
                <div className="wrap-input">
                    <input type="text" name='name' placeholder="Ваше ім'я" value={name} onChange={e => setName(e.target.value)} ></input>
                </div>
                <div className="container-btn">
                    <div className="wrap-btn">
                        <button onClick={btnAction} className="btn">Привітатись</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Greeting;