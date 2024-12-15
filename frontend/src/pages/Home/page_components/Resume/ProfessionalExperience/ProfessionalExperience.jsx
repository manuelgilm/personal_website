import "./ProfessionalExperience.css";

const experienceList = [
    {
        position: "ML & MLOps Engineer",
        company: "EPAM Systems",
        dateRange: "April 2022 - Present",
        tasksList: [
            "Designed an object-oriented ML project blueprint for the entire ML lifecycle, utilizing tools such as the Databricks Stack (Pyspark, feature store, mlflow), Poetry, and dbx.",
            "Developed Continuous Integration (CI) Pipelines in Azure Dev Ops and Continuous Delivery (CD) pipelines in Azure Data Factory. Tooling: Azure Dev Ops, Azure Data Factory.",
            "Developed a Monitoring System utilizing the New Relic platform. This system monitors the status of ML projects executed on Databricks, providing visibility into the jobs running on the platform.",
            "Built a Model Catalog for Databricks and Google Cloud Platform using IBM Factsheets, integrating Cloud Functions, Vertex AI, MLflow webhooks, and Databricks Jobs."
        ],
    },
    {
        position: "Data Scientist",
        company: "DCKStudios",
        dateRange: "July 2020 - March 2022",
        tasksList: [
            "Using data and process mining, we obtain graphic models for process flow, guiding future organizational decisions",
            "Developed AI applications enhancing user experience, incorporating speech-to-text, adult content detection, and brand and emotion recognition. Tooling: Azure Custom Vision, OpenCV, image classification, Object Detection, Image processing.",
            "Detecting water leaks in distribution networks using machine learning and hydraulic simulations. Tooling: Gym OpenAI, Reinforcement Learning"
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