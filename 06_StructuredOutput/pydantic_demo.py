from pydantic import BaseModel,EmailStr,Field

class student(BaseModel):
    name:str
    age:int
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10)


new_student:student={'name':'XY','age':90,'email':'abs@gmail.com','cgpa':9}

st=student(**new_student)

print(st)