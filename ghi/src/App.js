import { BrowserRouter, Routes, Route } from "react-router-dom";
import TopHits from "./Main";
import Nav from "./Nav";
import Hot from './Hot-100';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<TopHits/>} />
          <Route path="/Hot-100" element={<Hot/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
