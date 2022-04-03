from Address import Address
from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from Constants import PHONE_FORMAT_ERROR, DatabaseResult, \
    ERROR_DELETING_RECORD, NOTHING_TO_DELETE, RECORD_LOADED, \
    ERROR_LOADING_RECORD, RECORD_NOT_FOUND, \
    ERROR_SAVING_RECORD, PERSON_NAME_VALIDATION_ERROR, NULL_RECORD_ID
from Enums import TableNamesEnum, ColumnNamesEnum


class Person:
    def __init__(self, data_saved_callback_func=None,
                 invalid_data_callback_func=None,
                 record_id=None, last_updated=None,
                 first_name=None, middle_name=None, last_name=None,
                 prefix_name=None, suffix_name=None,
                 phone_number=None, street=None, street2=None,
                 city=None, state=None, zip_code=None, tags=None):
        self.__data_saved_callback_func = data_saved_callback_func
        self.__invalid_data_callback_func = invalid_data_callback_func
        self.__record_id = RecordID(record_id).record_id
        self.__last_updated = last_updated
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.prefix_name = prefix_name
        self.suffix_name = suffix_name
        self.__phone_number = phone_number
        self.__address = Address(invalid_data_callback_func,
                                 street, street2, city, state, zip_code)
        self.__tags = tags
        if not self.__tags:
            self.__tags = list()
        elif not isinstance(self.__tags, list):
            self.__tags = list()
        self.__person_events = None

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
    def tags(self):
        return self.tags

    def add_tags(self, *args):
        if not isinstance(self.__tags, list):
            self.__tags = list()
        for arg in args:
            if not isinstance(arg, list):
                self.__tags.append(str(arg).lower())
            else:
                lower_case_tags = map(lambda x: x.lower(), arg)
                self.__tags.extend(list(lower_case_tags))

    def remove_tag(self, tag):
        if not isinstance(self.__tags, list):
            self.__tags = list()
        else:
            if self.__tags.count(tag) > 0:
                self.__tags = \
                    list(filter(lambda val: val != tag,
                                self.__tags))

    def add_role(self, role_id):
        pass

    def load(self, record_id):
        data = PersonPlaceThingDB().read(TableNamesEnum.PERSON, {}, record_id)
        if len(data) == 1:
            self.__record_id = record_id
            self.first_name = data[0][ColumnNamesEnum.FIRST_NAME]
            self.middle_name = data[0][ColumnNamesEnum.MIDDLE_NAME]
            self.last_name = data[0][ColumnNamesEnum.LAST_NAME]
            self.prefix_name = data[0][ColumnNamesEnum.PREFIX_NAME]
            self.suffix_name = data[0][ColumnNamesEnum.SUFFIX_NAME]
            self.__phone_number = data[0][ColumnNamesEnum.PHONE_NUMBER]
            self.__address = Address(self.__invalid_data_callback_func,
                                     data[0][ColumnNamesEnum.STREET],
                                     data[0][ColumnNamesEnum.STREET2],
                                     data[0][ColumnNamesEnum.CITY],
                                     data[0][ColumnNamesEnum.STATE],
                                     data[0][ColumnNamesEnum.ZIP_CODE])
            self.__tags = data[0][ColumnNamesEnum.TAGS]
            self.__last_updated = data[0][ColumnNamesEnum.LAST_UPDATED]

            return DatabaseResult(True, self.__record_id,
                                  TableNamesEnum.PERSON
                                  + " " + RECORD_LOADED, "")
        else:
            return DatabaseResult(False, self.__record_id,
                                  ERROR_LOADING_RECORD,
                                  TableNamesEnum.PERSON
                                  + " " + RECORD_NOT_FOUND)

    def save(self):
        if (self.first_name and self.first_name.strip() != '') \
                    and (self.last_name and self.last_name.strip() != ''):

            data = {ColumnNamesEnum.FIRST_NAME: self.first_name,
                    ColumnNamesEnum.MIDDLE_NAME: self.middle_name,
                    ColumnNamesEnum.LAST_NAME: self.last_name,
                    ColumnNamesEnum.PREFIX_NAME: self.prefix_name,
                    ColumnNamesEnum.SUFFIX_NAME: self.suffix_name,
                    ColumnNamesEnum.PHONE_NUMBER: self.__phone_number,
                    ColumnNamesEnum.STREET: self.address.street,
                    ColumnNamesEnum.STREET2: self.address.street2,
                    ColumnNamesEnum.CITY: self.address.city,
                    ColumnNamesEnum.STATE: self.address.state,
                    ColumnNamesEnum.ZIP_CODE: self.address.zip_code,
                    ColumnNamesEnum.TAGS: self.__tags}

            return_val = PersonPlaceThingDB().save(TableNamesEnum.PERSON,
                                                   self.__record_id,
                                                   self.__last_updated, data)
            if return_val.succeeded:
                self.__fire_data_saved_callback_func(return_val.record_id,
                                                     return_val.message)
                self.load(return_val.record_id)
            else:
                if return_val.error.count("person_name_constraint") > 0:
                    error_message = "Person with name " \
                        f"{self.first_name} {self.middle_name} {self.last_name} " \
                        "already exists in the database."
                else:
                    error_message = return_val.error

                self.__fire_invalid_data_callback_func(return_val.record_id,
                                                       return_val.message
                                                       + ": " +
                                                       error_message)

            return return_val
        else:
            self.__fire_invalid_data_callback_func(
                self.record_id, PERSON_NAME_VALIDATION_ERROR)
            return DatabaseResult(False, self.record_id,
                                  ERROR_SAVING_RECORD,
                                  PERSON_NAME_VALIDATION_ERROR)

    def delete(self):
        if self.record_id and self.record_id != NULL_RECORD_ID:
            return_val = PersonPlaceThingDB().delete(TableNamesEnum.PERSON,
                                                     self.record_id)
            if return_val.succeeded:
                self.__fire_data_saved_callback_func(return_val.record_id,
                                                     return_val.message)
            return return_val
        else:
            self.__fire_invalid_data_callback_func(self.record_id,
                                                   ERROR_DELETING_RECORD
                                                   + ": " +
                                                   NOTHING_TO_DELETE)
            return DatabaseResult(False, self.record_id,
                                  ERROR_DELETING_RECORD, NOTHING_TO_DELETE)

    def __init_person(self):
        self.__record_id = None
        self.__record_id = NULL_RECORD_ID
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.prefix_name = None
        self.suffix_name = None
        self.__phone_number = None
        self.__address = Address(self.__invalid_data_callback_func)
        self.__tags = list()
        self.__last_updated = None

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
                    self.__fire_invalid_data_callback_func(
                        self.record_id, PHONE_FORMAT_ERROR)
                    return False
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
        if len(self.__tags) > 0:
            lines.append(",".join(self.__tags))
        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''

    def __fire_data_saved_callback_func(self, record_id, message):
        if self.__data_saved_callback_func:
            self.__data_saved_callback_func(table_name=TableNamesEnum.PERSON,
                                            record_id=record_id,
                                            message=message)

    def __fire_invalid_data_callback_func(self, record_id, message):
        if self.__invalid_data_callback_func:
            self.__invalid_data_callback_func(table_name=TableNamesEnum.PERSON,
                                              record_id=record_id,
                                              message=message)
