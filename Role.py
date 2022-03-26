from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum


class Role:
    def __init__(self, record_id=None, description=None):
        self.__record_id = RecordID(record_id).record_id
        self.description = description

    @property
    def record_id(self):
        return self.__record_id

    def load(self, record_id):
        data = PersonPlaceThingDB().read(TableNamesEnum().ROLE, {}, str(record_id))
        if len(data) == 1:
            self.__record_id = record_id
            self.description = data[0][ColumnNamesEnum().DESCRIPTION]

            return True
        else:
            self.__init_thing()
            return False

    def save(self):
        data = {ColumnNamesEnum().DESCRIPTION: self.description}
        self.__record_id = \
            PersonPlaceThingDB().save(TableNamesEnum().ROLE,
                                      self.__record_id, data)

    def delete(self, record_id=None):
        if record_id:
            PersonPlaceThingDB().delete(TableNamesEnum().ROLE, record_id)
        else:
            PersonPlaceThingDB().delete(TableNamesEnum().ROLE, self.record_id)
        self.__init_thing()

    def __init_thing(self):
        self.__record_id = None
        self.__record_id = RecordID().record_id
        self.description = None

    def __str__(self):
        return self.description
