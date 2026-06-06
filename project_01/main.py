from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiofiles
import json

app = FastAPI()

FILE_NAME = "data.json"

class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int

# Synchronous
# @app.get("/")
# async def get_students():
#     with open (FILE_NAME, "r") as file:
#         return json.load(file)
#
# @app.get("/{id}")
# async def get_student_by_id(id: int):
#     with open(FILE_NAME, "r") as file:
#         users = json.load(file)
#     user = next((u for u in users if u["id"] == id), None)
#
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# Asynchronous
@app.get('/')
async def get_students():
    async with aiofiles.open(FILE_NAME, "r") as file:
        content = await file.read()
    return json.loads(content)

@app.get('/{id}')
async def get_student_by_id(id: int):
    async with aiofiles.open(FILE_NAME, "r") as file:
        content = await file.read()
        students = json.loads(content)

    for student in students:
        if student['id'] == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.post('/')
async def create_student(student: Student):
    async with aiofiles.open(FILE_NAME, "r") as file:
        content = await file.read()
        students = json.loads(content)

    students.append(student.model_dump())

    async with aiofiles.open(FILE_NAME, "w") as file:
        await file.write(json.dumps(students, indent=2))

    return {
        "status": 201,
        "message": "Student created!",
        "student": student
    }