from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
app = FastAPI()
employees = [
    {
        "employee_id": "EMP001",
        "name": "Rahul",
        "age": 25,
        "qualification": "MCA",
        "salary": 50000
    },
    {
        "employee_id": "EMP002",
        "name": "Ankita",
        "age": 26,
        "qualification": "BCA",
        "salary": 25000
    }
]


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id):
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
    )


class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    age: int
    qualification: str
    salary: float


@app.post("/employees", status_code=201)
def create_employee(employee: EmployeeCreate):
    for existing_employee in employees:
        if existing_employee["employee_id"] == employee.employee_id:
            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )
    employees.append(employee.model_dump())
    return employee.model_dump()


@app.get("/")
def home():
    return {"message": "Employee Management API"}
