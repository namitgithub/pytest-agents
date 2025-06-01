from autogen_agentchat.agents import AssistantAgent

import os
from quality.agents.util.util import get_model_client

def search_file_tool(directory: str, pattern: str = None):
    """
    Recursively searches for files in the given directory.
    Optionally filter by filename pattern (e.g., '.py').
    Returns a list of file paths.
    """
    matches = []
    for root, _, files in os.walk(directory):
        print(directory)
        for filename in files:
            if pattern is None or pattern in filename:
                matches.append(os.path.join(root, filename))
    return matches

def save_file_content(file_path: str, content: str):
    """
    Saves the given content to the specified file path.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)
    return file_path

# def get_test_file_path(source_file_path: str, src_root: str = "./src", tests_root: str = "../tests") -> str:
#     """
#     Given a source file path, returns the corresponding test file path under the tests directory,
#     preserving the subdirectory structure.
#     Example: src/app/model/foo.py -> tests/app/model/test_foo.py
#     """
#     # Find the relative path after src/
#     src_root_with_sep = src_root + os.sep
#     if src_root_with_sep in source_file_path:
#         rel_path = source_file_path.split(src_root_with_sep, 1)[1]
#     else:
#         rel_path = os.path.relpath(source_file_path, src_root)
#     dir_name, base_name = os.path.split(rel_path)
#     test_base_name = f"test_{base_name}"
#     return os.path.join(tests_root, dir_name, test_base_name)     

def read_file_content(file_path: str) -> str:
    """
    Reads the content of the specified file path.
    """
    with open(file_path, 'r') as file:
        return file.read()

utc_developer = AssistantAgent(
    name="UnitTestDeveloper",
    description="An agent that develops unit tests for Python code.",
    model_client=get_model_client(),
    tools=[search_file_tool, read_file_content, save_file_content],
    system_message="""
                You are a unit test developer.
                Your job is to write unit tests for Python code.
                You will be provided with a directory containing Python files.
                Search for files, read the file content and write pytest for them.
                For each source file in src/app folder, create the test file in the corresponding path under the tests folder,
                preserving the subdirectory structure. For example, for 'app/module/foo.py', 
                create the test at 'tests/app/module/test_foo.py'. Create directories if required.
                After generating the test code, use the save_file_content tool to save the test code to the correct file path.
                Ensure that all the cases and conditions are covered in the tests.
                For example, include tests for edge cases, invalid inputs, boundary conditions, 
                expected outputs, and any exceptional scenarios specific to the code being tested.

                Use the following format for your response:
                1. <test_file_path> : <test_code>
                2. Call save_file_content with the test file path and test code.

                After writing and saving all tests, summarize the findings and end with "TERMINATE".
                """,
    model_client_stream=True
)