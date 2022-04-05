import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../../store/appContext";

import "../navbar/navbar.css";

export const Navbar = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    if (localStorage.getItem("token")) {
      actions.changeLogged(true);
    }
  }, []);

  const logout = () => {
    localStorage.clear();
    actions.changeLogged(false);
  };

  return (
    <nav className="navbar navbar-light">
      <div className="container-logo">
        <Link to="/">
          <span className="navbar-brand mb-0 h1">
            <img
              className="logo"
              src="https://res.cloudinary.com/dw4npwftd/image/upload/w_700,h_700,c_fill/v1645953196/logo2_s3josi.png"
            />
          </span>
        </Link>
      </div>
      {!store.isLogged ? (
        <div className="container-buttons">
          <Link to="/recipes/">
            <button className="btn btn-primary">Recetas</button>
          </Link>
          <Link to="/register">
            <button className="btn btn-primary">Registro</button>
          </Link>
          <Link to="/login">
            <button className="btn btn-primary">Login</button>
          </Link>
        </div>
      ) : (
        <div className="container-buttons menu">
          <Link to="/recipes/">
            <button className="btn btn-primary">Recetas</button>
          </Link>
          <Link to="/my-recipes">
            <button className="btn btn-primary">Mis recetas</button>
          </Link>
          <Link to="/my-menus">
            <button className="btn btn-primary">Mis menús</button>
          </Link>
          <Link to="/my-profile">
            <button className="btn btn-primary">Mi perfil</button>
          </Link>
          <Link to="/">
            <button className="btn btn-primary" onClick={logout}>
              Salir
            </button>
          </Link>
        </div>
      )}
    </nav>
  );
};
