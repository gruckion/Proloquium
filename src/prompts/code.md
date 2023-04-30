# Instructions

Generate a Python program for the following task: {task_description}.

Provide the code inside markdown code blocks with the file path and name as a cli command at the beginning of each block.

Also, provide any necessary test cases inside markdown code blocks with the file path and name as a comment at the beginning of each block.

Critical rules:

- Code must be declaritive, pythonic, with readable variable names
- Must use pytest
- Use fixtures when possible to avoid repetition.
- Split into # arrange, # act, # assert sections.
- Mock filesystem and network calls when possible.
- Must be strongly typed.
- File path/name must be correct.

For example:

File: `src/{project_name}/example.py`

```python
"""This is an example module."""

def example_function(input: Type):
    """This is an example function."""
    pass

    # ... more functions and classes to meet the requirements
```

File: `tests/{project_name}/test_example.py`

```python
"""This is an example test module."""

from {project_name}.example import example_function

def test_example_function(input: Type):
    """This is an example test."""
    # arrange
    # ... more fixtures to meet the requirements

    # act
    # ... more actions to meet the requirements

    # assert
    assert example_function() is None

    # ... more assertions and tests to meet the requirements
```
