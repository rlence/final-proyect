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
  console.log(BaseUrl);
  console.log("en el list recipe");
  console.log(localStorage.getItem("token"));
  return fetch(`${BaseUrl}/recipe/myrecipes`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};


export const getRecipe = (id) => {
  return fetch(`${BaseUrl}/recipe/myrecipes/get/${id}`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};


export const feedListRecipe = (search = null, page =null) => {
  const url = new URL(`${BaseUrl}/recipe/`);
  if (search != null && search !="") {
    url.searchParams.append("search", search);
  }
  if (page != null ) {
    url.searchParams.append("page", page);
  }
  return fetch(url);
};
