import React from "react";

const RigntContent = function() {
    return (
        <div className="right-content">
            <div className="wrap-form">
                <div className="form">
                    <span className="title">Вітання</span>
                    <div className="wrap-input">
                        <input type="text" name='name' placeholder="Ваше ім'я"></input>
                    </div>
                    <div className="container-btn">
                        <div className="wrap-btn">
                            <button className="btn">Привітатись</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default RigntContent;