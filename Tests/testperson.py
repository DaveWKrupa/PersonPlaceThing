from Person import Person
from CustomExceptions import InvalidZipCodeError, InvalidPhoneNumberError
from CustomExceptions import InvalidRecordIDError, InvalidTableNameError
from CustomExceptions import DatabaseSQLError, InvalidParametersError

import uuid
# create a person object and assign values to properties
# this test should include valid values and should not throw
# any errors

person = Person()
assert person.record_id == uuid.UUID(int=0), "Record ID test for person failed"

person.prefix_name = "Mr."
person.first_name = "Billy"
person.middle_name = "Bob"
person.last_name = "Thorton"
person.suffix_name = "III"
person.street = "385 Unknown Blvd."
person.street2 = "Apt. 49"
person.city = "Brighton"
person.state = "Colorado"
try:
    person.phone_number = "123.456-7890"
except InvalidPhoneNumberError as e:
    assert False, e.message


try:
    person.zip_code = "12345-6789"
except InvalidZipCodeError as e:
    assert False, e.message

print("Person 1")
print("Before Save")
print(person)
print(" ")
try:
    person.save()
except DatabaseSQLError as e:
    assert False, e.message
except InvalidTableNameError as e:
    assert False, e.message
except InvalidParametersError as e:
    assert False, e.message
except InvalidRecordIDError as e:
    assert False, e.message

print(person.record_id)
print(" ")
# load the person into a new object
person2 = Person()
try:
    person2.load(person.record_id)
except DatabaseSQLError as e:
    assert False, e.message
except InvalidTableNameError as e:
    assert False, e.message
except InvalidParametersError as e:
    assert False, e.message
except InvalidRecordIDError as e:
    assert False, e.message

print("person2")
print(person2)

# now update the record and save

person2.phone_number = "987-654-3210"
person2.address.street = "385 Known Ave."
try:
    person2.save()
except DatabaseSQLError as e:
    assert False, e.message
except InvalidTableNameError as e:
    assert False, e.message
except InvalidParametersError as e:
    assert False, e.message
except InvalidRecordIDError as e:
    assert False, e.message

print(" ")
print("person2updated")
print(person2)

print(" ")
print("person3")
# load the person into a new object
# should load updated values from db
person3 = Person()
try:
    person3.load(person2.record_id)
except DatabaseSQLError as e:
    assert False, e.message
except InvalidTableNameError as e:
    assert False, e.message
except InvalidParametersError as e:
    assert False, e.message
except InvalidRecordIDError as e:
    assert False, e.message


print(person3)

print(" ")
print("delete person3")
# delete the record without throwing any errors
person3_record_id = person3.record_id
print(person3_record_id)
try:
    person3.delete()
except DatabaseSQLError as e:
    assert False, e.message
except InvalidTableNameError as e:
    assert False, e.message
except InvalidParametersError as e:
    assert False, e.message
except InvalidRecordIDError as e:
    assert False, e.message

print("record deleted")


# now try to reload the deleted record
# the load function should pass back False
# and the person object should be in an initialized state

person4 = Person()
try:
    print(person4.load(person3_record_id))
except DatabaseSQLError as e:
    assert False, e.message
except InvalidTableNameError as e:
    assert False, e.message
except InvalidParametersError as e:
    assert False, e.message
except InvalidRecordIDError as e:
    assert False, e.message

print(" ")
print("person4 record id")
print(person4.record_id)
print("person4")
print(person4)
