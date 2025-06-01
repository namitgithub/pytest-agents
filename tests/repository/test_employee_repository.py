import pytest
from app.repository.employee_repository import EmployeeRepository
from unittest.mock import MagicMock

@pytest.fixture
def mock_db():
    db_mock = MagicMock()
    yield db_mock

@pytest.fixture
def employee_repository(mock_db):
    repository = EmployeeRepository()
    repository.db = mock_db  # Override the db with the mock
    return repository

def test_get_employee_by_id(employee_repository, mock_db):
    mock_db.query.return_value.fetchone.return_value = {'id': 1, 'name': 'John Doe', 'salary': 50000}
    employee = employee_repository.get_employee_by_id(1)
    assert employee['id'] == 1
    assert employee['name'] == 'John Doe'
    assert employee['salary'] == 50000
