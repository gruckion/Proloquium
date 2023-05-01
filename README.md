# Proloquium

## What is it?

Proloquium is an Artificial General Intelligence (AGI) system that leverages the power of Large Language Models (LLMs), LangChain, and Pinecone. Proloquium is a conversational AI system that uses Pinecone and LangChain to provide a conversational experience for end users who known little to nothing about the software development lifecycle to build high quality software that follows best practices with a focus on design patterns, scalability, testability, maintainability, security, performance, high availability. The end result form Proloquium is a software development plan that is generated from the conversation with the end user. This is then turned into a working prototype that can be continuously improved upon by the end user through conversation with Proloquium.

## How to use it?

In Proloquium you are the executive sponsor or customer you will interact with the **Project Manager**, **Project Owner** and **Lead Engineer** to define the project scope, timeline, and budget. You will also be responsible for providing the resources needed to complete the project.

- **YOU Executive Sponsor**: Provides overall project vision, support, and financial resources.

## Proloquium Agents

Proloquium has multiple agents that are responsible for different tasks. The agents are:

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

## Running the Project

1. Clone the repository: `git clone git@github.com:gruckion/Proloquium.git`
2. Change to the project directory: `cd Proloquium`
3. (Recommended) Use Makefile for building and running the application:
   - Build and run the application: `make run`
4. Alternatively, use Docker Compose to build and run the application:
   - Build and run the application: `./scripts/run.sh`
5. To run the application locally with Pipenv, ensure Pipenv is installed and active:
   - Install dependencies: `pipenv install`
   - Activate virtual environment: `pipenv shell`
   - Run the main.py script: `python main.py`
