import React from "react";
import { useSelector } from "react-redux";
// import { User } from "../actions/index";

import logo from "../images/insta-logo.png";

const Navbar = () => {
  const user = useSelector((state: any) => state.user);

  return (
    <nav className="navbar navbar-expand-lg card">
      <div className="container">
        <a className="navbar-brand" href="./#/day-35">
          <img src={logo} alt="logo" />
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="search">
          <input
            type="text"
            className="form-control form-control-sm"
            placeholder="🔍 Search"
          />
        </div>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <a className="nav-link" href="./#/day-35">
                <i className="bi bi-house-fill"></i>{" "}
                <span className="sr-only">(current)</span>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="./#/day-35">
                <i className="bi bi-chat"></i>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="./#/day-35">
                <i className="bi bi-compass"></i>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="./#/day-35">
                <i className="bi bi-heart"></i>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="./#/day-35">
                <img src={user.profilePicture} alt="profilePicture" />
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
