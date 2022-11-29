import { NavLink } from 'react-router-dom';


function Nav() {
  // something here to hide login/sign up links when the user is already logged in
  // something here to show history when a user is logged in

  return (
  <nav className="navbar navbar-dark bg-dark">
    <div className="container-fluid">
      <NavLink className="navbar-brand" to="/">Disposition</NavLink>
      <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="offcanvas offcanvas-end show text-bg-dark" data-bs-scroll="true" tabIndex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
        <div className="offcanvas-header text-bg-dark">
          <h5 className="offcanvas-title" id="offcanvasWithBothOptionsLabel">Menu</h5>
          <button type="button" className="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div className="offcanvas-body bg-success">

            <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                <li><NavLink className="nav-link ms-3" to="">Vibe Check</NavLink></li>
                <li><NavLink className="nav-link ms-3" to="">Login</NavLink></li>
                <li><NavLink className="nav-link ms-3" to="">Signup</NavLink></li>
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
