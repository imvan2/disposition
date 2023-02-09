// import { useEffect, useState } from "react";
import { useToken } from "./useToken";
import { useNavigate } from "react-router-dom";

function Logout() {
    const [, , logout] = useToken();

    const navigate = useNavigate();
    // const { token } = useAuthContext();


    const handleSubmit = async (e) => {
        e.preventDefault();
        sessionStorage.setItem("username", undefined);
        logout();
        navigate("/");
    }

    return (
        <>
            <h1>Are you sure you want to logout?</h1>
            <button onClick={handleSubmit}>Ok fine!</button>
        </>
    )
}

export default Logout;
