import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap";

import { Provider } from "react-redux";
import store from "./store";

import Day35Comp from "./Day35";
import "./day35.css";

const Day35 = () => {
  return (
    <Provider store={store}>
      <Day35Comp />
    </Provider>
  );
};

export default Day35;
