from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.ui import Console
import asyncio

from quality.agents.unit_test_palnner import planning_agent
from quality.agents.unit_test_developer import utc_developer
from quality.agents.unit_test_executor import utc_executor
from quality.agents.util.util import get_model_client

text_mention_termination = TextMentionTermination("TERMINATE")
max_message_termination = MaxMessageTermination(max_messages=25)

termination = text_mention_termination | max_message_termination

selector_prompt = """
    Select an agent to perform task.

    {roles}

    Current conversation context:
    {history}

    Read the aabove conversation, then select an agent from {participants} to perform the next task.    
    The planner agent must first assign the unit test development task to the developer agent (UnitTestDeveloper), and after all tests are written and saved, assign the test execution task to the executor agent (UnitTestExecutor).
    Only select one agent at a time.
"""

team = SelectorGroupChat(
    [planning_agent, utc_developer, utc_executor],
    model_client=get_model_client(),
    termination_condition=termination,
    selector_prompt=selector_prompt,
    allow_repeated_speaker=True,
)

# task = ("Create unit tests for the all the Python files present in path: /home/namit/Projects/workspaces/ai-agents/src/app"        
#         "Make sure to cover all cases and conditions in the tests."
#         "After saving all the test file content in the tests in tests folder"
#         "After saving all the test files, execute pytest on the entire tests directory."                
#         "Generate one single complete HTML report for all the test case in html_report_dir='tests' folder, containing the status for every test case (pass/fail) and test file."
#         "Mock the database connection and do not connect to database")

task = (
    "Step 1: The planner agent must assign the task of creating unit tests for all Python files in the path '/home/namit/Projects/workspaces/ai-agents/src/app' to the developer agent (UnitTestDeveloper). "
    "The developer agent should search for all Python files, generate comprehensive pytest unit tests for each, and save them in the corresponding path under the tests folder, preserving the subdirectory structure. "
    "Step 2: After all test files are saved, the planner agent must assign the task of executing pytest on the entire tests directory to the executor agent (UnitTestExecutor). "
    "The executor agent should generate a single complete HTML report in html_report_dir='tests', containing the status for every test case (pass/fail) and test file. "
    "Mock the database connection and do not connect to the database."
)

asyncio.run(Console(team.run_stream(task=task)))