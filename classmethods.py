class Student:
    count = 0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa

    def get_into(self):
        return f"{self.name} = {self.gpa}"
    
    @classmethod #use when need to use atrribute of the class
    def get_count(cls):
        return f"Total no. of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA : {cls.total_gpa / cls.count :.2f}"
    
student1=Student("Spange", 3.2)
student2=Student("Spante", 3.4)
student3=Student("Spanve", 3.3)
print(Student.get_count())
print(Student.get_average_gpa())
