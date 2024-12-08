import React from "react";
import "./Projects.css";

function Projects() {
  return (
    <section id="projects" className="projects-section">
      <h2>My Projects</h2>
      <div className="project-list">
        {/* Add your projects here */}
        <div className="project-item">
          <h3>Project Title</h3>
          <p>Short description of the project.</p>
        </div>
        {/* Repeat for more projects */}
      </div>
    </section>
  );
}

export default Projects;