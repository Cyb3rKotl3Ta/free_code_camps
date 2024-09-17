from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        'name': 'Jhon',
        'age': 17,
        'class': 'year 11',
    },
}


class Student(BaseModel):
    name: str
    age: int
    year: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

@app.get('/')
def index():
    return {'name': 'First Data'}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(description='ID of Student', gt=0)):
    return students[student_id]

@app.get('/get-by-name/{student_id}')
def get_student(*, student_id: int,  name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data not found'}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {'Error': 'Student exists'}

    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {'Error': 'Student does not exist'}

    if student.name is not None:
        students[student_id].name = student.name

    if student.age is not None:
        students[student_id].age = student.age

    if student.year is not None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {'Error': 'Student does not exist'}

    del students[student_id]
    return {'Message': 'Student delete successfully'}
