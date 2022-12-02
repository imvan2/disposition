import { NavLink } from 'react-router-dom';
// import Logo_Light from './Images/Logo_Light.png';
// <img src={Logo_Light} width={100} height={100} />

function Nav() {
  // something here to hide login/sign up links when the user is already logged in
  // something here to show history when a user is logged in

  return (
    <nav className="navbar navbar-dark bg-dark">
        <div className="container-fluid">
          <NavLink className="navbar-brand" to="/"><img height="25%" alt="Disposition logo" src='/images/Logo.png' /></NavLink>
          <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="offcanvas offcanvas-end text-bg-dark" data-bs-scroll="true" tabIndex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
            <div className="offcanvas-header bg-secondary text-white">
              <h5 className="offcanvas-title" id="offcanvasWithBothOptionsLabel">Menu</h5>
              <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div className="offcanvas-body bg-success p-3 mb-2 bg-dark text-white">
                <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                    <li><NavLink className="nav-link ms-3" to="/Vibecheck">Vibe Check</NavLink></li>
                    <li><NavLink className="nav-link ms-3" to="/Login">Login</NavLink></li>
                    <li><NavLink className="nav-link ms-3" to="/SignupForm">Sign-up</NavLink></li>
                    <li><NavLink className="nav-link ms-3" to="/Results">Results</NavLink></li>
                    <li><NavLink className="nav-link ms-3" to="">History</NavLink></li>
                    <li><NavLink className="nav-link ms-3" to="/Hot-100">Hot-100</NavLink></li>
                </ul>
            </div>
          </div>
        </div>
      </nav>
  );
}

export default Nav;