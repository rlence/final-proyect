const getState = ({ getStore, setStore }) => {
  return {
    store: {
      recipes: [],
      successMessage: null,
      isLogged: false,
    },

    actions: {
      setRecipes: (recipeList) => {
        setStore({ recipes: recipeList });
      },
      changeLogged: (isLogged) => {
        const store = getStore();
        setStore({
          ...store,
          isLogged: isLogged,
        });
      },
      showSuccessMessage: (message) => {
        const store = getStore();
        setStore({
          ...store,
          successMessage: message,
        });
      },
      cleanSuccessMessage: () => {
        const store = getStore();
        setStore({
          ...store,
          successMessage: null,
        });
      },
    },
  };
};

export default getState;
