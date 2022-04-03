from Event import Event


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


event = Event(get_data_saved_callback_func(), get_invalid_data_callback_func())


event.short_description = "My event"
event.long_description = "This is my event"
event.start_date_time = "2022-03-29 18:21:00-07:00"
event.end_date_time = "2022-03-29 19:21:00-07:00"
event.add_tags("Movies", "Books")
event.add_tags(["Social", "Reading"], "Producing", ["Profession", "Writing"])
result = event.save()
print(result)


event.long_description = "something else"
result = event.save()
print(result)

result = event.delete()
print(result)
