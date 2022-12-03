import { useEffect, useState } from "react";
import 'animate.css';
import './ResultsAnimation.css';

const ResultsPage = () => {
    const [good, setGood] = useState("");
    const [bad, setBad] = useState("");

    const handleClick = () => {
        setGood("good");
    }
    return (
        <>
            <h1 className="animate__zoomInDown mt-5 h-100 d-flex align-items-center justify-content-center" id="text">Your Customized Playlist</h1>
            <div className="animate__fadeIn mt-3 center">
                <div className="card mb-3" style={{"width": "900px"}} id="div1">
                    <div className="row g-0">
                        <div className="col-md-4">
                            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQKQNG9rNHG57S_SmXKdDVgk5ID7hALpB9fA&usqp=CAU" className="img-fluid rounded-start" alt="..." />
                        </div>
                        <div className="col-md-8">
                            <div className="card-body">
                                <h5 className="card-title">Playlist</h5>
                                <p className="card-text">Playlist description?</p>
                            </div>
                        </div>
                    </div>
                    <ul className="list-group list-group-flush">
                        <li className="list-group-item">Song 1</li>
                        <li className="list-group-item">Song 2</li>
                        <li className="list-group-item">Song 3</li>
                        <li className="list-group-item">Song 4</li>
                        <li className="list-group-item">Song 5</li>
                    </ul>
                </div>
                <br />
                <br />
                <br />
                <div className="card mb-3 mt-3 center" style={{"width": "900px", "textAlign":"center"}} id="div2">
                    <h2>How'd you like the playlist?</h2>
                    <button className="button"><iconify-icon icon="mdi:thumb-up-outline" width="100" onClick={handleClick}></iconify-icon></button>
                    <button className="button"><iconify-icon icon="mdi:thumb-up-outline" width="100" rotate="180deg" onClick={handleClick}></iconify-icon></button>
                </div>
            </div>
        </>
    )
}

export default ResultsPage;
