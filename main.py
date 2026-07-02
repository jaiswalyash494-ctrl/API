from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message":"hello yash"}

from fastapi import FastAPI
from pydantic import BaseModel

# Creating FastAPI app
app = FastAPI()

# Student model
class Student(BaseModel):
    name: str
    course: str
    age: int

# POST API
@app.post("/")
async def create_sdetail(student: Student):
    return {
        "Message": "Student details created successfully",
        "Name": student.name,
        "Course": student.course,
        "Age": student.age
    }