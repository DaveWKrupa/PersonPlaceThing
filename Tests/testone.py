from CustomExceptions import InvalidRecordIDError
from Address import Address
from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from datetime import datetime, timedelta



#date_time3 = '17:00:00-07:00'

# ppt = PersonPlaceThingDB()
# data = ppt.read("event", "4d546f17-3f5a-4fc6-9981-c0786cf9462b")
# print(data)
# dateval = data[0]["start_date"]
# timeval = data[0]["start_time"]
# duration = data[0]["duration_in_seconds"]
# print(dateval, timeval, duration)
# print(type(timeval))
#
# string_timeval = str(timeval)
# print(type(string_timeval))
# newtime = datetime.strptime(''.join(string_timeval.rsplit(':', 1)), '%H:%M:%S%z')
# print(newtime)
# timezone = newtime.timetz()
# print(timezone)
# print(type(timezone))
# try:
#     print(datetime.strptime(str(timezone), '%H:%M:%S%z'))
# except ValueError:
#     print("error")

# date_string1 = "2022-01-23"
# date_string2 = "2021-11-13"
# date_time1_string = '17:00:00-07:00'
# date_time2_string = '16:00:00-09:00'

# date_string1 = "2022-01-23"
# date_string2 = "2022-01-23"
# date_time1_string = '17:00:00-07:00'
# date_time2_string = '17:00:01-07:00'

# date_time1 = datetime.strptime(str(date_time1_string), '%H:%M:%S%z')
# date_time2 = datetime.strptime(str(date_time2_string), '%H:%M:%S%z')
# print(date_time1 > date_time2)
# print(date_time1 < date_time2)
# print(date_time1 == date_time2)
#
# print((date_time2 - date_time1).total_seconds())
#
# n1 = date_string1 + " " + date_time1_string
# n2 = date_string2 + " " + date_time2_string
# datetime_object1 = datetime.strptime(n1, '%Y-%m-%d %H:%M:%S%z')
# datetime_object2 = datetime.strptime(n2, '%Y-%m-%d %H:%M:%S%z')
# print(datetime_object1)
# print(type(datetime_object1))
# print(datetime_object2)
# print(type(datetime_object2))
# print(datetime_object2 > datetime_object1)
#
# try:
#     print(datetime.strptime(str(n1), '%Y-%m-%d %H:%M:%S%z'))
# except ValueError:
#     print("error")

# def __get_parameter_values_with_id_tuple(record_id=None, **kwargs):
#     param_vals = list()
#     for k, v in kwargs.items():
#         param_vals.append(v)
#     # append the record_id on the end
#     #param_vals.append(record_id)
#     return tuple(param_vals)
#
#
# print(__get_parameter_values_with_id_tuple(this="this", that="that"))

#print(PersonPlaceThingDB().exists("person", "ad8ea1dc-20c0-4b7a-b7da-65faf51de7d0"))
# print(RecordID.get_new_record_id())

# record_id = RecordID(RecordID.get_new_record_id())
# print(record_id)
# address = Address('123 Fake St.', 'Apt 2', 'Denver', 'Colorado', '12345-6789')
# print(address)
#
# recordid = RecordID()
# print(recordid)
#
# try:
#     recordid2 = RecordID("woerhkasdf")
#     print(recordid2)
# except InvalidRecordIDError as e:
#     print(f"Error1: {e}")
#
# try:
#     recordid2 = RecordID("eb2a771e-4079-4010-99f6-4505ab4d9dc8")
#     print(recordid2)
# except InvalidRecordIDError as e:
#     print(f"Error2: {e}")





# class MyClass:
#     def __init__(self, description):
#         self.description = description
#
#     def __str__(self):
#         return self.description
#
#
# myclass = MyClass("This is my class")

# print(myclass)


# string1 = "927-324.345"
# string2 = "1234897d34"
#
#
# for character in string1:
#     if not character.isnumeric() \
#             and character != "." \
#             and character != "-":
#         print("invalid1")
#
# for character in string2:
#     if not character.isnumeric() \
#             and character != "." \
#             and character != "-":
#         print("invalid2", character)
