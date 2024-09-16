from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        'name': 'Jhon',
        'age': 17,
        'class': 'year 11',
    },
}
print(len(students))

@app.get('/')
def index():
    return {'name': 'First Data'}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(description='ID of Student', gt=0, le=len(students))):
    return students[student_id]

@app.get('/get-by-name')
def get_student(name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data not found'}
