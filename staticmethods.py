class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod #use when need to use attribute from __init__
    def is_valid_position(position):
        valid_positions = ['Manager' , 'Cashier' , 'Cook' , 'Janitor']
        return position in valid_positions

employee1=Employee("Eurie",'Manager')
employee2=Employee("Euriel",'Cashier')
employee3=Employee("Euries",'Cook')
employees=[employee1,employee2,employee3]
# print(Employee.is_valid_position('Driver'))

for e in employees:
    print(e.get_info())

