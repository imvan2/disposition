import { useEffect, useState } from "react";
import { useToken, useAuthContext, getTokenInternal } from "./useToken";
import { useNavigate } from "react-router-dom";

function Login() {
  const [, login] = useToken();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const { token } = useAuthContext();
  console.log("token 1 from login::", token)

  const handleSubmit = async (e) => {
    e.preventDefault();
    const name = await login(username, password);

    if (name !== null) {
      navigate("/Vibecheck");
    } else {
      navigate("/SignupForm");
    }

  };
  return (
    <>
      <br></br>
      <br></br>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="username" className="form-label">
            User Name
          </label>
          <input
            onChange={(e) => setUsername(e.target.value)}
            type="text"
            className="form-control"
            id="username"
            placeholder="Username"
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">
            Password
          </label>
          <input
            onChange={(e) => setPassword(e.target.value)}
            type="password"
            className="form-control"
            id="password"
            placeholder="shhhhhh"
          />
        </div>
        <button className="btn btn-primary">Login</button>
        <div className="success-message">
          Welcome back! Great seeing you again. Can I get you a cup of tea?
        </div>
        <p>
          Not a member yet? Sign-up{" "}
          <a href="http://localhost:3000/SignupForm">here</a>
        </p>
      </form>
    </>
  );
}

export default Login;
