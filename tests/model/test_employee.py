from app.model.employee import Employee


def test_employee_repr():
    employee = Employee(id=1, name='John Doe', salary=50000)
    assert repr(employee) == "<Employee(id=1, name='John Doe', salary=50000)>"

def test_employee_str():
    employee = Employee(id=1, name='John Doe', salary=50000)
    assert str(employee) == "Employee ID: 1, Name: John Doe, Salary: 50000"