import React, { useState, useContext, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { Context } from "../../store/appContext";
import "../userprofile/userProfile.css";
import { getUser } from "../../service/user";
import { updateUser } from "../../service/user";
import SuccessMessage from "../../component/SuccessMessage/SuccessMessage.jsx";

export const UserProfile = () => {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [lastName, setLastName] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [isLoading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const { actions } = useContext(Context);

  const history = useHistory();

  useEffect(() => {
    getUser()
      .then((response) => response.json())
      .then((data) => {
        setEmail(data.email);
        setName(data.name);
        setLastName(data.last_name);
      });
  }, []);

  function getUserInfo() {
    const userInfo = {
      name: name,
      lastName: lastName,
      email: email,
      password: password,
    };
    setLoading(true);
    updateUser(userInfo)
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        if (data["error"]) {
          setErrorMessage(data["error"]["message"]);
        } else {
          actions.showSuccessMessage("Tu perfil ha sido actualizado");          
          history.push("/my-profile");
        }
      })
      .catch((err) => {
        console.log(err);
      })
      .finally(() => setLoading(false));
  }

  return (
    <div className="container-fluid profile">      
      <div className="">
        <h1 className="my-profile-title">Mis datos</h1>
        <div>
          <div className="mb-3">
            <form className="form-inline">
              <label className="form-label">
                Nombre
                <input
                  type="text"
                  onChange={(e) => setName(e.target.value)}
                  className="form-control"
                  value={name}
                />
              </label>
              <br />
              <label className="form-label">
                Apellidos
                <input
                  type="text"
                  className="form-control"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                />
              </label>
              <br />
              <label className="form-label">
                Email
                <input
                  type="email"
                  className="form-control"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </label>
            </form>
          </div>

          <form>
            <label className="form-label">
              Contraseña nueva
              <input
                type="password"
                className="form-control"
                onChange={(e) => setPassword(e.target.value)}
              />
            </label>
            <br />
            <label className="form-label last-label">
              Repetir contraseña nueva
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
              onClick={getUserInfo}
              disabled={isLoading}
            >
              {isLoading && (
                <span
                  className="spinner-border spinner-border-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
              )}
              Cambiar datos
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
