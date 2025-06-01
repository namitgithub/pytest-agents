from fastapi import APIRouter, HTTPException
from fastapi import status
from app.service.employee_service import EmployeeService
from app.dto.employee_dto import EmployeeDTO
from typing import List

router = APIRouter()

class EmployeeController:
    def __init__(self):        
        self.employee_service = EmployeeService()
        self.router = router
        router.add_api_route(
            "/employees",
            self.get_all_employees,
            methods=["GET"],
            status_code=status.HTTP_200_OK
        )
        router.add_api_route(
            "/employees/{employee_id}",
            self.get_employee,
            methods=["GET"],
            status_code=status.HTTP_200_OK
        )
        router.add_api_route(
            "/employees",
            self.create_employee,
            methods=["POST"],
            status_code=status.HTTP_201_CREATED
        )

    def get_all_employees(self)->List[EmployeeDTO]:
        return self.employee_service.get_all_employees()

    def create_employee(self, employee_data: EmployeeDTO):
        return self.employee_service.add_employee(employee_data)

    def get_employee(self, employee_id)->EmployeeDTO:
        return self.employee_service.get_employee_by_id(employee_id)
