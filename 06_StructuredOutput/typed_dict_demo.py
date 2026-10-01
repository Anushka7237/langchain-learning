from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int


new_person:Person={'name':'XYZ','age':56}

print(new_person)