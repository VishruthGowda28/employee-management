from fastapi import FastAPI
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


@app.get("/")
def home():
    return {"message": "Employee Management API"}
