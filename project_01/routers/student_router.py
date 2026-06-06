from fastapi import APIRouter
from models.student import Student
from services.student_services import (
    get_students,
    create_student
)

router = APIRouter(prefix="/students", tags=["Students"])

@router.get('/')
async def read_students():
    return await get_students()

@router.post('/')
async def write_student(student: Student):
    return await create_student(student)