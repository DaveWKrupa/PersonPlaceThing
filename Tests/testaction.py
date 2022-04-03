from Action import Action


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


action = Action(get_data_saved_callback_func(), get_invalid_data_callback_func())


action.short_description = "My action"
action.long_description = "This is my action"
action.start_date_time = "2022-03-29 18:21:00-07:00"
action.end_date_time = "2022-03-29 19:21:00-07:00"
action.add_tags("Movies", "Books")
action.add_tags(["Social", "Reading"], "Producing", ["Profession", "Writing"])
result = action.save()
print(result)


action.long_description = "something else"
result = action.save()
print(result)

result = action.delete()
print(result)
