
import "./EducationHistory.css";
const educationList = [
    {
        degree: "Bachelor of Science in Computer Science",
        institution: "University of Technology",
        dateRange: "2016 - 2020"
    }
]
function EducationItem(degree, institution, dateRange) {
    return (
        <div className="education-item">
            <h4>{degree}</h4>
            <h5>{institution}</h5>
            <span>{dateRange}</span>
        </div>
    )
}

function EducationHistory() {
    return (
        <div className="resume-content">
            <div className="resume-details">
                <h3>Education</h3>
                {educationList.map(education => EducationItem(education.degree, education.institution, education.dateRange))}
            </div>
        </div>
    )
}

export default EducationHistory;