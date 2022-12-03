import { useEffect, useState } from "react";
import './App.css';
import axios from "axios";
import { useLocation } from 'react-router-dom';


function Spotify() {
    const location = useLocation();
    console.log("location:::", location)
    // const { result } = state;
    // console.log("data::::", data)

    // From developer dashboard
    const CLIENT_ID = "5a2a9a022fc549efae7b97b447d43b5c"
    // must be set in the developer dashboard (source of Under Construction Warning)
    const REDIRECT_URI = "http://localhost:3000/Spotify"
    // authorization endpoint
    const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
    //requirement
    const RESPONSE_TYPE = "token"

    // Set and maintain state
    const [token, setToken] = useState('')
    // const [searchKey, setSearchKey] = useState("")
    const [playlists, setPlaylists] = useState([])


    //used to get token from url
    useEffect(() => {
        const hash = window.location.hash
        let token = window.localStorage.getItem("token")
        // how to get token from url (when we have a hashtag and no token)
        if (!token && hash) {
            token = hash.substring(1).split("&").find(elem => elem.startsWith("access_token")).split("=")[1]
            // console.log("token::::: ", token)

            // set hash token to an empty string
            window.location.hash = ""
            // save token to local storage
            window.localStorage.setItem("token", token)
        }
        setToken(token)
    }, [])

    // Erase Token from local storage (when you logout)
    const logout = () => {
        setToken("")
        window.localStorage.removeItem("token")
    }
    const pullPlaylists = async(e) => {
            e.preventDefault()
            const { data } = await axios.get("https://api.spotify.com/v1/search", {
                headers: {
                    Authorization: `Bearer ${token}`
                },
                params: {
                    q: location.state.result,
                    type: "playlist"
                }
            })
            console.log("location.state.result::::::" , location.state.result)
            console.log("DATA HERE", data);
            // set data.playlists.items to playlists state
            setPlaylists(data.playlists.items)
        }



    // function to create search request to spotify
    // useEffect(() => {
    //     const pullPlaylists = async(e) => {
    //         // e.preventDefault()
    //         const { data } = await axios.get("https://api.spotify.com/v1/search", {
    //             headers: {
    //                 Authorization: `Bearer ${token}`
    //             },
    //             params: {
    //                 q: location.state.result,
    //                 type: "playlist"
    //             }
    //         })
    //         console.log("DATA HERE", data);
    //         // set data.playlists.items to playlists state
    //         setPlaylists(data.playlists.items)
    //     }
    // }, [location, token]);

    // function to display the html information we want inside the html element
    const renderPlaylists = () => {
        return playlists.map(playlists => (
                <tr key={playlists.id}>
                    <td>{playlists.name}</td>
                    {/* <td>{playlists.id}</td> */}
                    <td>{playlists.images ? <img width={"25%"} src={playlists.images[0].url} alt="" /> : <div>No Image</div>}</td>
                    <td><a href={playlists.tracks.href}>link</a></td>
                </tr>
        ))
    }

    useEffect(() => {
        pullPlaylists()
    }, []);

    // JSX (passing the required credentials as a link to verify spotify account)
    // if no token display a tag Login to spotify: and :Please login text
    // if token display :logout and search bar:
    // function to set the search parameter
    // render playlists to display html at specified location
    return (
        <div className="App">
            <header className="App-header">
                <h1>Spotify Search Proof of Concept</h1>
                {!token ?
                    <a href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}`}>Login to Spotify</a>
                    : <button onClick={logout}>Logout</button>}
            </header>
            <body>
                <p>{location.state.result}</p>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Playlist Name</th>
                            <th>Image</th>
                            <th>Track Href</th>
                        </tr>
                    </thead>
                    <tbody>
                        {renderPlaylists()}
                    </tbody>
                </table>
            </body>
        </div>
    );
}

export default Spotify;
