import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { save_img } from "../service/user.js";
import "../../styles/home.css";
import { format } from "prettier";

export const Home = () => {
  const { store, actions } = useContext(Context);

  const [file, setFile] = useState("");
  const [fileUrl, setFileUrl] = useState("");

  const handelChangeFile = (e) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
      const reader = new FileReader();
      reader.onload = (e) => {
        if (reader.readyState === 2) {
          console.log("result", reader.result);
        }
      };
      reader.readAsDataURL(e.target.files[0]);
    }
  };

  const handelClick = async () => {
    try {
      const form = new FormData();
      form.append("img", file);
      form.append("username", "rlence");
      from.append("email", "kngewghiehg@gmail.com");
      const res = await save_img(form);
      const data = await res.json();
      console.log(data);
      setFileUrl(data[0]);
    } catch (err) {
      console.log(err);
    }
  };
  console.log(file);
  return (
    <div className="text-center mt-5">
      hola vamos hacer una subida de archivos
      <input type="file" onChange={handelChangeFile}></input>
      <img src={fileUrl}></img>
      <button onClick={handelClick}>save imga</button>
    </div>
  );
};
