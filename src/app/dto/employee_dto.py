from pydantic import BaseModel

class EmployeeDTO(BaseModel):
    id: int
    name: str
    salary: float
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "salary": self.salary
        }