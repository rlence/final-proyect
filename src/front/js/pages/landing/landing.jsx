import React from "react";
import { Link } from "react-router-dom";
import "./landing.css";

export const Landing = () => {
  return (
    <div>
      <section className="hero">
        <div className="hero-inner">
          <h1>EASY PLANNER</h1>
          <h2>La manera más fácil y rápida de organizar tus menús</h2>
          <Link to="/register" className="btn">
            Únete
          </Link>
        </div>
      </section>
      <div className="container info">
        <div className="row first-row">
          <div className="col-md-6 col-sm-12">
            <img
              className="medium-img"
              src="https://res.cloudinary.com/dw4npwftd/image/upload/v1645726409/s-o-c-i-a-l-c-u-t-hwy3W3qFjgM-unsplash_cau0ig.jpg"
            />
          </div>
          <div className="col-md-6 col-sm-12">
            <p className="text">
              ¿Cuánto timepo inviertes elaborando los menús semanales? ¿Te
              gustaría hacerlos con un click? Con Make Menu puedes hacerlo. Crea
              las recetas que más te gusten o añádelas de entre todas las
              recetas públicas. El menú se generará automáticamente de entre
              todas las recetas que tengas en el apartado Mis recetas.
            </p>
            <div className="btn btn-landing">
              <Link to="/register">
                <button className="btn btn-primary">Regístrate</button>
              </Link>
            </div>
          </div>
        </div>
        <div className="row second-row">
          <div className="col-md-6 col-sm-12">
            <p className="text">
              ¿Tienes una receta familiar que no quieres perder? ¿De esas que
              pasan de generación en generación? Guárdala en tu zona privada, o
              hazla pública si quieres. ¿Quieres echarle un ojo a nuestras
              recetas públicas? Seguro que encuentras nuevos sabores que
              incorporar a tus menús.
            </p>
            <div className="btn-landing">
              <Link to="/recipes">
                <button className="btn btn-primary">Ver recetas</button>
              </Link>
            </div>
          </div>
          <div className="col-md-6 col-sm-12">
            <img
              className="medium-img"
              src="https://res.cloudinary.com/dw4npwftd/image/upload/v1645726409/lily-banse--YHSwy6uqvk-unsplash_1_gf2ju9.jpg"
            />
          </div>
        </div>
      </div>
    </div>
  );
};
