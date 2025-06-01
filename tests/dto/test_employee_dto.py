from app.dto.employee_dto import EmployeeDTO

def test_employee_dto():
    employee_data = EmployeeDTO(id=1, name="John Doe", salary=50000)
    assert employee_data.id == 1
    assert employee_data.name == "John Doe"
    assert employee_data.salary == 50000
    assert employee_data.to_dict() == {"id": 1, "name": "John Doe", "salary": 50000}
