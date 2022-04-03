from Person import Person


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


person = Person(get_data_saved_callback_func(), get_invalid_data_callback_func())


person.prefix_name = "Mr."
person.first_name = "Billy"
person.middle_name = "Bob"
person.last_name = "Thorton"
person.suffix_name = "III"
person.address.street = "385 Unknown Blvd."
person.address.street2 = "Apt. 49"
person.address.city = "Brighton"
person.address.state = "Colorado"
person.address.zip_code = "12345-6789"
person.phone_number = "123.456-7890"

person.add_tags("Movies", "Books")
person.add_tags(["Social", "Reading", "Producing", "Profession", "Writing"])
result = person.save()
print(result)


person.last_name = "something else"
result = person.save()
print(result)

result = person.delete()
print(result)
