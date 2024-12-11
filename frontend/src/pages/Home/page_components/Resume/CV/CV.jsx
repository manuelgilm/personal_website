import './CV.css'
const educationList = [
    {
        degree: "Bachelor of Science in Computer Science",
        institution: "University of Technology",
        dateRange: "2016 - 2020"
    }
]
const experienceList = [
    {
        position: "ML & MLOps Engineer",
        company: "EPAM Systems",
        dateRange: "April 2022 - Present",
        tasksList: [
            "Designed and implemented scalable MLOps pipelines for deploying machine learning models.",
            "Automated workflows using Kubernetes and Docker, improving deployment efficiency by 40%.",
            "Collaborated with data scientists to ensure seamless integration of models into production systems."
        ]
    },
    {
        position: "Data Analyst",
        company: "Data Science Co.",
        dateRange: "July 2020 - March 2022",
        tasksList: [
            "Analyzed and visualized data to identify trends and patterns.",
            "Developed machine learning models to predict customer behavior.",
            "Generated reports and dashboards to communicate insights to stakeholders."
        ]
    }
]

function ExperienceItem(position, company, dateRange, tasksList) {
    return (
        <div className="experience-item">
            <h4>{position}</h4>
            <h5>{company}</h5>
            <span>{dateRange}</span>
            <p>
                {tasksList.map(task => <li>{task}</li>)}
            </p>

        </div>
    )
}

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

function ProfessionalExperience() {

    return (

        <div className="resume-content">
            <div className="resume-details">
                <h3>Professional Experience</h3>
                {experienceList.map(experience => ExperienceItem(experience.position, experience.company, experience.dateRange, experience.tasksList))}
            </div>
        </div>
    )

}

export default ProfessionalExperience;