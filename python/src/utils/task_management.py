"""Task management module."""

import time
from collections import deque

from common.config import settings
from utils.openai_utils import get_ada_embedding, openai_call
from utils.pinecone_utils import PineconeUtils


class TaskManager:
    """Task management class."""

    def __init__(self, objective: str, initial_task: str):
        """Initialize the task manager."""
        print("Initializing task manager...")

        self.objective = objective
        self.initial_task = initial_task
        self.task_list = deque([])
        self.task_id_counter = 0

        self.pinecone_utils = PineconeUtils(
            settings.TABLE_NAME,
            settings.OBJECTIVE,
        )

    def add_task(self, task: dict):
        """Add a task to the task list."""
        print(f"Adding task: {task['task_name']}")
        self.task_list.append(task)

    def task_creation_agent(
        self,
        objective: str,
        result: dict,
        task_description: str,
        #
        task_list: list[str],
    ):
        """Create new tasks based on the result of the last completed task."""

        prompt = f"""
        You are an task creation AI that uses the result of an execution
        agent to create new tasks with the following objective: {objective},
        The last completed task has the result: {result}.
        This result was based on this task description: {task_description}.
        These are incomplete tasks: {', '.join(task_list)}.
        Based on the result, create new tasks to be completed by the AI system
        that do not overlap with incomplete tasks.
        Return the tasks as an array.
        """
        response = openai_call(prompt)
        new_tasks = response.split("\n") if "\n" in response else [response]
        return [{"task_name": task_name} for task_name in new_tasks]

    def run(self):
        """Run the task management loop."""
        print("Running task manager...")

        first_task = {"task_id": 1, "task_name": self.initial_task}
        self.add_task(first_task)

        self.task_id_counter = 1
        while True:
            print("In task management loop...")
            print("Total tasks: " + str(len(self.task_list)))

            if self.task_list:
                # Print the task list
                print("\n*****TASK LIST*****\n")
                for t in self.task_list:
                    print(str(t["task_id"]) + ": " + t["task_name"])

                # Step 1: Pull the first task
                task = self.task_list.popleft()
                print("\n*****NEXT TASK*****\n")
                print(str(task["task_id"]) + ": " + task["task_name"])

                # Send to execution function to complete
                # the task based on the context
                result = self.execution_agent(
                    settings.OBJECTIVE,
                    task["task_name"],
                )
                this_task_id = int(task["task_id"])
                print("\033[93m\033[1m" + "\n*****TASK RESULT*****\n")
                print(result)

                # Step 2: Enrich result and store in Pinecone
                enriched_result = {
                    "data": result
                }  # This is where you should enrich the result if needed
                result_id = f"result_{task['task_id']}"
                vector = get_ada_embedding(enriched_result["data"])
                # get vector of the actual result extracted from the dictionary
                self.pinecone_utils.index.upsert(
                    [
                        (
                            result_id,
                            vector,
                            {"task": task["task_name"], "result": result},
                        )
                    ],
                    namespace=settings.OBJECTIVE,
                )

                # Step 3: Create new tasks and reprioritize task list
                new_tasks = self.task_creation_agent(
                    settings.OBJECTIVE,
                    enriched_result,
                    task["task_name"],
                    [t["task_name"] for t in self.task_list],
                )

                for new_task in new_tasks:
                    self.task_id_counter += 1
                    new_task.update({"task_id": self.task_id_counter})
                    self.add_task(new_task)

                self.prioritization_agent(this_task_id)

                # Sleep before checking the task list again
                time.sleep(1)

    def prioritization_agent(self, this_task_id: int):
        """Prioritize the tasks in the task list."""

        task_names = [t["task_name"] for t in self.task_list]
        next_task_id = int(this_task_id) + 1
        prompt = f"""
        You are an task prioritization AI tasked with cleaning the formatting
        of and reprioritizing the following tasks: {task_names}.
        Consider the ultimate objective of your team:{settings.OBJECTIVE}.
        Do not remove any tasks. Return the result as a numbered list, like:
        #. First task
        #. Second task
        Start the task list with number {next_task_id}."""

        response = openai_call(prompt)
        new_tasks = response.split("\n")
        self.task_list = deque()
        for task_string in new_tasks:
            task_parts = task_string.strip().split(".", 1)
            if len(task_parts) == 2:
                task_id = task_parts[0].strip()
                task_name = task_parts[1].strip()
                task = {"task_id": task_id, "task_name": task_name}
                self.task_list.append(task)

    def context_agent(self, query: str, number: int):
        """Get the context for a given query."""
        query_embedding = get_ada_embedding(query)
        results = self.pinecone_utils.index.query(
            query_embedding,
            top_k=number,
            include_metadata=True,
            namespace=settings.OBJECTIVE,
        )
        # print("***** RESULTS *****")
        # print(results)
        sorted_results = sorted(
            results.matches,
            key=lambda x: x.score,
            reverse=True,
        )
        return [(str(item.metadata["task"])) for item in sorted_results]

    def execution_agent(self, objective: str, task: str) -> str:
        """Execute a task and return the result."""

        context = self.context_agent(query=objective, number=5)
        # print("\n*******RELEVANT CONTEXT******\n")
        # print(context)
        prompt = f"""
        You are an AI who performs one task based on
        the following objective: {objective}\n.
        Take into account these previously completed tasks: {context}\n.
        Your task: {task}\nResponse:"""
        return openai_call(prompt, temperature=0.7, max_tokens=2000)
