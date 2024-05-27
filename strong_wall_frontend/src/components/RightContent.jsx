import React, {useState} from "react";
import Greeting from "./Greeting"
import Answer from "./Answer"


const RightContent = function() {
    const [firstMeeting, setFirstMeeting] = useState(true)
    const [name, setName] = useState('')
    const [status, setStatus] = useState('')

    const ResponseHandler = (status, name) => {
        setName(name);
        setStatus(status);
        setFirstMeeting(false)
    }


    return (
        <div className="right-content">
            {firstMeeting ? <Greeting ResponseHandler={ResponseHandler} /> : <Answer name={name} status={status} />}
        </div>
    );
};

export default RightContent;