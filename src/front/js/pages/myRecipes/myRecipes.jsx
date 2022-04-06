import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../../store/appContext";
import { listRecipe } from "../../service/recipe";
import Card from "../../component/Card/card.jsx";
import Spinner from "../../component/Spinner/spinner.jsx";

import "../myRecipes/myRecipes.css";
import SuccessMessage from "../../component/SuccessMessage/SuccessMessage.jsx";

export const MyRecipes = () => {
  const { store, actions } = useContext(Context);
  const [recipeList, setRecipeList] = useState([]);
  const [copyRecipeList, setCopyRecipeList] = useState([]);

  const [loading, setLoading] = useState(false);

  const recipes = async () => {
    try {
      setLoading(true);
      const res = await listRecipe();
      const data = await res.json();
      setRecipeList(data);
      setCopyRecipeList(data);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    recipes();
  }, []);

  const handleChange = (e) => {
    const search = e.target.value;

    if (search === "") {
      setRecipeList(copyRecipeList);
    } else {
      const newListFilter = copyRecipeList.filter((recipe) => {
        const titleRecipe = recipe.recipe.title;
        if (titleRecipe.toLowerCase().indexOf(search.toLowerCase()) >= 0) {
          return recipe;
        }
      });

      setRecipeList(newListFilter);
    }
  };

  return (
    <div className="container">
     
      <section className="up">
        <Link to="/recipes/create">
          <button className="btn btn-primary">Crear receta</button>
        </Link>

        <div className="search col-md-3">
          <form className="d-flex mb-3" onChange={handleChange}>
            <input
              aria-label="Search"
              type="search"
              className="form-control me-2"
              placeholder="Buscar receta..."
            />
          </form>
        </div>
      </section>
      <div className="row cards">
        {loading ? (
          <Spinner />
        ) : (
          recipeList.map((myRecipe) => (
            <Card
              key={myRecipe.id}
              title={myRecipe.recipe.title}
              img={myRecipe.recipe.photo}
              id={myRecipe.recipe.id}
            />
          ))
        )}
      </div>
    </div>
  );
};
