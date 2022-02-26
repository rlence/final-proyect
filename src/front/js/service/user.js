import BASE_URL from "./index.js";

export const save_img = (body) => {
  const url = `${BASE_URL}/api/user/img`;
  console.log(url);
  return fetch(url, {
    method: "POST",
    body: body,
  });
};
