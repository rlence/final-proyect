import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../../store/appContext";
import { feedListRecipe } from "../../service/recipe";
import Card from "../../component/Card/card.jsx";
import Spinner from "../../component/Spinner/spinner.jsx";

import "../feedRecipes/feedRecipes.css";
import SuccessMessage from "../../component/SuccessMessage/SuccessMessage.jsx";

export const FeedRecipes = () => {
  const { store, actions } = useContext(Context);
  const [recipeList, setRecipeList] = useState([]);
  const [currentPage, setCurrentPage] = useState([]);
  const [totalItems, setTotalItems] = useState([]);
  const [pageList, setPageList] = useState([]);
  const [totalPages, setTotalPages] = useState([]);

  const [loading, setLoading] = useState(false);

  const recipes = async (search = null, page = null) => {
    try {
      setLoading(true);
      const res = await feedListRecipe(search, page);
      const data = await res.json();
      setRecipeList(data.items);
      setCurrentPage(data.current_page);
      setTotalItems(data.total_items);
      setTotalPages(data.total_pages);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    recipes();
  }, []);

  useEffect(() => {
    const arr = [];

    for (let i = 0; i < totalPages + 1; i++) {
      arr.push(i + 1);
      console.log(arr);
      setPageList(arr);
    }
  }, [totalItems, currentPage]);

  // console.log("recipeList:" + recipeList)
  console.log("totalItems:" + totalItems);
  console.log("totalPages:" + totalPages);
  console.log("currentPage:" + currentPage);

  const handleChange = async (e) => {
    recipes(e.target.value);
  };

  const previousPage = (e) => {
    if (currentPage > 1) {
      currentPage = currentPage - 1;
    }
  };

  const nextPage = (e) => {
    if (currentPage < totalPages) {
      currentPage = currentPage + 1;
    }
  };

  return (
    <div className="container">
     

      <div className="search row justify-content-md-center">
        <form className="col-md-auto" onChange={handleChange}>
          <input
            aria-label="Search"
            type="search"
            className="form-control me-2"
            placeholder="Buscar receta..."
          />
        </form>
      </div>

      <div className="row cards">
        {loading ? (
          <Spinner />
        ) : (
          recipeList.map((recipe) => (
            <Card
              key={recipe.id}
              title={recipe.title}
              img={recipe.photo}
              id={recipe.id}
            />
          ))
        )}
      </div>

      <nav className= "recipe-pagination" aria-label="Page navigation example">
        <ul className="pagination justify-content-center">
          <li className="page-item" onClick={previousPage}>
            <a className="page-link" href="#" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>

          {pageList.map((page, index) => {
            return (
              <li
                className={`page-item ${page == currentPage ? "active" : ""}`}
                key={index}
              >
                <a className="page-link" href="#">
                  {page}
                </a>
              </li>
            );
          })}

          <li className="page-item" onClick={nextPage}>
            <a className="page-link" href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  );
};
