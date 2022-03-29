import { BaseUrl } from "./base.js";

export const listIngredient = () => {
  return fetch(`${BaseUrl}/ingredient/`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
  });
};
