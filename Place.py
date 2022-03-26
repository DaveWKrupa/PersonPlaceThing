from Address import Address
from RecordID import RecordID
from CustomExceptions import InvalidPhoneNumberError
from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum
from Constants import PHONE_FORMAT_ERROR


class Place:
    def __init__(self, record_id=None,
                 short_description=None, long_description=None,
                 phone_number=None, street=None, street2=None,
                 city=None, state=None, zipcode=None):
        self.__record_id = RecordID(record_id).record_id
        self.short_description = short_description
        self.long_description = long_description
        self.__phone_number = phone_number
        self.__address = Address(street, street2, city, state, zipcode)

    @property
    def record_id(self):
        return self.__record_id

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
        data = PersonPlaceThingDB().read(TableNamesEnum().PLACE, {}, record_id)
        if len(data) == 1:
            self.__record_id = record_id
            self.short_description = data[0][ColumnNamesEnum().SHORT_DESCRIPTION]
            self.long_description = data[0][ColumnNamesEnum().LONG_DESCRIPTION]
            self.__phone_number = data[0][ColumnNamesEnum().PHONE_NUMBER]
            self.__address = Address(data[0][ColumnNamesEnum().STREET],
                                     data[0][ColumnNamesEnum().STREET2],
                                     data[0][ColumnNamesEnum().CITY],
                                     data[0][ColumnNamesEnum().STATE],
                                     data[0][ColumnNamesEnum().ZIP_CODE])
            return True
        else:
            self.__init_place()
            return False

    def save(self):
        data = {ColumnNamesEnum().SHORT_DESCRIPTION: self.short_description,
                ColumnNamesEnum().LONG_DESCRIPTION: self.long_description,
                ColumnNamesEnum().PHONE_NUMBER: self.__phone_number,
                ColumnNamesEnum().STREET: self.address.street,
                ColumnNamesEnum().STREET2: self.address.street2,
                ColumnNamesEnum().CITY: self.address.city,
                ColumnNamesEnum().STATE: self.address.state,
                ColumnNamesEnum().ZIP_CODE: self.address.zip_code}
        self.__record_id = \
            PersonPlaceThingDB().save(TableNamesEnum().PLACE,
                                      self.__record_id, data)

    def delete(self, record_id=None):
        if record_id:
            PersonPlaceThingDB().delete(TableNamesEnum().PLACE, record_id)
        else:
            PersonPlaceThingDB().delete(TableNamesEnum().PLACE, self.record_id)
        self.__init_place()

    def __init_place(self):
        self.__record_id = None
        self.__record_id = RecordID().record_id
        self.short_description = None
        self.long_description = None
        self.__phone_number = None
        self.__address = Address()

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
        lines = []
        if self.short_description != '':
            lines.append(self.short_description)
        if self.long_description != '':
            lines.append(self.long_description)
        if str(self.address) != '':
            lines.append(str(self.address))
        if self.phone_number != '':
            lines.append(self.phone_number)
        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
