import React, { useState, useEffect, useContext } from "react";
import { Context } from "../../store/appContext";

import { getMenu, autoMenu } from "../../service/menu";

import "../myMenus/myMenus.css";

export const MyMenus = () => {
  const { store, actions } = useContext(Context);
  const [menu, setMenu] = useState({});
  const [menuNotFound, setMenuNotFound] = useState(false);

  const [loading, setLoading] = useState(false);

  const [currentDate, setCurrentDate] = useState(new Date());
  const [week, setWeek] = useState([]);
  const [warningMessage, setWarningMessage] = useState("");

  useEffect(() => {
    setLoading(true);
    setWeek(calculateWeek(currentDate));
    getMenu(currentDate.toISOString())
      .then((response) => response.json())
      .then((data) => {
        if (data == "menu not found") {
          setLoading(false);
          setMenuNotFound(true);
        } else {
          setLoading(false);
          setMenu(data);
        }
      });
  }, [currentDate]);

  const newMenu = () => {
    setLoading(true);
    autoMenu(currentDate.toISOString())
      .then((response) => response.json())
      .then((data) => {
        debugger;
        if (data.error.message == "insufficient recipes") {
          setWarningMessage("No tienes recetas suficientes para crear un menú");
        } else {
          setMenu(data);
          setMenuNotFound(false);
        }
      })
      .catch((error) => {
        console.log(error);
      });

    setLoading(false);
  };

  const capitalize = (word) => {
    const lower = word.toLowerCase();
    return word.charAt(0).toUpperCase() + lower.slice(1);
  };

  const getMonday = (date) => {
    date = new Date(date);
    let day = date.getDay(),
      diff = date.getDate() - day + (day == 0 ? -6 : 1);
    return new Date(date.setDate(diff));
  };

  const calculateWeek = (date) => {
    const monday = getMonday(date);
    let week = [monday];
    for (let index = 1; index < 7; index++) {
      week.push(
        new Date(
          monday.getFullYear(),
          monday.getMonth(),
          monday.getDate() + index
        )
      );
    }
    return week;
  };

  const previousWeek = () => {
    setCurrentDate(
      new Date(
        currentDate.getFullYear(),
        currentDate.getMonth(),
        currentDate.getDate() - 7
      )
    );
  };

  const nextWeek = () => {
    setCurrentDate(
      new Date(
        currentDate.getFullYear(),
        currentDate.getMonth(),
        currentDate.getDate() + 7
      )
    );
  };

  const getLunchList = () => {
    let lunchList = [];
    if ("menu_recipe_list" in menu) {
      lunchList = menu.menu_recipe_list.filter((menu_recipe) => {
        return menu_recipe.selected_tag == 1;
      });
    }

    return lunchList;
  };

  const getDinnerList = () => {
    let dinnerList = [];
    if ("menu_recipe_list" in menu) {
      dinnerList = menu.menu_recipe_list.filter((menu_recipe) => {
        return menu_recipe.selected_tag == 2;
      });
    }
    return dinnerList;
  };

  return (
    <div className="container">
      {warningMessage && (
        <div className="alert alert-warning" role="alert">
          No tienes recetas suficientes para crear un menú.
        </div>
      )}
      {menuNotFound ? (
        <section className="new-menu">
          <button className="btn btn-primary" onClick={newMenu}>
            Generar menú
          </button>
          <div className="alert alert-light" role="alert">
            No tienes menú asignado para esta semana. Clicka en Generar menú
            para crearlo.
          </div>
        </section>
      ) : (
        <div>
          <section className="move-weeks">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              fill="currentColor"
              className="bi bi-arrow-left"
              viewBox="0 0 16 16"
              onClick={previousWeek}
            >
              <path
                fill-rule="evenodd"
                d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"
              />
            </svg>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              fill="currentColor"
              className="bi bi-arrow-right"
              viewBox="0 0 16 16"
              onClick={nextWeek}
            >
              <path
                fill-rule="evenodd"
                d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"
              />
            </svg>

            <div>
              <label className="month">
                {capitalize(
                  currentDate.toLocaleDateString("es-es", {
                    month: "long",
                    year: "numeric",
                  })
                )}
              </label>
            </div>
          </section>
          <div className="table-responsive-lg">
            <table className="table">
              <thead>
                <tr>
                  {week.map((day, i) => {
                    return (
                      <th key={i}>
                        {capitalize(
                          day.toLocaleDateString("es-es", {
                            weekday: "long",
                            day: "numeric",
                          })
                        )}
                      </th>
                    );
                  })}
                </tr>
              </thead>
              <tbody>
                <tr>
                  {getLunchList().map((menu_recipe) => {
                    return (
                      <td key={menu_recipe.id}>{menu_recipe.recipe.title}</td>
                    );
                  })}
                </tr>
                <tr>
                  {getDinnerList().map((menu_recipe) => {
                    return (
                      <td key={menu_recipe.id}>{menu_recipe.recipe.title}</td>
                    );
                  })}
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
