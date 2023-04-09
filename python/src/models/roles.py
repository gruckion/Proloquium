"""Defines the roles that can be assigned to a team member."""


from enum import Enum

role_descriptions = {
    "EXECUTIVE_SPONSOR": """
        The external stakeholder who owns the project vision,
        defines the product requirements and desired outcomes,
        and provides funding. Collaborates with the product owner
        and project manager to review and select proposed plans,
        budgets, and features. Provides strategic direction and
        oversees progress on a high level.
    """,
    "PRODUCT_OWNER": """
        Represents the customer and defines product features and priorities.
        Works closely with the executive sponsor, project manager, and development
        team to create a product backlog, clarify requirements, and prioritize features.
        Ensures that the product vision aligns with the sponsor's expectations and customer needs
        by running requirement gathering sessions and conducting user research.
    """,
    "PROJECT_MANAGER": """
        Oversees the project's progress, timeline, and resource allocation.
        Coordinates with the executive sponsor, product owner, and team leads
        to ensure timely delivery and effective communication.
        Responsible for project planning, risk management, and progress reporting.
    """,
    "LEAD_ENGINEER": """
        Manages and leads the technical team, providing technical guidance and mentorship.
        Collaborates with the software architect, product owner, and project manager to
        ensure alignment between technical implementation and product requirements.
        Oversees the work of other engineers and assists in code reviews, architectural decisions, and problem-solving.
    """,
    "SOFTWARE_ARCHITECT": """
        Designs the software's high-level structure and ensures technical quality.
        Collaborates with the lead engineer and other technical team members to create
        and maintain the architectural vision. Evaluates and selects appropriate
        technologies, tools, and frameworks. Provides guidance on coding standards
        and best practices.
    """,
    "BACKEND_DEVELOPER": """
        Focuses on server-side logic, data storage, and integration with other systems.
        Works closely with the lead engineer, software architect, and other developers
        to implement and maintain the backend infrastructure. Develops APIs, data models,
        and server-side processes to support the frontend and ensure smooth integration.
    """,
    "FRONTEND_DEVELOPER": """
        Develops the user interface and ensures a smooth user experience.
        Collaborates with the lead engineer, UX/UI designer, and other developers
        to create and maintain the frontend application. Implements designs, optimizes
        performance, and ensures accessibility and responsiveness across devices.
    """,
    "FULL_STACK_DEVELOPER": """
        Works on both frontend and backend development tasks.
        Collaborates with the lead engineer, software architect, and other developers
        to ensure seamless integration between frontend and backend components.
        Contributes to the implementation and maintenance of both user interfaces
        and server-side infrastructure.
    """,
    "MOBILE_DEVELOPER": """
        Specializes in developing applications for mobile platforms, such as iOS and Android.
        Works closely with the lead engineer, UX/UI designer, and other developers to create
        and maintain mobile applications. Ensures optimal performance, accessibility, and user
        experience on various devices and operating systems.
    """,
    "QA_ENGINEER": """
        Tests the software for bugs, usability, and performance issues.
        Collaborates with the lead engineer, product owner, and other team members to create
        and execute test plans and test cases. Identifies and reports defects, verifies fixes,
        and ensures the quality of the product before release.
    """,
    "CLOUD_ENGINEER": """
        Designs, manages, and maintains cloud-based infrastructure and services using infrastructure as code.
        Collaborates with the lead engineer, software architect, and DevOps engineer to ensure scalability,
        security, and reliability of the cloud infrastructure. Implements monitoring, logging, and
        disaster recovery strategies.
    """,
    "DEVOPS_ENGINEER": """
        Streamlines development and deployment processes to improve efficiency and reliability.
        Works closely with the lead engineer, software architect, and cloud engineer to automate
        build, test, and deployment pipelines. Ensures continuous integration and delivery,
        monitors application performance, and maintains infrastructure.
    """,
    "UI_UX_DESIGNER": """
        Designs user interfaces and ensures a positive user experience.
        Collaborates with the product owner, frontend developer, and other team members to
        create wireframes, mockups, and prototypes. Conducts user research, usability testing,
        and iteratively refines designs based on feedback and requirements.
    """,
    "TECHNICAL_WRITER": """
        Creates documentation and user guides for the software.
        Works closely with the product owner, lead engineer, and other team members to
        understand the product's features, use cases, and technical details.
        Ensures clear and concise documentation for both end users and developers.
    """,
    "DATA_SCIENTIST_ENGINEER": """
        Analyzes and processes data, creating insights and developing machine learning models.
        Collaborates with the lead engineer, software architect, and other team members to
        integrate data analysis and machine learning components into the product.
        Ensures data quality, maintains data pipelines, and optimizes model performance.
    """,
    "BUSINESS_ANALYST": """
        Analyzes business requirements and translates them into technical specifications.
        Collaborates with the product owner, project manager, and development team to
        ensure alignment between business needs and product features. Facilitates
        communication and helps to resolve requirements-related issues.
    """,
    "SCRUM_MASTER_AGILE_COACH": """
        Facilitates Agile development processes and helps the team improve their practices.
        Works closely with the project manager, product owner, and development team to
        ensure effective communication, remove impediments, and foster a positive working environment.
        Supports the team in continuous improvement and promotes Agile principles and values.
    """,
}


class Role(Enum):
    """Defines the roles that can be assigned to a team member."""

    EXECUTIVE_SPONSOR = "EXECUTIVE_SPONSOR"
    PRODUCT_OWNER = "PRODUCT_OWNER"
    PROJECT_MANAGER = "PROJECT_MANAGER"
    LEAD_ENGINEER = "LEAD_ENGINEER"
    SOFTWARE_ARCHITECT = "SOFTWARE_ARCHITECT"
    BACKEND_DEVELOPER = "BACKEND_DEVELOPER"
    FRONTEND_DEVELOPER = "FRONTEND_DEVELOPER"
    FULL_STACK_DEVELOPER = "FULL_STACK_DEVELOPER"
    MOBILE_DEVELOPER = "MOBILE_DEVELOPER"
    QA_ENGINEER = "QA_ENGINEER"
    CLOUD_ENGINEER = "CLOUD_ENGINEER"
    DEVOPS_ENGINEER = "DEVOPS_ENGINEER"
    UI_UX_DESIGNER = "UI_UX_DESIGNER"
    TECHNICAL_WRITER = "TECHNICAL_WRITER"
    DATA_SCIENTIST_ENGINEER = "DATA_SCIENTIST_ENGINEER"
    SECURITY_ENGINEER = "SECURITY_ENGINEER"
    BUSINESS_ANALYST = "BUSINESS_ANALYST"
    SCRUM_MASTER_AGILE_COACH = "SCRUM_MASTER_AGILE_COACH"
