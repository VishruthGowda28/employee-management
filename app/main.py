from fastapi import FastAPI
from fastapi import HTTPException
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


@app.get("/")
def home():
    return {"message": "Employee Management API"}
