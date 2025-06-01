from quality.agents.util.util import get_model_client
from autogen_agentchat.agents import AssistantAgent
import subprocess
import os

def execute_pytest_tool(test_dir: str, html_report_dir: str = None):
    """
    After saving all test files, execute pytest on the entire tests directory to generate a complete HTML report 
    containing the status for every test file and test case (pass/fail).
    """
    try:
        os.makedirs(html_report_dir, exist_ok=True)
        html_report_path = os.path.join(html_report_dir, "report.html")
        cmd = [
            "pytest", test_dir, "--disable-warnings", "-q",
            "--html", html_report_path, "--self-contained-html"
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )
        output = result.stdout + result.stderr
        output += f"\nHTML report generated at: {html_report_path}"
        return output
    except Exception as e:
        return f"Error executing pytest: {e}"
    
    
utc_executor = AssistantAgent(
    name="UnitTestExecutor",
    description="An agent that executes unit tests for Python code.",
    model_client=get_model_client(),
    tools=[execute_pytest_tool],
    system_message="""                
                You are a unit test executor.
                Your job is to execute all unit tests for Python code in the provided directory.
                Execute all tests and report the results.                

                Use the following format for your response:
                1. <test_directory_path> : <test_results>
                2. HTML report path: <html_report_path>

                After executing all tests, Also generate a pytest HTML report in the specified directory, which should include all test files and their statuses. 
                summarize the findings and end with "TERMINATE".
            """,
    
    model_client_stream=True
)