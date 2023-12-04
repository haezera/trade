import { Link } from "react-router-dom";
import { TypeAnimation } from "react-type-animation";

const Home = () => {
  return (
    <div>
      <div className="center">
        <div className="container">
          <div className="slides">
            <div className="vertical-center">
              <TypeAnimation
                sequence={[
                  "Welcome to trade, a new trading experience.",
                  2000,
                  "Welcome to trade, a new friend.",
                  2000,
                  "Welcome to trade, your dedicated investment analyst.",
                  2000,
                  "Welcome to trade, your final solution.",
                  2000,
                ]}
                wrapper="span"
                speed={50}
                style={{
                  fontSize: "40px",
                  color: "white",
                  fontFamily: "SF Pro Text",
                }}
                repeat={Infinity}
              />
            </div>
          </div>

          <div className="slides">
            <div className="center">
              <div className="vertical-center">
                <h1>
                  We believe in free, open-sourced software for all retail
                  investors.
                </h1>{" "}
                <br />
                <h1>
                  Above all, we wish to utilise APIs and other free information
                  to give you, the user, the best experience possible.
                </h1>
              </div>
            </div>
          </div>

          <div className="slides">
            <div className="center">
              <div className="vertical-center">
                <h1>
                  Excited? Come join us <Link to="/signup"> now.</Link>
                </h1>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
