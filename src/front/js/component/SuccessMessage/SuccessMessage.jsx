import React, { useContext } from "react";
import { Context } from "../../store/appContext";

const SuccessMessage =() =>{
    const { store, actions } = useContext(Context);

    return(
        <div>
        {store.successMessage && (
            <div
              className="alert alert-success alert-dismissible fade show"
              role="alert"
            >
              {store.successMessage}
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
                onClick={() => actions.cleanSuccessMessage()}
              ></button>
            </div>
          )}
        </div>
    );
};
export default SuccessMessage;