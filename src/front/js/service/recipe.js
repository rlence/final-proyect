import { BaseUrl } from "./base.js";

export const createRecipe = (payload) => {
  const formData = new FormData();
  if (payload["ingredient_list"]) {
    payload.ingredient_list = JSON.stringify(payload.ingredient_list);
  }

  for (const key in payload) {
    formData.append(key, payload[key]);
  }
  return fetch(`${BaseUrl}/recipe/create`, {
    method: "POST",
    body: formData,
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};

export const listRecipe = () => {
  return fetch(`${BaseUrl}/recipe/myrecipes`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};

export const getRecipe = (id) => {
  return fetch(`${BaseUrl}/recipe/get/${id}`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};

export const getTag = (id_recipe) => {
  return fetch(`${BaseUrl}/recipe/myrecipe/${id_recipe}`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};

export const feedListRecipe = (search = null, page = null) => {
  const url = new URL(`${BaseUrl}/recipe/`);
  if (search != null && search != "") {
    url.searchParams.append("search", search);
  }
  if (page != null) {
    url.searchParams.append("page", page);
  }
  return fetch(url);
};

export const deleteRecipe = (id) => {
  return fetch(`${BaseUrl}/recipe/myrecipes/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};

export const updateRecipe = (id, payload) => {
  const formData = new FormData();
  if (payload["ingredient_list"]) {
    payload.ingredient_list = JSON.stringify(payload.ingredient_list);
  }

  for (const key in payload) {
    formData.append(key, payload[key]);
  }
  return fetch(`${BaseUrl}/recipe/update/${id}`, {
    method: "PUT",
    body: formData,
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,      
    },
  });
};

export const updateTag = (id_recipe, tag) => {
  return fetch(`${BaseUrl}/recipe/myrecipes/update/${id_recipe}`, {
    method: "PUT",
    body: JSON.stringify({
      tag: tag,
    }),
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
      "Content-Type": "application/json",
    },
  });
};

export const saveRecipe = (id_recipe, tag) => {
  return fetch(`${BaseUrl}/recipe/myrecipes/save`, {
    method: "POST",
    body: JSON.stringify({
      id_recipe: id_recipe,
      tag: tag,
    }),
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
      "Content-Type": "application/json",
    },
  });
};
