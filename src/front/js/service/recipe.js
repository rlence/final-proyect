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

// export const get_myrecipe =(id) => {
//   return fetch(`${BaseUrl}/recipe/myrecipes/get/${id}`, {
//     method: "GET",
//     headers: {

//       Authorization: `Bearer ${localStorage.getItem("token")}`,
//     },
//   });

// };

