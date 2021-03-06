from Address import Address
from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum
from Constants import ERROR_DELETING_RECORD, NOTHING_TO_DELETE, \
    RECORD_LOADED, ERROR_LOADING_RECORD, \
    SHORT_DESCRIPTION_VALIDATION_ERROR, \
    ERROR_SAVING_RECORD, PHONE_FORMAT_ERROR, \
    RECORD_NOT_FOUND, NULL_RECORD_ID, DatabaseResult

# The Place class used to describe locations.


class Place:
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_fun,
                 record_id=None, last_updated=None,
                 short_description=None, long_description=None,
                 phone_number=None, street=None, street2=None,
                 city=None, state=None, zip_code=None, tags=None):
        self.__data_saved_callback_func = data_saved_callback_func
        self.__invalid_data_callback_func = invalid_data_callback_fun
        self.__record_id = RecordID(record_id).record_id
        self.__last_updated = last_updated
        self.short_description = short_description
        self.long_description = long_description
        self.__phone_number = phone_number
        self.__address = Address(self.invalid_data_callback_func,
                                 street, street2, city, state, zip_code)
        self.__tags = tags
        if not self.__tags:
            self.__tags = list()
        elif not isinstance(self.__tags, list):
            self.__tags = list()

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

    def load(self, record_id):
        data = PersonPlaceThingDB().read(TableNamesEnum.PLACE, {}, record_id)
        if len(data) == 1:
            self.__record_id = record_id
            self.short_description = data[0][ColumnNamesEnum.SHORT_DESCRIPTION]
            self.long_description = data[0][ColumnNamesEnum.LONG_DESCRIPTION]
            self.__phone_number = data[0][ColumnNamesEnum.PHONE_NUMBER]
            self.__address = Address(self.invalid_data_callback_func,
                                     data[0][ColumnNamesEnum.STREET],
                                     data[0][ColumnNamesEnum.STREET2],
                                     data[0][ColumnNamesEnum.CITY],
                                     data[0][ColumnNamesEnum.STATE],
                                     data[0][ColumnNamesEnum.ZIP_CODE])
            self.__tags = data[0][ColumnNamesEnum.TAGS]
            self.__last_updated = data[0][ColumnNamesEnum.LAST_UPDATED]

            return DatabaseResult(True, self.__record_id, RECORD_LOADED, "")
        else:
            return DatabaseResult(False, self.__record_id,
                                  ERROR_LOADING_RECORD,
                                  TableNamesEnum.PLACE + " " +
                                  RECORD_NOT_FOUND)

    def save(self):
        if self.short_description and self.short_description.strip() != '':
            data = {ColumnNamesEnum.SHORT_DESCRIPTION: self.short_description,
                    ColumnNamesEnum.LONG_DESCRIPTION: self.long_description,
                    ColumnNamesEnum.PHONE_NUMBER: self.__phone_number,
                    ColumnNamesEnum.STREET: self.address.street,
                    ColumnNamesEnum.STREET2: self.address.street2,
                    ColumnNamesEnum.CITY: self.address.city,
                    ColumnNamesEnum.STATE: self.address.state,
                    ColumnNamesEnum.ZIP_CODE: self.address.zip_code,
                    ColumnNamesEnum.TAGS: self.__tags}

            return_val = PersonPlaceThingDB().save(TableNamesEnum.PLACE,
                                                   self.__record_id,
                                                   self.__last_updated,
                                                   data)

            if return_val.succeeded:
                self.__fire_data_saved_callback_func(return_val.record_id,
                                                     return_val.message)
                self.load(return_val.record_id)
            else:
                if return_val.error.count(
                        "place_short_desc_address_constraint") > 0:
                    error_message = "Place with short description" \
                                    " and address already " \
                                    "exists in the database.\n" \
                                    f"{self.short_description}\n" \
                                    f"{str(self.address)} " \

                else:
                    error_message = return_val.error

                self.__fire_invalid_data_callback_func(return_val.record_id,
                                                       return_val.message
                                                       + ": " +
                                                       error_message)

            return return_val
        else:
            self.__fire_invalid_data_callback_func(
                self.record_id, SHORT_DESCRIPTION_VALIDATION_ERROR)
            return DatabaseResult(False, self.record_id,
                                  ERROR_SAVING_RECORD,
                                  SHORT_DESCRIPTION_VALIDATION_ERROR)

    def delete(self):
        if self.record_id and self.record_id != NULL_RECORD_ID:
            return_val = PersonPlaceThingDB().delete(
                TableNamesEnum.PLACE, self.record_id)
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

    def __init_place(self):
        self.__record_id = None
        self.__record_id = RecordID().record_id
        self.short_description = None
        self.long_description = None
        self.__phone_number = None
        self.__address = Address()
        self.__last_updated = None

    def __is_phone_number_valid(self, phone_number):
        if phone_number:
            for character in phone_number:
                if not character.isnumeric() \
                        and character != "." \
                        and character != "-"\
                        and character != " ":
                    self.__fire_invalid_data_callback_func(self.record_id,
                                                           PHONE_FORMAT_ERROR)
                    return False

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
        if len(self.__tags) > 0:
            lines.append(",".join(self.__tags))
        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''

    def __fire_data_saved_callback_func(self, record_id, message):
        if self.__data_saved_callback_func:
            self.__data_saved_callback_func(table_name=TableNamesEnum.PLACE,
                                            record_id=record_id,
                                            message=message)

    def __fire_invalid_data_callback_func(self, record_id, message):
        if self.__invalid_data_callback_func:
            self.__invalid_data_callback_func(table_name=TableNamesEnum.PLACE,
                                              record_id=record_id,
                                              message=message)

    def invalid_data_callback_func(self, **kwargs):
        for k, v in kwargs.items():
            if k == "message":
                self.__fire_invalid_data_callback_func(self.record_id, v)
                break


