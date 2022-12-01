import { useEffect, useState } from 'react'

const LoginForm = () =>{
  // const [submitted, setSubmitted] =useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  async function login(username, password) {
  const url = `${process.env.REACT_APP_ACCOUNTS_HOST}/token`;

  const form = new FormData();
  form.append("username", username);
  form.append("password", password);

  const response = await fetch(url, {
    method: "post",
    credentials: "include",
    body: form,
  });
  if (response.ok) {
    const tokenUrl = `${process.env.REACT_APP_ACCOUNTS_HOST}/token`;

    try {
      const response = await fetch(tokenUrl, {
        credentials: "include",
      });
      if (response.ok) {
        const data = await response.json();
        const token = data.access_token;
        // DO SOMETHING WITH THE TOKEN SO YOU CAN USE IT
        // IN REQUESTS TO YOUR NON-ACCOUNTS SERVICES
      }
    } catch (e) {}
    return false;
  }
  let error = await response.json();
  // DO SOMETHING WITH THE ERROR, IF YOU WANT
}

  return (
    <>
    <br></br>
    <br></br>
      <form>
        <div className= "mb-3">
            <label htmlFor="username" className="form-label">User Name</label>
            <input required value={username} onChange={e => setUsername(e.target.value)} type="text" className="form-control" id="username" placeholder="Username" />
        </div>
        <div className= "mb-3">
            <label htmlFor="password" className="form-label">Password</label>
            <input required value={password} onChange={e => setPassword(e.target.value)} type="password" className="form-control" id="password" placeholder="shhhhhh" />
        </div>

        <button className="btn btn-primary">Login</button>
        <div className='success-message'>Welcome back! Great seeing you again. Can I get you a cup of tea?</div>
        <p>Not a membe yet? Sign-up <a href="http://localhost:3000/SignupForm">here</a></p>
       
    </form>
    </>

);
}

export default LoginForm