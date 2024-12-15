
import "./EducationHistory.css";
const educationList = [
    {
        degree: "Bachelor of Electrical Engineering",
        institution: "University of the Andes (Venezuela)",
        dateRange: "2011 - 2019"
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