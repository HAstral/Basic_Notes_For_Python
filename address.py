class AddressBook(object):
    version = 0.1
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def update_phone(self, phone):
        self.phone = phone

    def update_name(self, name):
        self.name = name