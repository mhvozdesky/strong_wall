import React from "react";

const Answer = function(props) {
    const { status, name } = props;
    let message = "";

    if (status === 200) {
        message = `Вже бачились, ${name}`;
    } else if (status === 201) {
        message = `Привіт, ${name}`;
    }

    return (
        <div className="wrap-form">
            <div className="form">
                <span className="title">{message}</span>
            </div>
        </div>
    );
};

export default Answer;