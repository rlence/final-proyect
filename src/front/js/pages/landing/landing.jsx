import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import "./landing.css";



export const Landing = () => {
  return (
    <div>
      <section className="hero">
        <div className="hero-inner">
          <h1>Menu planner</h1>
          <h2>La manera más fácil y rápida de organizar tus menús</h2>
          <Link to="/register" href="https://example.com/" className="btn">
              Unete
            
          </Link>
        </div>
      </section>
        <div className="row">
          <div className="col-6">
            <p>
              <img className="medium-img" src="https://res.cloudinary.com/dw4npwftd/image/upload/v1645726409/s-o-c-i-a-l-c-u-t-hwy3W3qFjgM-unsplash_cau0ig.jpg" />
            </p>
            <p>Guarda en tu zona privada todas tus recetas, las recetas familiares que no quieres perder, o aquellas que tienen ganas de probar e inclui en tus menús.</p>
            <button type="button" className="btn btn-outline-info">Info</button>

          </div>
          <div  className="col-6">
            <p>Filtra entre todas tus recetas las que quieres incorporar al menú y con un solo click generamos tus menus automaticamente junto con la lista de la compra</p>
            <p>
              <img className="medium-img" src="https://res.cloudinary.com/dw4npwftd/image/upload/v1645726409/lily-banse--YHSwy6uqvk-unsplash_1_gf2ju9.jpg" />
            </p>
            <button type="button" className="btn btn-outline-info">Info</button>
          </div>
        </div>
    </div>
  );
};
