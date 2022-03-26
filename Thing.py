from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum


class Thing:
    def __init__(self, record_id=None,
                 short_description=None, long_description=None):
        self.__record_id = RecordID(record_id).record_id
        self.short_description = short_description
        self.long_description = long_description

    @property
    def record_id(self):
        return self.__record_id

    def load(self, record_id):
        data = PersonPlaceThingDB().read(TableNamesEnum().THING, str(record_id))
        if len(data) == 1:
            self.__record_id = record_id
            self.short_description = data[0][ColumnNamesEnum().SHORT_DESCRIPTION]
            self.long_description = data[0][ColumnNamesEnum().LONG_DESCRIPTION]

            return True
        else:
            self.__init_thing()
            return False

    def save(self):
        data = {ColumnNamesEnum().SHORT_DESCRIPTION: self.short_description,
                ColumnNamesEnum().LONG_DESCRIPTION: self.long_description}
        self.__record_id = \
            PersonPlaceThingDB().save(TableNamesEnum().THING,
                                      self.__record_id, data)

    def delete(self, record_id=None):
        if record_id:
            PersonPlaceThingDB().delete(TableNamesEnum().THING, record_id)
        else:
            PersonPlaceThingDB().delete(TableNamesEnum().THING, self.record_id)
        self.__init_thing()

    def __init_thing(self):
        self.__record_id = None
        self.__record_id = RecordID().record_id
        self.short_description = None
        self.long_description = None

    def __str__(self):
        lines = []
        if self.short_description != '':
            lines.append(self.short_description)
        if self.long_description != '':
            lines.append(self.long_description)

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
