import React, {useState} from "react";
import axios from "axios";
import ReCAPTCHA from "react-google-recaptcha";

const Greeting = function(props) {

    const [name, setName] = useState('')
    const [captchaToken, setCaptchaToken] = useState(null);
    const [errors, setErrors] = useState({});
    const [unknownError, setUnknownError] = useState('');

    const handleCaptchaChange = (token) => {
        setCaptchaToken(token);
    };

    const ResponseHandler = (status) => {
        props.ResponseHandler(status, name)
    }

    const btnAction = (e) => {
        e.preventDefault();
        setErrors({});
        setUnknownError('');

        const url = '/api/v1/greeting/';

        let data = {'name': name, 'captcha': captchaToken}

        axios.post(
            url,
            data
        )
        .then((response) => {
            ResponseHandler(response.status)
        })
        .catch((error) => {
            const errorData = error.response.data;
                const newErrors = {};

                if (errorData.name) {
                    newErrors.name = errorData.name;
                }
                if (errorData.captcha) {
                    newErrors.captcha = errorData.captcha;
                }
                if (!errorData.name && !errorData.captcha) {
                    setUnknownError('Невідома помилка');
                    console.log(errorData);
                }

                setErrors(newErrors);
        })
    }


    return (
        <div className="wrap-form">
            <div className="form">
                <span className="title">Вітання</span>
                <div className="wrap-input">
                    {errors.name && (
                        <ul>
                            {errors.name.map((err, index) => (
                                <li key={index} style={{ color: 'red' }}>{err}</li>
                            ))}
                        </ul>
                    )}
                    <input type="text" name='name' placeholder="Ваше ім'я" value={name} onChange={e => setName(e.target.value)} ></input>
                </div>
                {errors.captcha && (
                    <ul>
                        {errors.captcha.map((err, index) => (
                            <li key={index} style={{ color: 'red' }}>{err}</li>
                        ))}
                    </ul>
                )}
                <ReCAPTCHA
                    sitekey="6LcIqegpAAAAABPXQ-_fUXwVyAiWhxHBWDh65b5g"
                    onChange={handleCaptchaChange}
                />
                {unknownError && (
                    <p style={{ color: 'red' }}>{unknownError}</p>
                )}
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