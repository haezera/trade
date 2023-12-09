import "./style.css";
import { useState } from "react";

const Signup = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res = await fetch("http://localhost:5000/user/register", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          firstName: firstName,
          lastName: lastName,
          email: email,
          password: password,
        }),
      });
      console.log("New session:" + res);
      if (res.status === 200) {
        setFirstName("");
        setLastName("");
        setEmail("");
        setPassword("");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="App">
      <center>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={firstName}
            placeholder="First name"
            onChange={(e) => setFirstName(e.target.value)}
          />{" "}
          <br />
          <input
            type="text"
            value={lastName}
            placeholder="Last name"
            onChange={(e) => setLastName(e.target.value)}
          />
          <br />
          <input
            type="text"
            value={email}
            placeholder="Email"
            onChange={(e) => setEmail(e.target.value)}
          />{" "}
          <br />
          <input
            type="password"
            value={password}
            placeholder="Password"
            onChange={(e) => setPassword(e.target.value)}
          />
          <br />
          <button type="submit">Create</button>
        </form>
      </center>
    </div>
  );
};

export default Signup;
