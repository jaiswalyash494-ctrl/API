from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Nitish", "course": "AI", "city": "Mumbai"},
    2: {"name": "yash", "course": "Data Science", "city": "Pune"},
    3: {"name": "ivan", "course": "Cyber Security", "city": "Delhi"}
}

@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id, "Student Not Found")


@app.get("/search")
def search_students(course: str = None, city: str = None):
    return {
        "course": course,
        "city": city
    }


@app.get("/student/{student_id}/details")
def student_details(student_id: int, semester: int, section: str):
    return {
        "student_id": student_id,
        "semester": semester,
        "section": section
    }
