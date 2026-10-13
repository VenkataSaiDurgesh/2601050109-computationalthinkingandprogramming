1. Algorithm / Procedure
Create a Student using a traditional class.
Create another Student using a dataclass.
Store name, ID, and age.
Display the student details.
Compare both implementations.
2. Very Simple Python Code
from dataclasses import dataclass


# Traditional class
class Student:
    def __init__(self, name: str, id: int, age: int) -> None:
        self.name = name
        self.id = id
        self.age = age

    def show(self) -> None:
        print(self.name, self.id, self.age)


# Dataclass
@dataclass
class StudentData:
    name: str
    id: int
    age: int


s1 = Student("Suma", 101, 22)
s2 = StudentData("Tabu", 102, 23)

print("Traditional Class:")
s1.show()

print("Dataclass:")
print(s2)
3. Input and Output
Output:

Traditional Class:
Suma 101 22

Dataclass:
StudentData(name='Tabu', id=102, age=23)
4. Inference
The same student data can be represented using both a traditional class and a dataclass. The dataclass requires less code.

5. Analysis
Traditional Class	Dataclass
More code	Less code
__init__() required	Automatically created
show() required	Easy object display
More manual work	Simpler for data storage
Conclusion: Dataclasses are useful when the main purpose of a class is to store data.
