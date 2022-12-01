// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import {useEffect, useState} from 'react';





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
    const data = [{'rank': '1', 'title': 'Anti-Hero', 'artist': 'Taylor Swift', 'weeks at no.1': '4', 'last week': '1', 'peak position':'1', 'weeks on chart': '4', 'album': 'https://charts-static.billboard.com/img/2022/10/taylor-swift-824-antihero-fgo-180x180.jpg'},
                  {'rank': '2', 'title': 'Rich Flex', 'artist': 'Drake & 21 Savage', 'last week': '2', 'peak position': '2', 'weeks on chart': '2', 'album': 'https://upload.wikimedia.org/wikipedia/en/a/a5/Her_Loss.jpeg'},
                  {'rank': '3', 'title': 'Unholy', 'artist': 'Sam Smith & Kim Petras', 'last week': '10', 'peak position': '1', 'weeks on chart': '8', 'album': 'https://upload.wikimedia.org/wikipedia/en/3/38/Sam_Smith_and_Kim_Petras_-_Unholy.png'},
                  {'rank': '4', 'title': 'Bad Habit', 'artist': 'Steve Lacy', 'last week': '13', 'peak position': '1', 'weeks on chart': '20', 'album': 'https://upload.wikimedia.org/wikipedia/en/6/63/Steve_Lacy_-_Bad_Habit.png'},
                  {'rank': '5', 'title': 'As It Was', 'artist': 'Harry Styles', 'last week': '17', 'peak position': '1', 'weeks on chart': '33', 'album': 'https://charts-static.billboard.com/img/2022/04/harry-styles-6jk-asitwas-po3-180x180.jpg'},
                  {'rank': '6', 'title': 'Major Distribution', 'artist': 'Drake & 21 Savage', 'last week': '3', 'peak position': '3', 'weeks on chart': '2', 'album': 'https://charts-static.billboard.com/img/2009/04/drake-04g-180x180.jpg'},
                  {'rank': '7', 'title': "I'm Good (Blue)", 'artist': 'David Guetta & Bebe Rexha', 'last week': '20', 'peak position': '7', 'weeks on chart': '12', 'album': 'https://upload.wikimedia.org/wikipedia/en/8/87/David_Guetta_and_Bebe_Rexha_-_I%27m_Good_%28Blue%29.png'},
                  {'rank': '8', 'title': 'Lift Me Up', 'artist': 'Rihanna', 'last week': '22', 'peak position': '2', 'weeks on chart': '3', 'album': 'https://upload.wikimedia.org/wikipedia/en/4/43/Rihanna_-_Lift_Me_Up.png'},
                  {'rank': '9', 'title': 'Spin Bout U', 'artist': 'Drake & 21 Savage', 'last week': '5', 'peak position': '5', 'weeks on chart': '2', 'album': 'https://charts-static.billboard.com/img/2009/04/drake-04g-180x180.jpg'},
                  {'rank': '10', 'title': 'On BS', 'artist': 'Drake & 21 Savage', 'last week': '4', 'peak position': '4', 'weeks on chart': '2', 'album': 'https://charts-static.billboard.com/img/2009/04/drake-04g-180x180.jpg'}]
    console.log(typeof(data))
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

                  {data.map(song => {
                  return(
                    <tr>
                      <td>{song.rank}</td>
                      <td>{song.title}</td>
                      <td>{song.artist}</td>
                      <td><img width={"100%"} src={song.album}></img></td>
                    </tr>
                    )
                  })}
            </tbody>
            </table>
        </div>
      </div>
    </>
  );
}

export default TopHits;
