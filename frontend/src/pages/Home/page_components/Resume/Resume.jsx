import React, { useState } from "react";
import "./Resume.css";
import ProfessionalExperience from "./ProfessionalExperience/ProfessionalExperience";
import EducationHistory from "./EducationHistory/EducationHistory";
// import ResumePDF from "../../assets/Manuel Gil-English - Extended.pdf"; // Ensure correct path

// function Resume() {
//   return (
//     <section id="resume" className="resume-section">
//       <h2>Resume</h2>
//       <div className="resume-content">
//         <div className="resume-download">
//           <a href="src/assets/Manuel Gil-English - Extended.pdf" download className="download-button">
//             Download Resume
//           </a>
//         </div>
//         <div className="resume-details">
//           <h3>Professional Experience</h3>
//           <div className="experience-item">
//             <h4>ML & MLOps Engineer</h4>
//             <h5>EPAM Systems</h5>
//             <span>April 2022 - Present</span>
//             <p>
//               - Designed and implemented scalable MLOps pipelines for deploying machine learning models.
//               <br />
//               - Automated workflows using Kubernetes and Docker, improving deployment efficiency by 40%.
//               <br />
//               - Collaborated with data scientists to ensure seamless integration of models into production systems.
//             </p>
//           </div>
//           <h3>Education</h3>
//           <div className="education-item">
//             <h4>Bachelor of Science in Computer Science</h4>
//             <h5>University of Technology</h5>
//             <span>2016 - 2020</span>
//             <p>
//               - Specialized in Artificial Intelligence and Machine Learning.
//               <br />
//               - Graduated with Honors.
//             </p>
//           </div>
//         </div>
//       </div>
//     </section>
//   );
// }
// function Resume() {
//   return (
//     <section id="resume" className="resume-section">
//       <h2>Resume</h2>
//       <div className="resume-content">
//         <div className="resume-download">
//           <a href="src/assets/Manuel Gil-English - Extended.pdf" download className="download-button">
//             Download Resume
//           </a>
//         </div>
//         <div className="resume-details">
//             <ProfessionalExperience />
//             <EducationHistory />

//         </div>
//       </div>
//     </section>
//   );
// }

function Resume() {
  const [isCollapsed, setIsCollapsed] = useState(true);

  const toggleCollapse = () => {
    setIsCollapsed(!isCollapsed);
  };

  return (
    <section id="resume" className="resume-section">
      <h2>Resume</h2>
      <div className="resume-content">
        <div className="resume-download">
          <a href="../../assets/Manuel Gil-English - Extended.pdf" download className="download-button">
            Download Resume
          </a>
        </div>
        <button className="collapse-button" onClick={toggleCollapse}>
          {isCollapsed ? "Show Details" : "Hide Details"}
        </button>
        {!isCollapsed && (
          <div className="resume-details">
            <ProfessionalExperience />
            <EducationHistory />
          </div>
        )}
      </div>
    </section>
  );
}


export default Resume;