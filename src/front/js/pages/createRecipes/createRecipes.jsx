import React, { useState, useContext, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { Context } from "../../store/appContext";
import Select from "react-select";

import { createRecipe } from "../../service/recipe";
import { listIngredient } from "../../service/ingredient";
import SuccessMessage from "../../component/SuccessMessage/SuccessMessage.jsx";

import "../createRecipes/createRecipes.css";

export const CreateRecipes = () => {
  const { actions } = useContext(Context);
  const history = useHistory();
  const [ingredientList, setIngredientList] = useState([]);
  const [selectedIngredientList, setSelectedIngredientList] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [tag, setTag] = useState("");
  const [img, setImg] = useState();
  const [fileUrl, setFileUrl] = useState();

  const [isPrivate, setIsPrivate] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
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

  const isFormValid = () => {
    if (title.length == 0) {
      setErrorMessage("Falta el título");
      return false;
    }
    if (tag == 0) {
      setErrorMessage("Tienes que indicar si es comida o cena");
      return false;
    }

    if (description.length == 0) {
      setErrorMessage("Falta la descripción");
      return false;
    }
    return true;
  };

  const handleChangeTitle = (event) => {
    setTitle(event.target.value);
  };

  const handleChangeTag = (event) => {
    setTag(event.target.value);
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

  const changeImage = () => {
    document.getElementById("image").click();
  };

  const handleChangeIsPrivate = (event) => {
    setIsPrivate(event.target.checked);
  };

  const handleChangeDescription = (event) => {
    setDescription(event.target.value);
  };

  const submit = () => {
    if (!isFormValid()) {
      return;
    }
    const ingredient_list = selectedIngredientList.map((ingredient) => {
      return { id: ingredient.value, name: ingredient.label };
    });
    const payload = {
      title,
      description,
      tag,
      img,
      private: isPrivate,
      ingredient_list: ingredient_list,
    };
    createRecipe(payload)
      .then((resp) => resp.json())
      .then((data) => {
        if (data["msg"]) {
          alert("error", data["msg"]);
        } else {
          actions.showSuccessMessage("Tu receta ha sido creada");
          history.push("/my-recipes");
        }
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="container">
   
      {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
      <h3>Crear nueva receta</h3>
      <div className="row">
        <div className="col">
          <label className="form-label">Título</label>
          <input
            onChange={handleChangeTitle}
            type="text"
            className="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-default"
            placeholder="Arroz a banda"
          />
          <label className="form-label">
            ¿Es una comida, una cena o ambas?
          </label>
          <select
            className="form-select"
            aria-label="Default select example"
            onChange={handleChangeTag}
          >
            <option value="0">---</option>
            <option value="1">Comida</option>
            <option value="2">Cena</option>
            <option value="3">Ambas</option>
          </select>
          <div className="form-check">
            <input
              onChange={handleChangeIsPrivate}
              className="form-check-input"
              type="checkbox"
              checked={isPrivate}
              id="flexCheckDefault"
            />
            <label className="form-check-label" htmlFor="flexCheckDefault">
              Esta receta es privada
            </label>
          </div>
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
          {img ? (
            <img
              src={fileUrl}
              className="upload-image__image"
              onClick={changeImage}
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
          ></textarea>
        </div>
      </div>
      <div className="row">
        <div className="col">
          <div className="d-grid gap-2">
            <button type="button" className="btn btn-primary" onClick={submit}>
              Crear receta
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
