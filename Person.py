from Address import Address
from RecordID import RecordID
from CustomExceptions import InvalidPhoneNumberError
from PersonPlaceThingDB import PersonPlaceThingDB
from Constants import PHONE_FORMAT_ERROR
from Enums import TableNamesEnum, ColumnNamesEnum


class Person:
    def __init__(self, record_id=None,
                 first_name=None, middle_name=None, last_name=None,
                 prefix_name=None, suffix_name=None,
                 phone_number=None, street=None, street2=None,
                 city=None, state=None, zipcode=None):
        self.__record_id = RecordID(record_id).record_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.prefix_name = prefix_name
        self.suffix_name = suffix_name
        self.__phone_number = phone_number
        self.__address = Address(street, street2, city, state, zipcode)

    @property
    def record_id(self):
        return self.__record_id

    @property
    def name(self):
        return self.__format_name()

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if self.__is_phone_number_valid(value):
            self.__phone_number = value

    @property
    def address(self):
        return self.__address

    @property
    def street(self):
        return self.__address.street

    @street.setter
    def street(self, value):
        self.__address.street = value

    @property
    def street2(self):
        return self.__address.street2

    @street2.setter
    def street2(self, value):
        self.__address.street2 = value

    @property
    def city(self):
        return self.__address.city

    @city.setter
    def city(self, value):
        self.__address.city = value

    @property
    def state(self):
        return self.__address.city

    @state.setter
    def state(self, value):
        self.__address.state = value

    @property
    def zip_code(self):
        return self.__address.zip_code

    @zip_code.setter
    def zip_code(self, value):
        self.__address.zip_code = value

    def load(self, record_id):
        data = PersonPlaceThingDB().read(TableNamesEnum().PERSON, {}, record_id)
        if len(data) == 1:
            self.__record_id = record_id
            self.first_name = data[0][ColumnNamesEnum().FIRST_NAME]
            self.middle_name = data[0][ColumnNamesEnum().MIDDLE_NAME]
            self.last_name = data[0][ColumnNamesEnum().LAST_NAME]
            self.prefix_name = data[0][ColumnNamesEnum().PREFIX_NAME]
            self.suffix_name = data[0][ColumnNamesEnum().SUFFIX_NAME]
            self.__phone_number = data[0][ColumnNamesEnum().PHONE_NUMBER]
            self.__address = Address(data[0][ColumnNamesEnum().STREET],
                                     data[0][ColumnNamesEnum().STREET2],
                                     data[0][ColumnNamesEnum().CITY],
                                     data[0][ColumnNamesEnum().STATE],
                                     data[0][ColumnNamesEnum().ZIP_CODE])
            return True
        else:
            self.__init_person()
            return False

    def save(self):
        data = {ColumnNamesEnum().FIRST_NAME: self.first_name,
                ColumnNamesEnum().MIDDLE_NAME: self.middle_name,
                ColumnNamesEnum().LAST_NAME: self.last_name,
                ColumnNamesEnum().PREFIX_NAME: self.prefix_name,
                ColumnNamesEnum().SUFFIX_NAME: self.suffix_name,
                ColumnNamesEnum().PHONE_NUMBER: self.__phone_number,
                ColumnNamesEnum().STREET: self.address.street,
                ColumnNamesEnum().STREET2: self.address.street2,
                ColumnNamesEnum().CITY: self.address.city,
                ColumnNamesEnum().STATE: self.address.state,
                ColumnNamesEnum().ZIP_CODE: self.address.zip_code}
        self.__record_id = \
            PersonPlaceThingDB().save(TableNamesEnum().PERSON,
                                      self.__record_id, data)

    def delete(self, record_id=None):
        if record_id:
            PersonPlaceThingDB().delete(TableNamesEnum().PERSON, record_id)
        else:
            PersonPlaceThingDB().delete(TableNamesEnum().PERSON, self.record_id)
        self.__init_person()

    def __init_person(self):
        self.__record_id = None
        self.__record_id = RecordID().record_id
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.prefix_name = None
        self.suffix_name = None
        self.__phone_number = None
        self.__address = Address()

    def __format_name(self):
        name = self.prefix_name if self.prefix_name else ''
        name += (" " + self.first_name) if self.first_name else ''
        name += (" " + self.middle_name) if self.middle_name else ''
        name += (" " + self.last_name) if self.last_name else ''
        name += (" " + self.suffix_name) if self.suffix_name else ''
        return name

    def __is_phone_number_valid(self, phone_number):
        if phone_number:
            for character in phone_number:
                if not character.isnumeric() \
                        and character != "." \
                        and character != "-"\
                        and character != " ":
                    raise InvalidPhoneNumberError(PHONE_FORMAT_ERROR)
        return True

    def __str__(self):
        name = (self.prefix_name + " ") if self.prefix_name else ''
        name += (self.first_name + " ") if self.first_name else ''
        name += (self.middle_name + " ") if self.middle_name else ''
        name += (self.last_name + " ") if self.last_name else ''
        name += (self.suffix_name + " ") if self.suffix_name else ''
        lines = []
        if name != '':
            lines.append(name)
        if str(self.address) != '':
            lines.append(str(self.address))
        if self.phone_number:
            lines.append(self.phone_number)
        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
