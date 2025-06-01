import pytest
from fastapi.testclient import TestClient
from app.controller.employee_controller import EmployeeController
from unittest.mock import MagicMock
from app.dto.employee_dto import EmployeeDTO

# Set up the test client
employee_controller = EmployeeController()
client = TestClient(employee_controller.router)

@pytest.fixture
def mock_service(monkeypatch):
    mock_service = MagicMock()
    monkeypatch.setattr(employee_controller, 'employee_service', mock_service)
    return mock_service

def test_get_all_employees(mock_service):
    mock_service.get_all_employees.return_value = [EmployeeDTO(id=1, name="John Doe", salary=50000)]
    response = client.get("/employees")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "John Doe", "salary": 50000}]

def test_create_employee(mock_service):
    employee_data = EmployeeDTO(id=1, name="John Doe", salary=50000)
    mock_service.add_employee.return_value = employee_data
    response = client.post("/employees", json=employee_data.dict())
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "salary": 50000}

def test_get_employee(mock_service):
    employee_id = 1
    mock_service.get_employee_by_id.return_value = EmployeeDTO(id=1, name="John Doe", salary=50000)
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "salary": 50000}
