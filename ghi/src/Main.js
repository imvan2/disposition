import { BrowserRouter, Routes, Route } from "react-router-dom";
import {useEffect, useState} from 'react';

// function TopHits() {

//   const options = {
//     method: "GET",
//     headers: {
//       "X-RapidAPI-Key": "4f3acccf77msh618eb26dc33adcbp1efe23jsn49ef60bca91e",
//       "X-RapidAPI-Host": "billboard-api2.p.rapidapi.com",
//     },
//   };

//   const [data, setData] = useState([]);

//   async function gettingBillboard() {
//       const response = await fetch(
//         "https://billboard-api2.p.rapidapi.com/hot-100?range=1-10&date=2022-11-26",
//         options
//       )
//         .then(data.json())
//         .catch((err) => console.error(err));

//       setData(data)
//     }


//   useEffect(() => {
//     console.log("useEffect ran");
//     gettingBillboard(); }, []);

//   console.log("data:::::", data);

//STARTS HERE
  const TopHits = () => {

  //   const options = {
  //     method: "GET",
  //     headers: {
  //       "X-RapidAPI-Key": "b42d5029a5mshb87ed9e4c8e1dd5p1f3c44jsn69ebf416a9b1",
  //       "X-RapidAPI-Host": "billboard-api2.p.rapidapi.com",
  //     },
  //   };

	// const [songs, setSongs] = useState([]);

	// useEffect(() => {
	// 	const fetchBillBoard = async () => {
	// 		const url = "https://billboard-api2.p.rapidapi.com/hot-100?range=1-10&date=2022-11-26";
	// 		const response = await fetch(url, options);

	// 		if (response.ok) {
	// 			const data = await response.json();
	// 			setSongs(data.content);
	// 		}
	// 	};
	// 	fetchBillBoard();
	// }, []);

  // console.log("songs:::::", songs)
  return (
    <>
      <div className="px-4 py-5 my-5 text-center">
        <h1 className="display-5 fw-bold">Disposition</h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">
            The premiere solution for finding music that fits your vibe (;!
          </p>
          <br></br>
          <h1>Top 100 Hits</h1>
          <br></br>
          <table className="table table-striped">
            <thead>
              <tr>
                  <th>Rank</th>
                  <th>Title</th>
                  <th>Artist</th>
                  <th>Album Image</th>
              </tr>
            </thead>
            <tbody>
                {/* {songs?.map((song, i) => {
                    return (
                        <tr key={i}>
                            <td>{song.rank}</td>
                            <td>{song.title}</td>
                            <td>{song.artist}</td>
                            <td>{song.album}</td>
                        </tr>
                    )
                })} */}
            </tbody>
            </table>
        </div>
      </div>
    </>
  );
}

export default TopHits;
