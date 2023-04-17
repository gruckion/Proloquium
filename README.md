# Proloquium
[![Unit Tests](https://img.shields.io/github/actions/workflow/status/gruckion/Proloquium/ci.yml?label=unit%20tests)](https://github.com/gruckion/Proloquium/actions/workflows/ci.yml)
[![Discord Follow](https://dcbadge.vercel.app/api/server/hkMUKh3puU?style=flat)](https://discord.gg/hkMUKh3puU)
[![GitHub Repo stars](https://img.shields.io/github/stars/gruckion/Proloquium?style=social)](https://github.com/gruckion/Proloquium/stargazers)


## What is it?

Proloquium is an Artificial General Intelligence (AGI) system that leverages the power of Large Language Models (LLMs), LangChain, and Pinecone.

Proloquium is a conversational AI system that uses Pinecone and LangChain to provide a conversational experience for end users to accomplish tasks that traditionally require an entire team each carrying out specialist roles. Proloquium uses a rolling episodic memory organiser for each agent to consolidate memories as embeddings in a hiearchical structure which is refined through reprocessing of previous tasks and is measured against both the previous and current identified objective and testing criteria.

Proloquium has 3 main abilities;
1. Autonomously creates software: follows the software development lifecycle with agile planning, code reviews, and retrospectives to allow the AI agents and end user to build applications at enterprise quality software that follows best practices with a focus on design patterns, scalability, testability, maintainability, security, performance, high availability.
2. Autonomously creates tools: identifies its limitations and tools it is lacking, then plans, builds and then uses the tools to meet objective at hand. Proloquium will continue to add tools to its self updating its own code base in the process.
3. Autonomously agent creation: identifies gaps in specialist knowledge required, produces agents with those skill sets which it can then utilitse to accomplish the task at hand.

The end result from Proloquium is a conversational AI that is capable of building tools and agents to accomplish tasks for the end user and for its own internal AI agents.

## Who am I?

In Proloquium you are the executive sponsor or client you will interact with the **Project Manager**, **Project Owner** and **Application Lead** to define the project scope, timeline, and budget. You will also be responsible for providing the resources needed to complete the project.

- **YOU Executive Sponsor**: Provides overall project vision, support, and financial resources.

## Proloquium Agents

Proloquium has multiple agents that are responsible for different tasks. As well as being able to autonomously identify and create new agents to delegate specialist tasks too;

### Product Development

- **Project Manager**: Oversees the project's progress, timeline, and resource allocation.
- **Product Owner**: Represents the customer and defines product features and priorities.
- **Software Architect**: Designs the software's high-level structure and ensures technical quality.
- **Backend Developer**: Focuses on server-side logic, data storage, and integration with other systems.
- **Frontend Developer**: Develops the user interface and ensures a smooth user experience.
- **Full-stack Developer**: Works on both frontend and backend development tasks.
- **Mobile Developer**: Specializes in developing applications for mobile platforms, such as iOS and Android.
- **Quality Assurance (QA) Engineer**: Tests the software for bugs, usability, and performance issues.
- **DevOps Engineer**: Streamlines development and deployment processes to improve efficiency and reliability.
- **UI/UX Designer**: Designs user interfaces and ensures a positive user experience.
- **Technical Writer**: Creates documentation and user guides for the software.
- **Data Scientist/Engineer**: Analyzes and processes data, creating insights and developing machine learning models.
- **Security Engineer**: Ensures the software and infrastructure are secure from vulnerabilities and attacks.
- **Business Analyst**: Analyzes business requirements and translates them into technical specifications.
- **Scrum Master/Agile Coach**: Facilitates Agile development processes and helps the team improve their practices.

### Executive Functions

- **CEO (Chief Executive Officer)**: Sets the company's vision, strategy, and overall direction.
- **CFO (Chief Financial Officer)**: Manages the company's financial resources and ensures fiscal health.
- **COO (Chief Operating Officer)**: Oversees day-to-day operations and ensures efficient processes.
- **CMO (Chief Marketing Officer)**: Leads marketing efforts and drives brand growth and awareness.
- **HR Manager (Human Resources Manager)**: Manages employee recruitment, retention, and development.
- **Sales Manager**: Leads the sales team and drives revenue growth.
- **Customer Support Representative**: Assists customers with inquiries and resolves issues.
- **Legal Counsel**: Provides legal advice and ensures compliance with laws and regulations.
- **Supply Chain Manager**: Manages procurement, logistics, and inventory to optimize operations.
- **IT Manager**: Oversees information technology infrastructure and support.

### Data Stratergy

- **Chief Data Officer (CDO)**: Sets the data strategy and ensures data quality and accessibility.
- **Data Analyst**: Examines data sets to identify trends and draw insights.
- **Data Engineer**: Builds and maintains data pipelines and infrastructure.
- **Data Architect**: Designs data models and structures to support analysis and processing.
- **Database Administrator**: Manages and optimizes database performance and security.
- **Data Visualization Specialist**: Creates visual representations of data to communicate insights.
- **Data Governance Manager**: Ensures data is managed according to policies and regulations.
- **Machine Learning Engineer**: Develops machine learning models and integrates them into applications.
- **AI Researcher**: Conducts research on artificial intelligence methods and technologies.
- **Big Data Specialist**: Works with large-scale data sets and develops strategies for processing and storage.


## Architecture

The Proloquium architecture is comprised of three main components:

1. **Pinecone** - A distributed, scalable, and high-performance vector index for embedding-based similarity search.
2. **LangChain** - A language model that is trained on a chain of text corpora.
3. **GPT** - A large language model that is trained on a large text corpus. Defaults to GPT 4 or 3.5

## Requirements

- Python 3.9+
- Docker 20.10+ (with Docker Compose 1.29+)
- Make (Optional)
- Pipenv 2021.5.29+
- OpenAI GPT-3 or GPT-4 API Key
- Pinecone API key
- Serp API key
- Wolfram Alpha API key

## Running the Project

1. Clone the repository: `git clone git@github.com:gruckion/Proloquium.git`
2. Change to the project directory: `cd Proloquium`
3. (Recommended) Use Makefile for building and running the application:
   - Build and run the application: `make run`
4. Alternatively, use Docker Compose to build and run the application:
   - Build and run the application: `./scripts/run.sh`
5. To run the application locally with Pipenv, ensure Pipenv is installed and active:
   - Install dependencies: `cd python; pipenv install --dev`
   - Activate virtual environment: `pipenv shell`
   - Run the main.py script: `python main.py`
