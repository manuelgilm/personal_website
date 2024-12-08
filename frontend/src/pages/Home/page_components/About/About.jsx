import React from "react";
import "./About.css";

function About() {
  return (
    <section id="about" className="about-section">
      <h2>About Me</h2>
      <div className="about-container">
        <div className="about-image">
          <img src="src/assets/profile_image/perfil_photo.jpg" alt="Profile" />
        </div>
        <div className="about-text">
          <p>
          Hello! I'm Manuel Gil, an ML & MLOps engineer passionate about deploying machine learning models into production
          environments. I specialize in building scalable MLOps pipelines, automating workflows, and ensuring the reliability
          and efficiency of AI-driven applications. With expertise in Python, TensorFlow, Kubernetes, and cloud platforms like
          AWS and GCP, I strive to bridge the gap between data science and production systems.
          </p>
          <h3>Skills</h3>
          <div className="skills">
            <span>Python</span>
            <span>Machine Learning</span>
            <span>MLOps</span>
            <span>Kubernetes</span>
            <span>Docker</span>
            <span>Azure & Databricks</span>
            <span>TensorFlow & PyTorch</span>
            <span>CI/CD</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default About;