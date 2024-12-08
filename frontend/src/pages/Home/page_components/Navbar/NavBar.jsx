import React from "react";
import "./Navbar.css";


function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">Manuel Gil</div>
      <ul className="navbar-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#resume">Resume</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#articles">Blog</a></li>
        <li><a href="#certifications">Certificates</a></li>
      </ul>
    </nav>
  );
}
export default Navbar;