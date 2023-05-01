# List of tasks to complete

## TODO

- [ ] LanChain has an [OutputParser](https://docs.langchain.com/docs/components/chains/llm-chain)
- [ ] Use [LangChain indexes](https://docs.langchain.com/docs/components/chains/index_related_chains) for the projects code / meta data
  - [ ] StuffDocumentsChain
  - [ ] MapReduceDocumentsChain
  - [ ] Refine
  - [ ] Map-Rerank

## Research

- [x] Create a new project in Pinecone
- [ ] Look at how LangChain works
- [ ] Incorporate AutoGPT's approach to LangChain into Proloquium
- [ ] Look at how MemoryGPT works and how it can be used in Proloquium
- [ ] Look at AutoGPT's update to allow it to write its own code and run scripts allows it to recursively develop
- [ ] RobotGPT has voice
- [ ] This product looks like a finished product https://www.imagica.ai/ but is waiting list
- [ ] Find a way to find and crawl documentation needed to write code
- [ ] Maybe a pseudo code to code converter which is more compact for GPT to work with
- [ ] Maybe obfuscate the code and provide that compressed code too and do lookups via indexes
- [ ] Produce a vector map of the code base and how it relates to each other and external libraries

## Application

- [ ] Write and run scripts
- [ ] Access all code in the project
- [ ] See folder structure
- [ ] Use Language Server Protocol (LSP) to provide an outline of the code
- [ ] Identify what other information these LSPs can provide to help GPT

"""
This module will allow the user to specify a project folder to work on.
It then identifies the programming languages being used in the project
and stores them in the proloqium cache.

The
"""


Roles:
 types

Meetings:
 names:

Client > objective

## Main Goal

1. objective
2. Build a cold
3. needs multiple files
4. might need to integrate with external frameworks
5. test cases to make sure it works and continues to work
6. documentation

## Step back what's hello world? Proof of concept.

1. Interact with GPT and get it to write quality code
2. Have it save the code for me
3. Get it to generate tests to ensure it works
4. Have it run the code check it works
5. Feed in errors and fix them and itterate

## Avoid doing stuff ChatGPT can already do

### Step 1

- Capture requirements from user, build high level plan
- Evaluate plan and decide on technology solutions
- Then break down the plan into actionable parts
- Write business test 'features' for the stories
- Then generate the 'fixtures' for the features
- Then write the code with multiple files to meet the requirements and save to disc
- Write unit tests for each function and save to disc
- Add docstrings to everything including module file
- Run the tests and fix any errors
- Run the program and fix any errors
- Repeat until it works

1. Individual function and unit test writer <???> requirments come from an outter layer

- Write a function that achieve the objective
- Self reflect on the requirements and code to improve the function code (decelartive, immutable, pythonic)
- Write a unit test for the function with full code coverage
- Self reflect on the requirements, code and test to improve the function code

- Save function
- Save test
- Lint the code
- Run code check it compiles
- Run test check it passes
- Repeat

1. What code is needed to make the task?

2. User story -> individual tasks?

```
You are the lead developer of a software development team. You are breaking down user stories into individual tasks.

```
Customer can process a input csv and generate an output csv with an additional column called campaign_name which they input via the CLI and it validates email addresses
```

Above is a user story, provide names and descriptions for each task to achieve the above user story. Language is python.

Declarative, Immutable, pythonic, design patterns, solid, and ensure 100% unit test coverage.
```

- Create a CSV parser, reads in and outputs csv
- Update the CSV to append the campaign_name from the cli input
- Verify all email addresses are valid throw error if not


### Step 2

- Have it work with existing projects
- Have it work with multiple languages


Build in an improvement mechanism, which looks at the prompt and the output and the corrected output
and then returns an improved prompt, using GPT.

Need a way of having GPT summarise the tech stack, so it can consider the tech stack summary when writing code
for existing projects.


# User flow

1. Start the program
2. Collect the persons information
   - Name
   - Job role
   - Email address
   - Phone number
   - Github username
   - Company name
3. Gather requirements discovery call
4. System generates agents to accomplish the task
5. Can ask for status update from  any of the agents
6. System agents communicate to each other to define the project scope, requirements and resolve any ambiguities
7. Agents communicate with the user to resolve any ambiguities and refine the requirements
8. User agrees to the project scope and requirements
9. Business analyst agent generate a project plan and present it to the user
10. User agrees to the project plan is then refined into epics, features and user stories
11. User agrees to the to the detailed project plan
12. Technical architect agent generates a technical design document
13. Lead developer agent generates a project structure and boilerplate code
14. Sprint planning agent generates a sprint plan and discusses user stories with the developer agents
15. Developers action the tasks in the sprint plan and review the code with the lead developer agent
16. Unit tests are written and executed by the developer agents and the code is updated until all tests pass
17. Lead developer agent reviews the code and merges it into the main branch if it meets the requirements
18. Lead developer agent deploys the code to the staging environment and notifies the user
19. User reviews the application in the staging environment and notifies the business analyst agent of any issues
20. Issues are resolved and the application is deployed to the production environment after the user approves it
