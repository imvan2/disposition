import { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
// import { useAuthContext } from "../authorization/useToken";

const Vibecheck = () => {
  //setting state for the questions
  const [firstQ, setFirstQ] = useState("");
  const [secondQ, setSecondQ] = useState("");
  const [thirdQ, setThirdQ] = useState("");
  const [fourthQ, setFourthQ] = useState("");
  const [fifthQ, setfifthQ] = useState("");
  const [sixthQ, setGenre] = useState("");
  const options = ["Choose..", "Crocs", "Sneakers", "Sandals", "Slippers"];
  const [selected, setSelected] = useState(options[0]);
  // const [submitted, setSubmitted] = useState(false);

  const navigate = useNavigate();

  // getting the userID
  const [userID, setUserID] = useState(0);
  const location = useLocation();

  // const { token } = useAuthContext();

  // function SubmitButton() {
  //   if (firstQ && secondQ && thirdQ && fourthQ && fifthQ && sixthQ) {
  //     return <button type="button">Button</button>;
  //   } else {
  //     return (
  //       <button type="button" disabled>
  //         Button
  //       </button>
  //     );
  //   }
  // }

  // handling when the submit button is clicked
  const handleSubmit = async (event) => {
    event.preventDefault();

    const total = Math.floor(
      (firstQ + secondQ + thirdQ + fourthQ + fifthQ) / 5
    );
    const genreStr = sixthQ;
    let disposition = "";
    if (total === 1) {
      disposition = "gloomy";
    } else if (total === 2) {
      disposition = "mellow";
    } else if (total === 3) {
      disposition = "upbeat";
    } else if (total === 4) {
      disposition = "energetic";
    }
    const mood = disposition + " " + genreStr;
    // setSubmitted(true);

    try {
      const username = location.state.username;

      // GET request for username
      const accountUrl = `${process.env.REACT_APP_ACCOUNTS_API_HOST}/accounts/${username}`;
      const fetchConfig = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      };
      const accountResponse = await fetch(accountUrl, fetchConfig);
      if (accountResponse.ok) {
        const user = await accountResponse.json();
        if (user === null) {
          setUserID(0);
        } else {
          setUserID(user.id);
        }
      }
    } catch {
      setUserID(0);
    }

    // making a post request to save the answers to backend
    const data = { user_id: userID, mood: disposition, genre: genreStr };
    const answersUrl = `${process.env.REACT_APP_QUIZ_API_HOST}/answers`;
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(answersUrl, fetchConfig);

    if (response.ok) {
      const newData = await response.json();
      console.log(newData);
    }
    // END
    // if user authenticated
    // navigate to results page

    // if user NOT authenticated
    // navigate to login/signup
    navigate("/disposition/Results", { state: { result: mood } });

    // save genre+outcome
    // const data = {}
    // data.total =data.firstQ+ data.secondQ+ data.thirdQ+ data.fourthQ + data.fifthQ+ data.sixthQ
    // delete data.
  };

  //first question answer
  const water = () => {
    setFirstQ(1);
  };
  const coffee = () => {
    setFirstQ(2);
  };
  const tea = () => {
    setFirstQ(3);
  };
  const alcohol = () => {
    setFirstQ(4);
  };

  // second question answers
  const shrek = () => {
    setSecondQ(4);
  };
  const clueless = () => {
    setSecondQ(2);
  };
  const mean = () => {
    setSecondQ(3);
  };
  const notebook = () => {
    setSecondQ(1);
  };

  // third question answers
  const neat = () => {
    setThirdQ(2);
  };
  const home = () => {
    setThirdQ(1);
  };
  const gym = () => {
    setThirdQ(3);
  };
  const night = () => {
    setThirdQ(4);
  };

  // fourth question answers
  const q4 = (e) => {
    if (e.target.value === "Crocs") {
      setFourthQ(4);
      setSelected(e.target.value);
    } else if (e.target.value === "Sneakers") {
      setFourthQ(2);
      setSelected(e.target.value);
    } else if (e.target.value === "Sandals") {
      setFourthQ(3);
      setSelected(e.target.value);
    } else if (e.target.value === "Slippers") {
      setFourthQ(1);
      setSelected(e.target.value);
    }
  };

  // fifth question answers
  function spring() {
    setfifthQ(1);
  }
  const summer = () => {
    setfifthQ(2);
  };
  const fall = () => {
    setfifthQ(3);
  };
  const winter = () => {
    setfifthQ(4);
  };

  // sixth question answers
  // const genre = async (e) => {
  //   e.preventDefault()
  //   setGenre(e.target.value)
  // }

  const dontClickBtn = (e) => {
    e.target.style.position = `absolute`;
    e.target.style.left = `${window.Math.ceil(Math.random() * 90)}%`;
  };

  return (
    <>
      <br></br>
      <br></br>
      <div className="jumbotron jumbotron-fluid p-3 mb-2 bg-dark text-white">
        <div className="container"></div>
        <h1 className="display-4">Vibe Check</h1>
        <p className="lead">
          Using advanced AI technology, a personalized playlist will be
          delivered from the ether, straight to your tympanic membrane
        </p>
      </div>
      {/* </div> */}
      <br></br>
      <hr />
      <form onSubmit={handleSubmit}>
        <div className="shadow-lg p-3 mb-5 bg-white rounded">
          <label htmlFor="validationServer01" className="form-labels">
            What's your favorite beverage?
          </label>

          <div className="form-check form-check-inline ms-2" onClick={water}>
            <input
              className="form-check-input"
              type="radio"
              name="inlineRadioOptions"
              id="1"
              value="water"
              required
            />
            <label className="form-check-label" htmlFor="inlineRadio1">
              Water💦
            </label>
          </div>
          <div className="form-check form-check-inline" onClick={coffee}>
            <input
              className="form-check-input"
              type="radio"
              name="inlineRadioOptions"
              id="1"
              value="coffee"
            />
            <label className="form-check-label" htmlFor="inlineRadio2">
              Cofee☕️
            </label>
          </div>
          <div className="form-check form-check-inline">
            <input
              className="form-check-input"
              type="radio"
              onClick={tea}
              name="inlineRadioOptions"
              id="1"
              value="tea"
            />
            <label className="form-check-label" htmlFor="inlineRadio3">
              Tea🍵
            </label>
          </div>
          <div className="form-check form-check-inline">
            <input
              className="form-check-input"
              type="radio"
              onClick={alcohol}
              name="inlineRadioOptions"
              id="1"
              value="alcohol"
            />
            <label className="form-check-label" htmlFor="inlineRadio4">
              Alcohol🍺
            </label>
          </div>
        </div>

        {/* second form */}
        <div className="form-group shadow-lg p-3 mb-5 bg-white rounded">
          <label htmlFor="exampleFormControlSelect2" className="mb-3">
            What's your favorite movie
          </label>
          <select
            multiple
            className="form-control"
            id="exampleFormControlSelect2"
          >
            <option onClick={shrek}>Shrek</option>
            <option onClick={clueless}>Clueless</option>
            <option onClick={mean}>Mean Girls</option>
            <option onClick={notebook}>Notebook</option>
          </select>
        </div>

        {/* third form */}
        <div
          className="btn-group shadow p-3 mb-5 bg-white rounded"
          role="group"
        >
          <label>Which best describes you?</label>
          <br />
          <button
            type="button"
            onClick={neat}
            className="btn btn-outline-primary ms-5"
          >
            Neat Freak 🧹
          </button>
          <button
            type="button"
            onClick={home}
            className="btn btn-outline-primary ms-5"
          >
            Home Body 🏡
          </button>
          <button
            type="button"
            onClick={gym}
            className="btn btn-outline-primary ms-5"
          >
            Gym Life 💪🏽
          </button>
          <button
            type="button"
            onClick={night}
            className="btn btn-outline-primary ms-5"
          >
            Night Owl 🦉
          </button>
        </div>
        <br />

        {/* fourth form */}
        <div className="shadow p-3 mb-5 bg-white rounded">
          <label className="my-1 mr-2" htmlFor="inlineFormCustomSelectPref">
            Favorite type of footwear{" "}
          </label>
          <select
            value={selected}
            onChange={q4}
            className="custom-select my-1 mr-sm-2 ms-3"
            id="inlineFormCustomSelectPref"
          >
            {options.map((value) => (
              <option value={value} key={value}>
                {value}
              </option>
            ))}
          </select>
        </div>
        <br />

        {/* fifth form */}
        <div className="shadow-lg p-3 mb-5 bg-white rounded">
          <label className="form-label">What's your favorite season?</label>
          <div className="form-check form-check-inline ms-4" onClick={spring}>
            <input
              className="form-check-input"
              type="radio"
              name="check"
              id="5"
              value="option1"
            />
            <label className="form-check-label" htmlFor="inlineRadio5">
              Spring 🌻
            </label>
          </div>
          <div className="form-check form-check-inline" onClick={summer}>
            <input
              className="form-check-input"
              type="radio"
              name="check"
              id="5"
              value="Summer"
            />
            <label className="form-check-label" htmlFor="inlineRadio6">
              Summer ☀️
            </label>
          </div>
          <div className="form-check form-check-inline">
            <input
              className="form-check-input"
              type="radio"
              onClick={fall}
              name="check"
              id="5"
              value="Fall"
            />
            <label className="form-check-label" htmlFor="inlineRadio7">
              Fall 🍂
            </label>
          </div>
          <div className="form-check form-check-inline">
            <input
              className="form-check-input"
              type="radio"
              onClick={winter}
              name="check"
              id="5"
              value="Winter"
            />
            <label className="form-check-label" htmlFor="inlineRadio8">
              Winter 🧊
            </label>
          </div>
        </div>
        <br />

        {/* sixth form */}
        <div className="form-group shadow-lg p-3 mb-5 bg-white rounded">
          <label htmlFor="exampleFormControlTextarea1">Specify a genre</label>
          <textarea
            className="form-control"
            onChange={(e) => setGenre(e.target.value)}
            id="exampleFormControlTextarea1"
            rows="3"
          ></textarea>
        </div>
        <hr />
        {/* seventh form */}
        <label className="form-label">Done?</label>
        <br />
        <button type="button" className="btn btn-dark" onClick={handleSubmit}>
          NOT YET!!!!
        </button>
        <button
          type="button"
          className="btn btn-dark ms-3"
          onClick={() => alert("Congrats, this does nothing")}
          onMouseOver={dontClickBtn}
        >
          SUBMIT
        </button>
        <br />
        <br />
        <hr />
      </form>
    </>
  );
};

export default Vibecheck;
