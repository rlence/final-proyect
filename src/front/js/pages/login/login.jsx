import React, {useState } from "react";
import "../login/login.css";
import { useHistory } from "react-router-dom";
import { loginUser } from "../../service/user";

export const Login = () => {
  const [email, setEmail] = useState("");
  const [passw, setPassw] = useState("");
  const [message, setMessage] = useState("");
  const [showSpinner, setShowSpinner] = useState(false);
  const history = useHistory();

  const onLoginUserClick = () => {
    loginUser(email, passw)
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data)
        if (data == "user not exist") {
          setMessage("User does not exist");
          setShowSpinner(false);
        } else {
          localStorage.setItem("token", data["token"]);
          history.push("/");
        }
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="container-fluid">
      <p>{message}</p>

      <div className="mb-3">
        <label htmlFor="FormControlInput1" className="form-label">
          Email
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleFormControlInput1"
          placeholder="name@example.com"
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="FormControlTextarea1" className="form-label">
          Password
        </label>
        <input
          type="password"
          className="form-control"
          id="exampleFormControlTextarea1"
          rows="3"
          onChange={(e) => setPassw(e.target.value)}
        />
      </div>
      {showSpinner ? (
        <div className="spinner-border">
          <span className="visually-hidden">Loading...</span>
        </div>
      ) : (
        <button
          type="button"
          className="btn btn-primary"
          onClick={onLoginUserClick}
        >
          Login
        </button>
      )}
    </div>
  );
};
