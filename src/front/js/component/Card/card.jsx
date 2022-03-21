import React from "react";
import "./card.css";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";

const Card = (props) => {
  return (
    <div className="card card-recipe">
      <img src={props.img} className="card-img-top" alt="..." />
      <div className="card-body">
        <h5 className="card-title">{props.title}</h5>
        <Link to={`/recipes/${props.id}`} href="#" className="btn btn-primary">
          Ver receta
        </Link>
      </div>
    </div>
  );
};

Card.propTypes = {
  id: PropTypes.number,
  title: PropTypes.string,
  img: PropTypes.string,
};
export default Card;
