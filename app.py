from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Sandeep Chandrakant Chavan",
    "first_name": "Sandeep",
    "title": "Data Analyst & SCADA Systems Specialist",
    "tagline": "Turning raw operational data into real-time insights, automation, and executive-ready dashboards.",
    "location": "Mumbai, India",
    "phone": "+91 91367 85013",
    "phone_raw": "+919136785013",
    "email": "sandeepc1207@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sandeep-chavan-163a03270",
    "linkedin_handle": "linkedin.com/in/sandeep-chavan-163a03270",
    "scada_project": "https://www.scadadr.windworldindia.com",
    "scada_demo": "https://drive.google.com/file/d/1kYk3X9sGFo03ukoLQpaxgCgqniTt-9pb/view?usp=drive_link",
    "resume_download": "static/files/Sandeep_Chavan_Resume.pdf",
    "photo": "images/sandeepchavan.jpg",
    "summary_1": (
        "Data Analyst and SCADA Systems Specialist with 9+ years of experience in data analytics, "
        "ETL pipeline development, SCADA data management, automation, and MIS reporting. Skilled in "
        "Python, SQL, Power BI, VBA, MySQL, and data visualization to deliver real-time insights and "
        "improve operational efficiency."
    ),
    "summary_2": (
        "Experienced in developing automated reporting systems, real-time dashboards, anomaly detection "
        "models, and SCADA data pipelines for wind turbine monitoring. Proficient with modern AI-assisted "
        "development tools including GitHub Copilot, Blackbox AI, Antigravity, Trae AI, Claude, and local "
        "LLM deployment using Ollama models to accelerate coding, automation, and data analysis workflows."
    ),
    "stats": [
        {"value": 9, "suffix": "+", "label": "Years of Experience"},
        {"value": 4, "suffix": "", "label": "Organizations Served"},
        {"value": 4, "suffix": "", "label": "Professional Certifications"},
        {"value": 30, "suffix": "+", "label": "Tools & Technologies"},
    ],
    "services": [
        {
            "icon": "chart",
            "title": "Data Analytics & MIS Reporting",
            "description": "End-to-end analytics, KPI tracking, and automated MIS reports that turn raw business data into clear executive insight.",
        },
        {
            "icon": "database",
            "title": "SCADA Data Engineering",
            "description": "ETL pipelines and automated SCADA data ingestion for wind turbine monitoring — reliable, real-time, and scalable.",
        },
        {
            "icon": "gauge",
            "title": "Dashboards & Visualization",
            "description": "Real-time operational dashboards in Power BI and Tableau that give leadership instant visibility into performance.",
        },
        {
            "icon": "bolt",
            "title": "Process Automation",
            "description": "Python, VBA, and batch-script automation that eliminates repetitive work — from reporting to FTP data transfers.",
        },
        {
            "icon": "spark",
            "title": "AI-Assisted Development",
            "description": "Modern AI tools (Copilot, Claude, local LLMs) applied to accelerate coding, automation, and data workflows.",
        },
        {
            "icon": "server",
            "title": "Database Management",
            "description": "Hands-on experience across MySQL, MSSQL, and Teradata — querying, processing, and validating large datasets.",
        },
    ],
    "skills": [
        {
            "category": "Programming & Analytics",
            "icon": "code",
            "tech": ["Python", "SQL", "VBA", "Excel (Advanced)", "Power BI", "Tableau"],
        },
        {
            "category": "Data Engineering",
            "icon": "database",
            "tech": [
                "ETL Pipeline Development",
                "Data Processing",
                "Data Cleaning",
                "Automation Scripts",
                "FTP & Batch Automation",
            ],
        },
        {
            "category": "Databases",
            "icon": "server",
            "tech": ["MySQL", "MSSQL", "Teradata", "Hadoop"],
        },
        {
            "category": "Tools & Development",
            "icon": "tool",
            "tech": ["VS Code", "Jupyter Notebook", "PyCharm", "SharePoint"],
        },
        {
            "category": "AI & Developer Productivity",
            "icon": "spark",
            "tech": [
                "GitHub Copilot",
                "Blackbox AI",
                "Antigravity AI",
                "Trae AI",
                "Claude",
                "Ollama (Local LLM)",
            ],
        },
    ],
    "experience": [
        {
            "company": "Wind World India Ltd.",
            "role": "Senior Engineer – SCADA Department",
            "location": "Mumbai, India",
            "period": "Nov 2024 – Present",
            "current": True,
            "tag": "SCADA & Data Engineering",
            "points": [
                "Designed and maintained ETL pipelines using Python to process large volumes of SCADA turbine data.",
                "Developed real-time operational dashboards using Power BI and VBA for monitoring turbine performance.",
                "Automated SCADA data ingestion into MySQL databases, improving reporting efficiency and reducing manual work.",
                "Performed anomaly detection and trend analysis on turbine operational data.",
                "Implemented data transfer automation using FTP and batch scripting for remote server synchronization.",
                "Built executive dashboards for leadership to monitor generation performance across wind farms.",
            ],
        },
        {
            "company": "Yes Bank Ltd.",
            "role": "Assistant Manager – Internal Audit",
            "location": "Mumbai, India",
            "period": "Nov 2021 – Nov 2024",
            "current": False,
            "tag": "Audit Analytics",
            "award": "Trailblazer Award (2024) – for innovation in automation and audit analytics.",
            "points": [
                "Developed exception and risk analytics reports using Hadoop and SQL.",
                "Built Tableau dashboards for audit analytics and compliance monitoring.",
                "Automated internal audit workflows using Excel VBA, reducing manual processing time.",
                "Conducted User Acceptance Testing (UAT) for internal reporting tools.",
                "Performed Loan Review Mechanism (LRM) analysis and data validation.",
            ],
        },
        {
            "company": "Datamatics Global Services Ltd.",
            "role": "Executive – Actuarial Department",
            "location": "Mumbai, India",
            "period": "Mar 2018 – Oct 2021",
            "current": False,
            "tag": "Client: ICICI Prudential Life Insurance",
            "points": [
                "Processed actuarial data using DCS and Prophet Studio.",
                "Developed actuarial reports and queries using Teradata SQL.",
                "Supported data validation, testing, and internal system UAT.",
            ],
        },
        {
            "company": "Concept Enterprises",
            "role": "Executive – Client Support",
            "location": "",
            "period": "Oct 2015 – Feb 2018",
            "current": False,
            "tag": "Client Servicing",
            "points": [
                "Coordinated with clients regarding service requests, quotations, and billing processes.",
                "Assisted in preparing quotations and ensuring timely follow-up with clients.",
                "Supported day-to-day client servicing and handled queries related to orders and services.",
                "Maintained proper documentation for client transactions and internal processes.",
            ],
        },
    ],
    "education": [
        {
            "degree": "Bachelor of Commerce (B.Com)",
            "institution": "Mumbai University",
            "year": "2013",
            "score": "72%",
        },
        {
            "degree": "HSC",
            "institution": "Sheth Anandilal Podar Junior College",
            "year": "2010",
            "score": "65%",
        },
        {
            "degree": "SSC",
            "institution": "St. Joseph High School",
            "year": "2008",
            "score": "68%",
        },
    ],
    "certifications": [
        {"title": "Microsoft SQL Certification", "vendor": "Microsoft", "icon": "shield"},
        {"title": "Advanced Certification in Microsoft Excel", "vendor": "Microsoft", "icon": "grid"},
        {"title": "Python for Data Science", "vendor": "Data Science", "icon": "python"},
        {"title": "Microsoft Power BI Certification", "vendor": "Microsoft", "icon": "chart"},
    ],
    "projects": [
        {
            "title": "SCADA Data Platform — Wind Turbine Monitoring",
            "description": (
                "A live SCADA data reporting platform for wind turbine performance monitoring — "
                "real-time dashboards, automated data pipelines, and generation analytics for leadership."
            ),
            "tags": ["Python", "MySQL", "Power BI", "ETL", "SCADA"],
            "link": "https://www.scadadr.windworldindia.com",
            "link_text": "Visit Live Platform",
            "external": True,
        },
        {
            "title": "SCADA Platform — Demo Walkthrough",
            "description": (
                "Video walkthrough of the SCADA reporting platform, demonstrating real-time turbine "
                "dashboards, anomaly detection, and ETL-driven reporting in action."
            ),
            "tags": ["Demo", "Dashboards", "Analytics"],
            "link": "https://drive.google.com/file/d/1kYk3X9sGFo03ukoLQpaxgCgqniTt-9pb/view?usp=drive_link",
            "link_text": "Watch Demo",
            "external": True,
        },
    ],
    "personal": {
        "dob": "01 December 1991",
        "marital": "Married",
    },
}


@app.route("/")
def home():
    return render_template("index.html", p=PROFILE)


if __name__ == "__main__":
    app.run(debug=True)
