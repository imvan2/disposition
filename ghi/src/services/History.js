import { useEffect, useState } from "react";
import "./App.css";
// import axios from "axios";
// import { useLocation } from 'react-router-dom';

function History() {
  const [answersHist, setAnswersHist] = useState([]);

  useEffect(() => {
    async function gettingData() {
      const answersUrl = `http://localhost:8002/answers/`;
      const fetchConfig = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      };
      const answersResponse = await fetch(answersUrl, fetchConfig);
      if (answersResponse.ok) {
        const answers = await answersResponse.json();
        console.log("answers:", answers);
        setAnswersHist(answers);
      }
    }
    gettingData();
  }, []);

  return (
    <div>
      <header className="">
        <br></br>
        <br></br>
        <div className="jumbotron jumbotron-fluid p-3 mb-2 bg-dark text-white">
          <div className="container"></div>
          <h1 className="display-4">History</h1>
        </div>
      </header>
      <br></br>
      <br></br>
      {/* <body> */}
      <table className="table table-striped shadow-lg p-3 mb-5 bg-white rounded">
        <thead>
          <tr>
            <th>Mood</th>
            <th>Genre</th>
          </tr>
        </thead>
        <tbody>
          {answersHist.map((answer, id) => {
            return (
              <tr key={id}>
                <td>{answer.mood}</td>
                <td>{answer.genre}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      {/* </body> */}
    </div>
  );
}
export default History;
