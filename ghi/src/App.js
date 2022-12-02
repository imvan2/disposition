import { BrowserRouter, Routes, Route } from "react-router-dom";
import TopHits from "./services/Main";
import Nav from "./Nav";
import Hot from './in-progress/Hot-100';
import SignupForm from './authorization/Signup';
import Login from './authorization/Login';
import Vibecheck from './services/Vibecheck'
import { AuthProvider, useToken } from "./in-progress/auth.js";
import ResultsPage from './Results.js';

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
          <AuthProvider>
            <GetToken />
              <Routes>
                <Route path="/" element={<TopHits/>} />
                <Route path="/Hot-100" element={<Hot/>} />
                <Route path="/SignupForm" element={<SignupForm/>} />
                <Route path="/Login" element={<Login/>} />
                <Route path="/Vibecheck" element={<Vibecheck/>} />
                <Route path="/Results" element={<ResultsPage/>} />
              </Routes>
          </AuthProvider>
        </div>
      </BrowserRouter>

    </>

  );
}

export default App;
