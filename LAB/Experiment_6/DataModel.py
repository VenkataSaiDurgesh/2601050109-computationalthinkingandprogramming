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
