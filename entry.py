from address import AddressBook

address1 = AddressBook('Aye', '0912345678')
print('Phone No.', address1.phone)
address1.update_phone('0987654321')
print('Updated Phone No.', address1.phone)
address1.update_name('Mrat')
print('Updated Name.',address1.name)