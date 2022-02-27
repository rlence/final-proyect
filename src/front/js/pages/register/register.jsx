import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

import "./register.css";
import { registerService } from "../../services/register_service";

export const Register = () => {
  const history = useHistory();
  const [isLoading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [lastName, setLastName] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  function isFormValid() {
    if (name.length == 0) {
      setErrorMessage("El nombre es obligatorio");
      return false;
    }
    if (email.length == 0) {
      setErrorMessage("El email es obligatorio");
      return false;
    }
    if (password.length == 0) {
      setErrorMessage("La contraseña es obligatoria");
      return false;
    }
    if (password != repeatPassword) {
      setErrorMessage("La contraseña no coincide");
      return false;
    }
    return true;
  }

  function registerUser() {
    if (isFormValid()) {
      const userInfo = {
        name: name,
        lastName: lastName,
        email: email,
        password: password,
      };
      setLoading(true);
      registerService(userInfo)
        .then((resp) => resp.json())
        .then((data) => {
          console.log(data);
          if (data["error"]) {
            setErrorMessage(data["error"]["message"]);
          } else {
            setErrorMessage("");
            localStorage.setItem("token", JSON.stringify(data));
            history.push("/");
          }
        })
        .catch((err) => {
          console.log(err);
        })
        .finally(() => setLoading(false));
    }
  }

  return (
    <div className="container-fluid">
      {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
      <div className="mb-3">
        <form>
          <label>
            Nombre*
            <input
              type="text"
              onChange={(e) => setName(e.target.value)}
              className="form-control"
            />
          </label>
          <br />
          <label>
            Apellidos
            <input
              type="text"
              className="form-control"
              onChange={(e) => setLastName(e.target.value)}
            />
          </label>
          <br />
          <label>
            Email*
            <input
              type="email"
              className="form-control"
              onChange={(e) => setEmail(e.target.value)}
            />
          </label>
          <br />
          <label>
            Contraseña*
            <input
              type="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
          <br />
          <label className="last-label">
            Repetir contraseña*
            <input
              type="password"
              className="form-control"
              onChange={(e) => setRepeatPassword(e.target.value)}
            />
          </label>
          <br />
          <button
            type="button"
            className="btn btn-primary"
            onClick={registerUser}
            disabled={isLoading}
          >
            {isLoading && (
              <span
                className="spinner-border spinner-border-sm"
                role="status"
                aria-hidden="true"
              ></span>
            )}
            Crear cuenta
          </button>
        </form>
      </div>
    </div>
  );
};
