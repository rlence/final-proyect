import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import "../navbar/navbar.css";

export const Navbar = () => {
  const [isLogged, setIsLogged] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("token")) {
      setIsLogged(true);
    }
  });

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
      {!isLogged ? (
        <div className="container-buttons">
          <Link to="/register">
            <button className="btn btn-primary">Registro</button>
          </Link>
          <Link to="/login">
            <button className="btn btn-primary">Login</button>
          </Link>
        </div>
      ) : (
        <div className="container-buttons menu">
          <Link to="/my-recipes">
            <button className="btn btn-primary">Mis recetas</button>
          </Link>
          <Link to="/my-menus">
            <button className="btn btn-primary">Mis menús</button>
          </Link>
        </div>
      )}
    </nav>
  );
};
