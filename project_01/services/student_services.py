import aiofiles
import json

FILE_NAME="data.json";

async def get_students():
    async with aiofiles.open(FILE_NAME, "r") as file:
        content = await file.read()
    return json.loads(content)

async def create_student(student):
    students = await get_students()

    students.append(student.model_dump())

    async with aiofiles.open(FILE_NAME, 'w') as file:
        await file.write(json.dumps(students, indent=2))

    return student