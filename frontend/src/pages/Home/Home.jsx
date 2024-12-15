import React from "react";
import "./Home.css";
import Navbar from "./page_components/Navbar/NavBar";
import Header from "./page_components/Header/Header";
import About  from "./page_components/About/About";
import Projects from "./page_components/Projects/Projects";
import Contact from "./page_components/Contact/Contact";
import Resume from "./page_components/Resume/Resume";
function Home() {
  return (
    <>    
        <Navbar />
        <div className="home-container">
            {/* <Header /> */}
            <About />
            <Resume />
            <Contact />

        </div>
    </>
  )
};

export default Home;