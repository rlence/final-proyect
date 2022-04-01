import React, { useState, useContext, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { Context } from "../../store/appContext";
import Select from "react-select";
import { useParams } from "react-router-dom";
import {
  getRecipe,
  updateRecipe,
  getTag,
  updateTag,
} from "../../service/recipe";

import { listIngredient } from "../../service/ingredient";

import "../updateRecipe/updateRecipe.css";

export const UpdateRecipes = () => {
  const { actions } = useContext(Context);
  const history = useHistory();
  const [ingredientList, setIngredientList] = useState([]);
  const [selectedIngredientList, setSelectedIngredientList] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [tag, setTag] = useState("");
  const [img, setImg] = useState(undefined);
  const [fileUrl, setFileUrl] = useState("");
  const [recipe, setRecipe] = useState({});
  const { recipe_id } = useParams();
  const [errorMessage, setErrorMessage] = useState("");
  const [canRender, setCanRender] = useState(false);
  const [default_val, setDefaultVal] = useState([]);

  useEffect(() => {
    getTag(recipe_id)
      .then((response) => response.json())
      .then((data) => {
        setTag(data.tag);
      });

    getRecipe(recipe_id)
      .then((response) => response.json())
      .then((data) => {
        setRecipe(data);
        setFileUrl(data.photo);
        let def_val = data.ingredient_list.map((ele) => ({
          label: ele.name,
          value: ele.id,
        }));
        setDefaultVal(def_val);
        setSelectedIngredientList(def_val);
        setCanRender(true);
      });

    listIngredient()
      .then((response) => response.json())
      .then((data) => {
        setIngredientList(
          data.items.map((ingredient) => {
            return { value: ingredient.id, label: ingredient.name };
          })
        );
      });
  }, []);

  const handleChangeTitle = (event) => {
    setRecipe({ ...recipe, title: event.target.value });
    // setTitle(event.target.value);
  };

  const handleChangeImg = (e) => {
    if (e.target.files) {
      const img = e.target.files[0];
      setImg(img);

      const reader = new FileReader();
      reader.onload = (e) => {
        if (reader.readyState === 2) {
          setFileUrl(reader.result);
        }
      };
      reader.readAsDataURL(img);
    }
  };

  const handleChangeTag = (event) => {
    setTag(event.target.value);
    updateTag(recipe_id, event.target.value)
      .then((resp) => resp.json())
      .then((data) => {
        if (data["msg"]) {
          alert("error", data["msg"]);
        }
      })
      .catch((err) => console.log(err));
  };

  const changeImage = () => {
    document.getElementById("image").click();
  };

  const handleChangeIsPrivate = (event) => {
    setRecipe({ ...recipe, isPrivate: event.target.checked });
    // setIsPrivate(event.target.checked);
  };

  const handleChangeDescription = (event) => {
    setRecipe({ ...recipe, description: event.target.value });
    // setDescription(event.target.value);
  };

  const submit = () => {
    // if (!isFormValid()) {
    //   return;
    // }
    const ingredient_list = selectedIngredientList.map((ingredient) => {
      return { id: ingredient.value, name: ingredient.label };
    });

    recipe.ingredient_list = ingredient_list;

    let payload = {
      title: recipe.title,
      description: recipe.description,
      tag: recipe.tag,
      //private: recipe.isPrivate,
      ingredient_list: recipe.ingredient_list,
    };

    if (img) {
      payload.img = img;
    }

    updateRecipe(recipe_id, payload)
      .then((resp) => resp.json())
      .then((data) => {
        if (data["msg"]) {
          alert("error", data["msg"]);
        } else {
          actions.showSuccessMessage("Tu receta ha sido actualizada");
          history.push("/my-recipes");
        }
      })
      .catch((err) => console.log(err));
  };

  console.log(recipe);
  console.log(tag);

  if (!canRender) {
    return <div>Loading...</div>;
  } else {
    return (
      <div className="container">
        {errorMessage && (
          <div className="alert alert-danger">{errorMessage}</div>
        )}
        <h3>Actualizar receta</h3>
        <div className="row">
          <div className="col">
            <label className="form-label">Título</label>
            <input
              onChange={handleChangeTitle}
              type="text"
              className="form-control"
              aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-default"
              defaultValue={recipe.title}
            />
            <label className="form-label">
              ¿Es una comida, una cena o ambas?
            </label>
            <select
              className="form-select"
              aria-label="Default select example"
              onChange={handleChangeTag}
              value={tag ? tag.toString() : "0"}
            >
              <option value="0">---</option>
              <option value="1">Comida</option>
              <option value="2">Cena</option>
              <option value="3">Ambas</option>
            </select>
          </div>
          <div className="col">
            <input
              onChange={handleChangeImg}
              id="image"
              name="input-b1"
              type="file"
              className="file d-none"
              data-browse-on-zone-click="true"
            />
            {fileUrl ? (
              <img
                src={fileUrl}
                className="upload-image__image"
                onClick={changeImage}
                defaultValue={recipe.photo}
              />
            ) : (
              <label htmlFor="image" className="upload-image">
                {/* Selecciona la imagen de la receta */}
              </label>
            )}
          </div>
        </div>
        <div className="row">
          <div className="col">
            <label className="form-label">Ingredientes</label>
            <Select
              isMulti
              options={ingredientList}
              onChange={(data) => setSelectedIngredientList(data)}
              isSearchable={true}
              isClearable={true}
              defaultValue={default_val}
            />
          </div>
        </div>

        <div className="row">
          <div className="col">
            <label className="form-label">Descripción</label>
            <textarea
              onChange={handleChangeDescription}
              className="form-control"
              rows="3"
              defaultValue={recipe.description}
            ></textarea>
          </div>
        </div>
        <div className="row">
          <div className="col">
            <div className="d-grid gap-2">
              <button
                type="button"
                className="btn btn-primary"
                onClick={submit}
              >
                Actualizar
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
};
