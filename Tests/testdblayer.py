from PersonPlaceThingDB import PersonPlaceThingDB
from CustomExceptions import InvalidTableNameError

data = PersonPlaceThingDB().read("person", id="ad8ea1dc-20c0-4b7a-b7da-65faf51de7d0")
print(data)
#
#
#
# # test is_table_name_valid = True
# ppt = PersonPlaceThingDB()
# is_name_valid = False
# is_name_valid = ppt.is_table_name_valid("person")
# assert is_name_valid, "Test for is_table_name_valid = True failed."
#
# # test is_table_name_valid = False
#
# is_name_valid = False
# is_name_valid = ppt.is_table_name_valid("people")
# assert not is_name_valid, "Test for is_table_name_valid = False failed."
#
#
# expected_statement = "SELECT * FROM testtable WHERE id = %s AND name = %s AND age = %s AND hiredate = %s;"
# select_statement = ppt.get_select_statement("testtable", id="asdkfh", name="asdfohwae", age=87, hiredate="2002-07-19")
# assert select_statement == expected_statement, "Select statement test failed."
#
# expected_message = "The table name passed in does not exist in the database."
# exception_message = ""
# try:
#     ppt.read("badtablename")
# except InvalidTableNameError as e:
#     exception_message = e.message
#
# assert expected_message == exception_message
#
# expected_column_name_list = ['id', 'name', 'phone_number', 'address']
# column_name_list = ppt.get_column_names("person")
# assert column_name_list == expected_column_name_list, "Column name list test failed."
#
