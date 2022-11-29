import { useEffect, useState } from "react";
import './App.css';
import axios from "axios";

function Hot() {
    // From developer dashboard
    const CLIENT_ID = "5a2a9a022fc549efae7b97b447d43b5c"
    // must be set in the developer dashboard (source of Under Construction Warning)
    const REDIRECT_URI = "http://localhost:3000/Hot-100"
    // authorization endpoint
    const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
    //requirement
    const RESPONSE_TYPE = "token"

    // Set and maintain state
    const [token, setToken] = useState('')
    const [tracks, setTracks] = useState([])

    //used to get token from url
    useEffect(() => {
        const hash = window.location.hash
        let token = window.localStorage.getItem("token")
        // how to get token from url (when we have a hashtag and no token)
        if (!token && hash) {
            token = hash.substring(1).split("&").find(elem => elem.startsWith("access_token")).split("=")[1]

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

    // function to create search request to spotify
    const searchPlaylists = async (e) => {
        e.preventDefault()
        const { data } = await axios.get("https://api.spotify.com/v1/playlists/6UeSakyzhiEt4NB3UAd6NQ", {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
        console.log("DATA HERE", data);
        // set data.playlists.items to playlists state
        setTracks(data.tracks.items)
    }
    // function to display the html information we want inside the html element
    const renderTracks = () => {
        return tracks.map(tracks => (
            <div key={tracks.id}>
                {tracks.track.artists[0].name} -
                {tracks.track.name}
                {tracks.track.album.images.length ? <img width={"100%"} src={tracks.track.album.images[1].url} alt="" /> : <div>No Image</div>}
                <p> </p>
            </div>
        ))
    }

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

                {token ?
                    <button onClick={searchPlaylists}>Hot 100 Test</button>
                    : <h2>Please login</h2>
                }

                {renderTracks()}
            </header>
        </div >
    );
}

export default Hot;
