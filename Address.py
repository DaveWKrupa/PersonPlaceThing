from CustomExceptions import InvalidZipCodeError
from Constants import ZIP_CODE_FORMAT_ERROR


class Address:
    def __init__(self, street=None, street2=None,
                 city=None, state=None, zip_code=None):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.__zip_code = None
        self.zip_code = zip_code  # this will validate as set

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        if value and value.strip() != '':
            for character in value:
                if not character.isnumeric() \
                        and character != "-":
                    raise InvalidZipCodeError(ZIP_CODE_FORMAT_ERROR)
                else:
                    self.__zip_code = value

    def __str__(self):
        lines = []
        if self.street:
            lines.append(self.street)
        if self.street2:
            lines.append(self.street2)
        city_state_zip = self.city if self.city else ''
        city_state_zip += ", " if (self.city
                                   and self.state
                                   and self.zip_code) else ''
        city_state_zip += self.state if self.state else ''
        city_state_zip += " " if city_state_zip else ''
        city_state_zip += self.zip_code if self.zip_code else ''
        if city_state_zip != '':
            lines.append(city_state_zip)

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
