from app.repository.employee_repository import EmployeeRepository
class EmployeeService:
    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def get_all_employees(self):
        return self.employee_repository.get_all()

    def get_employee_by_id(self, employee_id):
        return self.employee_repository.get_employee_by_id(employee_id)

    def add_employee(self, employee_data):
        return self.employee_repository.add_employee(employee_data)

    def update_employee(self, employee_id, employee_data):
        return self.employee_repository.update_employee(employee_id, employee_data)
