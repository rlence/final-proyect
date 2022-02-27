export const registerService = (userInfo) => {
  return fetch(
    "https://3001-lienzoenblanco-finalproy-q9k5fffbwbi.ws-eu34xl.gitpod.io/api/user/register",
    {
      method: "POST",
      body: JSON.stringify(userInfo),
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
};
