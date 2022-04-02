from Role import Role


def get_data_saved_callback_func():
    def data_saved_callback_func(**kwargs):
        for k, v in kwargs.items():
            print(k, v)

    return data_saved_callback_func


def get_invalid_data_callback_func():
    def invalid_data_callback_func(**kwargs):
        for k, v in kwargs.items():
            print(k, v)

    return invalid_data_callback_func


new_role = Role(get_data_saved_callback_func(), get_invalid_data_callback_func())
new_role.short_description = "Librarian"
new_role.long_description = "Long description of a librarian"
new_role.add_tags("Movies", "Books")
new_role.add_tags(["Social", "Reading", "Producing", "Profession", "Writing"])
result = new_role.save()
print(result)


new_role.long_description = "something else"
result = new_role.save()
print(result)

result = new_role.delete()
print(result)
#
# role_factory = RoleFactory()
# data = role_factory.get_all()
# for k, v in data.items():
#     print(k, v.short_description)
#
# print("***************************************")
# data = role_factory.get_where_like("suSpect")
# if data:
#     for k, v in data.items():
#         print(k, v.short_description)
#
# print("***************************************")
# data = role_factory.get_by_tags(["profession"])
# if data:
#     for k, v in data.items():
#         print(k, v.short_description)
