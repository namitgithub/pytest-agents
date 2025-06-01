from app.utils.helpers import get_db
class EmployeeRepository:
    def __init__(self):
        self.db = next(get_db())

    def get_employee_by_id(self, employee_id):
        return self.db.query("SELECT * FROM employees WHERE id = ?", (employee_id,)).fetchone()

    def add_employee(self, employee_data):
        self.db.execute("INSERT INTO employees (name, position) VALUES (?, ?)", 
                        (employee_data['name'], employee_data['position']))
        self.db.commit()

    def update_employee(self, employee_id, employee_data):
        self.db.execute("UPDATE employees SET name = ?, position = ? WHERE id = ?", 
                        (employee_data['name'], employee_data['position'], employee_id))
        self.db.commit()

    def delete_employee(self, employee_id):
        self.db.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        self.db.commit()