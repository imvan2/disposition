// import { useEffect, useState } from "react";

// const options = {
//   method: "GET",
//   headers: {
//     "X-RapidAPI-Key": "b9d153f428msh4788285d2521effp1d5967jsnec5996c9668e",
//     "X-RapidAPI-Host": "billboard-api2.p.rapidapi.com",
//   },
// };

//   export const Billboard = () =>{
//   const [data, setData] = useState([]);

//   useEffect(() => {
//     console.log("useEffect ran");

//     function gettingBillboard() {
//       const data = fetch(
//         "https://billboard-api2.p.rapidapi.com/hot-100?range=1-10&date=2022-11-26",
//         options
//       )
//         .then((response) => response.json())
//         .then((response) => console.log(response))
//         .catch((err) => console.error(err));
//     }
//     setData(data);

//     gettingBillboard();
//   }, []);
// return data;
// }
