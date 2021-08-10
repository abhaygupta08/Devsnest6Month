import './App.css';
import Header from "./containers/header";
import ProductListing from "./containers/productListing";
import ProductDetails from "./containers/productDetail";

import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";

function App() {
    return (<div className="App" >
        <Router>
            <Header />
            <Switch>
                <Route path="/" exact component={ProductListing} />
                <Route path="/product/:productId" exact component={ProductDetails} />
                <Route> 404 NOT Found</Route>
            </Switch>
        </Router>
    </div>
    );
}

export default App;