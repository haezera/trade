import { createRoot } from "react-dom/client";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./style.css";
import Home from "./Home";
import Signup from "./Signup";
import Signin from "./Signin";
const App = () => {
  return (
    <Router>
      <div className="App">
        <div className="center">
          <div className="navbar">
            <Link to="/">home</Link>
            <Link to="/about">news</Link>
            <Link to="/signup">sign up</Link>
            <Link to="/signin">sign in</Link>
            <Link to="/contact">contact us</Link>
            <Link to="/aboutus">about us</Link>
          </div>
        </div>
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/signup" element={<Signup />}></Route>
          <Route path="/signin" element={<Signin />}></Route>
        </Routes>
      </div>
    </Router>
  );
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
