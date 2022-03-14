import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../../store/appContext";

import "../myRecipes/myRecipes.css";

export const MyRecipes = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="container">
      {store.successMessage && (
        <div
          className="alert alert-success alert-dismissible fade show"
          role="alert"
        >
          {store.successMessage}
          <button
            type="button"
            className="btn-close"
            data-bs-dismiss="alert"
            aria-label="Close"
            onClick={() => actions.cleanSuccessMessage()}
          ></button>
        </div>
      )}
      <p>Estás en mis recetas</p>
      <Link to="/recipes/create">
        <button className="btn btn-primary">Crear receta</button>
      </Link>
    </div>
  );
};
