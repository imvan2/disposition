import { useEffect, useState } from 'react'

const LoginForm = () =>{
  // const [submitted, setSubmitted] =useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");


  // const handleSubmit = async(event) =>{
  //       event.preventDefault();
  //       const data = {username, password};

  //       const loginUrl = "http://localhost:8001/login";
  //       const fetchConfig = {
  //           method :"POST",
  //           body: JSON.stringify(data),
  //           headers : {
  //               "Content-Type": "application/json",
  //           }
  //       }
  //       console.log("FETCH:::", fetchConfig)
  //       const response = await fetch(signupUrl, fetchConfig)
  //       console.log("response::", response)
  //       if (response.ok) {
  //         const newUser = await response.json();
  //         setUsername("");
  //         setPassword("");
  //         setSubmitted(true);
  //       }
//}
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
    </form>
    </>

);
}

export default LoginForm