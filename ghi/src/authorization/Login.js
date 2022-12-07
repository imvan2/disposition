import { useEffect, useState } from "react";
import { useToken} from "./useToken";
// import {useAuthContext, getTokenInternal } from "./useToken";
import { useNavigate } from "react-router-dom";

function Login() {

   // From developer dashboard
    const CLIENT_ID = "5a2a9a022fc549efae7b97b447d43b5c"
    // must be set in the developer dashboard (source of Under Construction Warning)
    const REDIRECT_URI = "http://localhost:3000/Login"
    // authorization endpoint
    const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
    //requirement
    const RESPONSE_TYPE = "token"

    // Set and maintain state
    const [token, setToken] = useState('')

   useEffect(() => {
        const hash = window.location.hash

        let token = window.localStorage.getItem("token")

        // how to get token from url (when we have a hashtag and no token)
        if (!token && hash) {
            token = hash.substring(1).split("&").find(elem => elem.startsWith("access_token")).split("=")[1]
            // set hash token to an empty string
            window.location.hash = ""
            // save token to local storage
            window.localStorage.setItem("token", token)
        }
        setToken(token)
    }, [])

    const logout = () => {
      setToken("")
      window.localStorage.removeItem("token")
    }

  const [, login] = useToken();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

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
      <h1>Please login to spotify first</h1>
      <h2>
      {!token ?
        <a href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}`}>Login to Spotify</a>
        : <button className="btn btn-dark" onClick={logout}>Logout</button>}
        </h2>


      {!token ?
        <p></p> :
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
      }
      {/* <form onSubmit={handleSubmit}>
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
      </form> */}
    </>
  );
}

export default Login;
