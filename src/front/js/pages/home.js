import React, { useContext, useState} from "react";
import { Context } from "../store/appContext";

import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const {file, setFile} = useState("");
	const {fileUrl, setFileUrl} = useState("");

	//ejemplo para previsualizar una imegen
// 	const handelChangeFile =(e) => {
// 		if(e.target.files){
// 			const reader = new FileReader();
// 			reader.onload = (e) => {
// 				if (reader.readyState === 2) {
// 					setFileUrl(reader.result);
// 				}
// 			};
// 			reader.readAsDataURL(e.target.files[0]);
// 		}

// 	};

	// const handelClick = async() =>{
	// 	try {
	// 		const form = new FormData();
	// 		form.append("img", file);
	// 		form.append("username", )
	// 	}
	// };
	return (
		<div className="text-center mt-5">
			<input type="file" onChange={handelChangeFile}></input>
			<img src ={fileUrl}></img>
		</div>
	);
};
