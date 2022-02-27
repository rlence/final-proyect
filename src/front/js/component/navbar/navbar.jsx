import React from "react";
import { Link } from "react-router-dom";
import "../navbar/navbar.css";
import logoImageUrl from "../../../img/logo.png";

export const Navbar = () => {
  return (
    <nav className="navbar navbar-light bg-light">
      <div className="container-logo">
        <Link to="/">
          <span className="navbar-brand mb-0 h1">
            <img className="logo" src={logoImageUrl} />
          </span>
        </Link>
      </div>

      <div className="container-buttons">
        <Link to="/register">
          <button className="btn btn-outline-primary">Registro</button>
        </Link>
        <Link to="/login">
          <button className="btn btn-outline-primary">Login</button>
        </Link>
      </div>
    </nav>
  );
};
