import "./style.css";

const Signup = () => {
  return (
    <div>
      <center>
        <h1>Welcome to trade - please enter your information below</h1>
      </center>
      <hr />
      <div className="center">
        <form>
          <label htmlFor="fname">First Name</label>
          <br />
          <input type="text"></input>
          <label htmlFor="lname">Last Name</label>
          <br />
          <input type="text"></input>
          <label htmlFor="email">Email</label>
          <br />
          <input type="text"></input>
          <label htmlFor="lname">Password</label>
          <br />
          <input type="password"></input>
          <input type="submit" value="Submit"></input>
        </form>
      </div>
    </div>
  );
};

export default Signup;
