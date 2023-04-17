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
