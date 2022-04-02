from RelationshipType import RelationshipType


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


new_obj = RelationshipType(get_data_saved_callback_func(), get_invalid_data_callback_func())
new_obj.short_description = "Lovers"
new_obj.long_description = "Long description of a lovers"
new_obj.add_tags("Movies", "Books")
new_obj.add_tags(["Social", "Reading", "Producing", "Profession", "Writing"])
result = new_obj.save()
print(result)


new_obj.long_description = "something else"
result = new_obj.save()
print(result)

result = new_obj.delete()
print(result)