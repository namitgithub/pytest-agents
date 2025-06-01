# pytest-agents

A Python project that leverages LLM-powered agents to automate the process of generating, saving, and executing unit tests for Python codebases. The system uses [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [pytest](https://pytest.org/), and [autogen-agentchat](https://github.com/microsoft/autogen) to orchestrate a team of agents that plan, develop, and execute tests, producing a comprehensive HTML report.

---

## Features

- **Agent-based Workflow**: Uses three specialized agents:
  - **PlanningAgent**: Breaks down the testing workflow and delegates tasks.
  - **UnitTestDeveloper**: Searches for Python files, generates pytest-based unit tests, and saves them in the correct structure.
  - **UnitTestExecutor**: Executes all tests and generates an HTML report.
- **Automatic Test Generation**: For every Python file in `src/app`, corresponding tests are generated and saved in the `tests` directory, preserving the subdirectory structure.
- **Mocked Database**: All database interactions are mocked for safe and isolated testing.
- **Comprehensive Reporting**: Generates a single HTML report (`tests/report.html`) summarizing all test results.
- **FastAPI Example**: Includes a sample employee management API with DTO, service, repository, and controller layers.

---

## Project Structure

```
.
├── src/
│   ├── main.py
│   ├── app/
│   │   ├── controller/
│   │   │   └── employee_controller.py
│   │   ├── dto/
│   │   │   └── employee_dto.py
│   │   ├── model/
│   │   │   └── employee.py
│   │   ├── repository/
│   │   │   └── employee_repository.py
│   │   ├── service/
│   │   │   └── employee_service.py
│   │   └── utils/
│   │       └── helpers.py
│   └── quality/
│       ├── agents/
│       │   ├── unit_test_palnner.py
│       │   ├── unit_test_developer.py
│       │   ├── unit_test_executor.py
│       │   └── util/
│       │       └── util.py
│       └── __init__.py
├── tests/
│   ├── controller/
│   ├── dto/
│   ├── model/
│   ├── repository/
│   ├── service/
│   ├── utils/
│   └── report.html
├── pyproject.toml
├── poetry.toml
├── .env
└── README.md
```

---

## How It Works

### 1. Agent Orchestration

The entry point is [`src/main.py`](src/main.py), which sets up a `SelectorGroupChat` with three agents:

- [`quality.agents.unit_test_palnner.planning_agent`](src/quality/agents/unit_test_palnner.py)
- [`quality.agents.unit_test_developer.utc_developer`](src/quality/agents/unit_test_developer.py)
- [`quality.agents.unit_test_executor.utc_executor`](src/quality/agents/unit_test_executor.py)

The planner agent delegates:
- Test generation to the developer agent.
- Test execution and report generation to the executor agent.

### 2. Test Generation

[`utc_developer`](src/quality/agents/unit_test_developer.py) uses tools to:
- Search for Python files in `src/app`.
- Read file contents.
- Generate and save pytest-based unit tests in the `tests` directory, mirroring the source structure.

### 3. Test Execution

[`utc_executor`](src/quality/agents/unit_test_executor.py) runs all tests using `pytest` and generates a single HTML report at `tests/report.html`.

### 4. Mocked Database

All database access in [`app.utils.helpers.get_db`](src/app/utils/helpers.py) is mocked using `unittest.mock.MagicMock` to ensure tests do not require a real database.

---

## Example: Employee API

The project includes a sample Employee API with the following layers:

- **Model**: [`app.model.employee.Employee`](src/app/model/employee.py)
- **DTO**: [`app.dto.employee_dto.EmployeeDTO`](src/app/dto/employee_dto.py)
- **Repository**: [`app.repository.employee_repository.EmployeeRepository`](src/app/repository/employee_repository.py)
- **Service**: [`app.service.employee_service.EmployeeService`](src/app/service/employee_service.py)
- **Controller**: [`app.controller.employee_controller.EmployeeController`](src/app/controller/employee_controller.py)

---

## Running the Project

### 1. Install Dependencies

```sh
poetry install
```

Or with pip:

```sh
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=sk-...
```

### 3. Start the Agent Workflow

```sh
poetry run python src/main.py
```

### 4. View Test Report

After execution, open `tests/report.html` in your browser to see the test results.

---

## Running Tests Manually

You can run all tests and generate the HTML report manually:

```sh
pytest tests --html=tests/report.html --self-contained-html
```

---

## Customization

- **Agent Prompts**: Modify the system messages in the agent definitions in [`src/quality/agents/`](src/quality/agents/) to change agent behavior.
- **Test Directory**: Change the source or test directory paths in [`src/main.py`](src/main.py) or agent tools as needed.

---

## License

MIT License

---

## Acknowledgements

- [Microsoft AutoGen](https://github.com/microsoft/autogen)
- [pytest](https://pytest.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)