import pytest
from app.service.employee_service import EmployeeService
from unittest.mock import MagicMock

@pytest.fixture
def employee_service():
    service = EmployeeService()
    return service

@pytest.fixture
def mock_repository(monkeypatch, employee_service):
    mock = MagicMock()
    monkeypatch.setattr(service, 'employee_repository', mock)
    return mock


def test_get_all_employees(employee_service, mock_repository):
    mock_repository.get_all.return_value = [{'id': 1, 'name': 'John Doe', 'salary': 50000}]
    employees = employee_service.get_all_employees()
    assert len(employees) == 1
    assert employees[0]['name'] == 'John Doe'
