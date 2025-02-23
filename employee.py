from address import AddressBook
class EmployeeAddressBook(AddressBook):
    def __init__(self, name, phone, id, dept):
        AddressBook.__init__(self,name,phone)
        self.empid = id
        self.department = dept