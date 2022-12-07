import { BrowserRouter, Routes, Route } from "react-router-dom";
import TopHits from "./services/Main";
import Nav from "./Nav";
import Hot from './in-progress/Hot-100';
import SignupForm from './authorization/Signup';
import Login from './authorization/Login';
import Logout from './authorization/Logout';
import Vibecheck from './services/Vibecheck'
import { AuthProvider, useToken } from "./authorization/useToken.js";
import Results from './services/Results.js';
import History from './services/History'

function GetToken() {
    // Get token from JWT cookie (if already logged in)
    useToken();
    return null;
}

function App() {

  return (
    <>
      <BrowserRouter>
      <AuthProvider>
      <GetToken />
      <Nav />
        <div className="container">
              <Routes>
                <Route path="/" element={<TopHits/>} />
                <Route path="/Hot-100" element={<Hot/>} />
                <Route path="/SignupForm" element={<SignupForm/>} />
                <Route path="/Login" element={<Login/>} />
                <Route path="/Logout" element={<Logout/>} />
                <Route path="/Vibecheck" element={<Vibecheck/>} />
                <Route path="/Results" element={<Results/>} />
                <Route path="/History" element={<History/>} />
              </Routes>

        </div>
        </AuthProvider>
      </BrowserRouter>

    </>

  );
}

export default App;
