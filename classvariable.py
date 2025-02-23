
class Student:
    class_year=2023
    num_students=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 21)
student2 = Student("Jane", 22)
student3 = Student("Alice", 23)
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)