import { BrowserRouter, Routes, Route } from "react-router-dom";
import TopHits from "./Main";
import Nav from "./Nav";
import Hot from './Hot-100';
import SignupForm from './Signup';
import LoginForm from './Login';
import PersonalityForm from './PersonalityForm'
import { AuthProvider, useToken } from "./auth.js";

function GetToken() {
    // Get token from JWT cookie (if already logged in)
    useToken();
    return null
}

function App() {
  return (
    <>
      <BrowserRouter>
      <Nav />
        <div className="container">
          <Routes>
            <Route path="/" element={<TopHits/>} />
            <Route path="/Hot-100" element={<Hot/>} />
            <Route path="/SignupForm" element={<SignupForm/>} />
            <Route path="/Login" element={<LoginForm/>} />
            <Route path="/Login" element={<LoginForm/>} />
            <Route path="/Vibecheck" element={<PersonalityForm/>} />
          </Routes>
        </div>
      </BrowserRouter>
    </>

  );
}

export default App;
