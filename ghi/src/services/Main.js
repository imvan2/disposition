//STARTS HERE
import '../ResultsAnimation.css';
import './Main.css';
import { useAuthContext } from '../authorization/useToken';
import { useState, useEffect } from 'react';


const TopHits = () => {
  const [top100, setTop100] = useState([]);

  useEffect(() => {
    async function getTop100() {
      const top100Url = `${process.env.REACT_APP_PLAYLIST_API_HOST}/top100/`;
      const fetchConfig = {
        method: "GET",
        headers: {
          "Content-type": "application/json"
        },
      };

      const top100Response = await fetch(top100Url, fetchConfig);
      if (top100Response.ok) {
        const data = await top100Response.json();
        setTop100(data);
      }
    }
    getTop100();
  }, []);

  // checking if the user is logged in with our app and/or spotify
  const { token } = useAuthContext();
  const [loggedInBoth, setLoggedInBoth] = useState(false);

  const spotToken = window.localStorage.getItem("token");
  // console.log("spotToken:::", spotToken);
  // console.log("token::::", token);

  const checkingToken = (token, spotToken) => {
    if ((typeof (token) == "string") === true && (typeof (spotToken) == "string") === true) {
      setLoggedInBoth(true);
    } else {
      setLoggedInBoth(false);
    }
  };

  useEffect(() => { checkingToken(token, spotToken) });

  return (
    <>
      <header>
      </header>
      {/* <body> */}
      <div>
        <div className="col-xs-12 center-block text-center align-items-center justify-content-center">
          {/* <h1 className="animate__lightSpeedInRight display-5 fw-bold"></h1> */}
          <div className="col-lg-6 mx-auto">
            <p className="display-5 mt-5 h-100 d-flex  align-items-center justify-content-center ">
              The premiere solution for finding music that fits your vibe!
            </p>
            {/* <h1 className="display-5 fw-bold"></h1> */}
            <br></br>
            <br></br>
            {/* {if (token && )}
          <a href="/Login" button="button" className="animate__zoomInDown btn btn-primary btn-lg center bg-secondary">
            Get a Vibe Check
          </a> */}
            {!loggedInBoth ? <a href="/disposition/Login" button="button" className="btn btn-primary btn-lg center bg-secondary">
              Get a Vibe Check
            </a> : <a href="/disposition/VibeCheck" button="button" className="btn btn-primary btn-lg center bg-secondary">
              Get a Vibe Check
            </a>}
            <br></br>
            <br></br>
            <br></br>
            <div className="shadow-l g p-3 mb-5 bg-white rounded">
              <h1>BillBoard's Top 100 Hits</h1>
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

                  {top100.map((song, id) => {
                    return (
                      <tr key={id}>
                        <td>{song.rank}</td>
                        <td>{song.title}</td>
                        <td>{song.artist}</td>
                        <td><img width={"100%"} src={song.album_pic} alt="album art here"></img></td>
                      </tr>
                    )
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      {/* </body> */}
    </>
  );
}

export default TopHits;
