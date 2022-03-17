import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop.jsx";

import { Home } from "./pages/home";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import injectContext from "./store/appContext";
import { Landing } from "./pages/landing/landing.jsx";
import { Login } from "./pages/login/login.jsx";
import { Register } from "./pages/register/register.jsx";
import { MyRecipes } from "./pages/myRecipes/myRecipes.jsx";
import { MyMenus } from "./pages/myMenus/myMenus.jsx";
import { CreateRecipes } from "./pages/createRecipes/createRecipes.jsx";
import { ViewRecipe } from "./pages/viewRecipe/viewRecipe.jsx";

import { Navbar } from "./component/navbar/navbar.jsx";
import { Footer } from "./component/footer.jsx";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div>
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <Navbar />
          <Switch>
            <Route exact path="/">
              <Landing />
            </Route>
            <Route exact path="/login">
              <Login />
            </Route>
            <Route exact path="/register">
              <Register />
            </Route>
            <Route exact path="/my-recipes">
              <MyRecipes />
            </Route>
            <Route exact path="/my-menus">
              <MyMenus />
            </Route>
            <Route exact path="/recipes/create">
              <CreateRecipes />
            </Route>
            <Route exact path="/recipes/:recipe_id">
              <ViewRecipe />
            </Route>
            <Route>
              <h1>Not found!</h1>
            </Route>
          </Switch>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
