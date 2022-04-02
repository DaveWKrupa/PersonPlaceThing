
# from DataFactory import TagsList
#
# data = TagsList().get_tags_list()
# print(data)
# lower_case_tags = map(lambda x: x.upper(), data)
# print(list(lower_case_tags))


# class FirstClass:
#     def __init__(self):
#         refresh_callback = self.get_refresh_callback_function()
#         self.second_class = SecondClass(refresh_callback)
#
#     def save(self):
#         self.second_class.save()
#
#     def get_refresh_callback_function(self):
#         def refresh_data_callback_function():
#             self.refresh_data()
#
#         return refresh_data_callback_function
#
#     def refresh_data(self):
#         print("refreshing data")
#
#
# class SecondClass:
#     def __init__(self, refresh_callback):
#         self.refresh_callback = refresh_callback
#
#     def save(self):
#         self.refresh_the_data()
#
#     def refresh_the_data(self):
#         self.refresh_callback()
#
#
# fc = FirstClass()
# fc.save()









# my_list = ["one", "two", "three", "four", "four"]
# print(my_list.count("four"))
# print(my_list)
# my_list = list(filter(lambda val: val != "four", my_list))
# print(my_list)
#
# my_set = set(my_list)
# print(my_set)


# from PersonPlaceThingDB import PersonPlaceThingDB
#
# ppt = PersonPlaceThingDB()
# records = ppt.read("person", {})
# print(records)

# #
# class MyParentClass:
#     def __init__(self):
#         self._myparentclassattribute = "My parent class attribute"
#
#     def myfunc(self, first_arg):
#         print("myfunc " + first_arg)
#
# class MySecondParentClass:
#     def __init__(self):
#         self._myparentclassattribute = "My parent class attribute"
#
#     def myfunctwo(self, first_arg):
#         print("myfunctwo " + first_arg)
# #
# #
#
#
# class MyChildClass(MyParentClass):
#     def __init__(self):
#         super().__init__()
#         self.mychildclassattribute = "My child class attribute"
#
#     # def myfunc(self, first_arg, second_arg):
#     #     print(first_arg, second_arg)
#
#
# class MyChildClass2(MyParentClass):
#     def __init__(self):
#         super().__init__()
#         self.mychildclassattribute = "My child class2  attribute"
#




    # @property
    # def myparentclassattribute(self):
    #     return None
    #
    # @myparentclassattribute.setter
    # def myparentclassattribute(self, value):
    #     pass

#     @property
#     def myoverride(self):
#         return self._myparentclassattribute
#
#     @myoverride.setter
#     def myoverride(self, value):
#         self._myparentclassattribute = value
#
#
#
# child = MyChildClass()
# #print(child.myparentclassattribute)
# print(child.myoverride)
# child.myoverride = "HDFuihe"
# print(child.myoverride)
# print(child._myparentclassattribute)
# from DateTimeManager import DateTimeManager
#
# dtm = DateTimeManager()
#
#
# date_string1 = "2022-01-23"
# date_string2 = "2022-01-23"
# time_string1 = ""
# time_string2 = ""
# date_time1_string = '2022-01-23 17:00:00-07:00'
# date_time2_string = ' 2022-01-23 17:00:01-07:00'
#
# dtm.start_date = date_string1
# print(dtm.start_date)
# print("hello")






# from PersonPlaceThingDB import PersonPlaceThingDB
#
#
# test = [{'id': 'ad8ea1dc-20c0-4b7a-b7da-65faf51de7d0', 'first_name': 'Professor Plum', 'phone_number': '444.444.4444', 'street': '973 Elm St.', 'street2': None, 'city': None, 'state': None, 'zip_code': None, 'middle_name': None, 'last_name': None, 'prefix_name': None, 'suffix_name': None}]
#
# val = test[0]["phone_number"]
# print(val)

#print(ppt.read("testtable"))

#ppt.update("testtable")







#print(ppt.get_select_statement("testtable", id="asdkfh", name="asdfohwae", age=87, hiredate="2002-07-19"))
#print(ppt.get_column_names("testtable"))
#print(ppt.get_parameter_values_tuple(id="asdkfh", name="asdfohwae", age=87, hiredate="2002-07-19"))
#print(ppt.read("testtable", id="asdkfh", name="asdfohwae", age=87, hiredate="2002-07-19"))









    # def connect(self):
    #     """ Connect to the PostgreSQL database server """
    #     conn = None
    #     try:
    #         # read connection parameters
    #         params = Configuration.config(filename='database.ini', section='postgresql')
    #
    #         # connect to the PostgreSQL server
    #         #print('Connecting to the PostgreSQL database...')
    #         conn = psycopg2.connect(**params)
    #
    #         # # create a cursor
    #         # cur = conn.cursor()
    #         # cur.execute('SELECT * FROM '
    #         #             '"TestTable";')
    #         # for table in cur.fetchall():
    #         #     print(table)
    #
    #
    #         #print(uuid.uuid4())
    #         # cur.execute('INSERT INTO "TestTable" ("ID", "Name", "Age", "Birthday")'
    #         #             ' VALUES(%s, %s, %s, %s)', ('4f45de89-9a27-44da-a2e4-7fd5235b5abf',
    #         #             'Fred', 8, '2013-06-07'))
    #         # conn.commit()
    #         # cur.execute('SELECT * FROM '
    #         #             '"TestTable";')
    #         # for table in cur.fetchall():
    #         #     print(table)
    #
    #         # cur.execute("""SELECT table_name FROM information_schema.tables
    #         #    WHERE table_schema = 'public'""")
    #         #
    #         # for table in cur.fetchall():
    #         #     print(table)
    #
    #
    #         # cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    #         # cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
    #         # cur.execute("SELECT * FROM test;")
    #         # cur.fetchone()
    #         #cur.execute("SELECT * FROM Person;")
    #         #cur.fetchone()
    #         # execute a statement
    #         # print('PostgreSQL database version:')
    #         # cur.execute('SELECT version()')
    #         #
    #         # # display the PostgreSQL database server version
    #         # db_version = cur.fetchone()
    #         # print(db_version)
    #
    #         # close the communication with the PostgreSQL
    #         cur.close()
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print(error)
    #     finally:
    #         if conn is not None:
    #             conn.close()
    #             print('Database connection closed.')

# sql = ""
        # for k, v in kwargs.items():
        #     print(f'{k} is {v} years old')
        # cur.execute('INSERT INTO "TestTable" ("ID", "Name", "Age", "Birthday")'
        #         #             ' VALUES(%s, %s, %s, %s)', ('4f45de89-9a27-44da-a2e4-7fd5235b5abf',
        #         #             'Fred', 8, '2013-06-07'))
        #         # conn.commit()


       # with ManagedConnection.get_managed_cursor() as cur:

        # with ManagedConnection.get_managed_connection() as conn:
        #     # create a cursor
        #     cur = conn.cursor()
        #     sql = f'SELECT * FROM "{table_name}" '
        #     print(sql)
            # cur.execute("SELECT * FROM ")
            #             #f"""{table_name}"" "
            #             # f"WHERE ""ID"" " = " +
            #
            #             # '{record_id}';"
            #             )
            # for table in cur.fetchall():
            #     print(table)


