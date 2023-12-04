import { createRoot } from "react-dom/client";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./style.css";
import Home from "./Home";
import Signup from "./Signup";

const App = () => {
  return (
    <Router>
      <div className="App">
        <div className="center">
          <div className="navbar">
            <Link to="/">home</Link>
            <Link to="/about">news</Link>
            <Link to="/signup">signup</Link>
            <Link to="/contact">contact us</Link>
          </div>
        </div>
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/signup" element={<Signup />}></Route>
        </Routes>
      </div>
    </Router>
  );
};

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App />);
