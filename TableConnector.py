from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum
from RecordID import RecordID


class TableConnector:
    def __init__(self, table_name, record_id=None,
                 record_id_left=None, record_id_right=None,
                 relationship_type_id=None, role_id=None, description=None):
        self._table_name = table_name
        self._record_id = RecordID(record_id).record_id
        # The record ids passed in should follow the table name pattern
        # e.g. for person_action connector table
        # self._record_id_left = person_id
        # self._record_id_right = action_id
        self._record_id_left = record_id_left
        self._record_id_right = record_id_right
        self.relationship_type_id = relationship_type_id
        self.description = description
        self.role_id = role_id

    def save(self):
        record_id_left_name, record_id_right_name = self.__get_record_id_names()
        if self._table_name == TableNamesEnum().PERSON_ROLE:
            # the person_role table has one less column than the others
            data = {record_id_left_name: self._record_id_left,
                    ColumnNamesEnum().RELATIONSHIP_TYPE_ID: self.relationship_type_id,
                    ColumnNamesEnum().DESCRIPTION: self.description,
                    ColumnNamesEnum().ROLE_ID: self.role_id}
        else:
            data = {record_id_left_name: self._record_id_left,
                    record_id_right_name: self._record_id_right,
                    ColumnNamesEnum().RELATIONSHIP_TYPE_ID: self.relationship_type_id,
                    ColumnNamesEnum().DESCRIPTION: self.description,
                    ColumnNamesEnum().ROLE_ID: self.role_id}
        self._record_id = \
            PersonPlaceThingDB().save(self._table_name,
                                      self._record_id, data)

    def load(self, table_name, record_id):
        record_id_left_name, record_id_right_name = self.__get_record_id_names()
        data = PersonPlaceThingDB().read(table_name, {}, record_id)
        if len(data) == 1:
            self._record_id = record_id
            self._table_name = table_name
            self._record_id_left = data[0][record_id_left_name]
            if self._table_name != TableNamesEnum().PERSON_ROLE:
                # don't set this for Person_Role table
                self._record_id_right = data[0][record_id_right_name]
            self.relationship_type_id = data[0][ColumnNamesEnum().RELATIONSHIP_TYPE_ID]
            self.description = data[0][ColumnNamesEnum().DESCRIPTION]
            self.role_id = data[0][ColumnNamesEnum().ROLE_ID]

            return True
        else:
            self.__init_table_connector()
            return False

    def __init_table_connector(self):
        self._record_id = None
        self._table_name = None
        self._record_id_left = None
        self._record_id_right = None
        self.relationship_type_id = None
        self.description = None
        self.role_id = None

    def __get_record_id_names(self):
        if self._table_name == TableNamesEnum().ACTION_ACTION:
            return ColumnNamesEnum().ACTION_ID_A, \
                   ColumnNamesEnum().ACTION_ID_B
        elif self._table_name == TableNamesEnum().ACTION_EVENT:
            return ColumnNamesEnum().ACTION_ID, ColumnNamesEnum().EVENT_ID
        elif self._table_name == TableNamesEnum().ACTION_PLACE:
            return ColumnNamesEnum().ACTION_ID, ColumnNamesEnum().PLACE_ID
        elif self._table_name == TableNamesEnum().EVENT_EVENT:
            return ColumnNamesEnum().EVENT_ID_A, ColumnNamesEnum().EVENT_ID_B
        elif self._table_name == TableNamesEnum().EVENT_PLACE:
            return ColumnNamesEnum().EVENT_ID, ColumnNamesEnum().PLACE_ID
        elif self._table_name == TableNamesEnum().PERSON_ACTION:
            return ColumnNamesEnum().PERSON_ID, ColumnNamesEnum().ACTION_ID
        elif self._table_name == TableNamesEnum().PERSON_EVENT:
            return ColumnNamesEnum().PERSON_ID, ColumnNamesEnum().EVENT_ID
        elif self._table_name == TableNamesEnum().PERSON_PERSON:
            return ColumnNamesEnum().PERSON_ID_A, \
                   ColumnNamesEnum().PERSON_ID_B
        elif self._table_name == TableNamesEnum().PERSON_PLACE:
            return ColumnNamesEnum().PERSON_ID, ColumnNamesEnum().PLACE_ID
        elif self._table_name == TableNamesEnum().PERSON_THING:
            return ColumnNamesEnum().PERSON_ID, ColumnNamesEnum().THING_ID
        elif self._table_name == TableNamesEnum().PERSON_ROLE:
            # role_id already available as record id
            return ColumnNamesEnum().PERSON_ID, None
        elif self._table_name == TableNamesEnum().PLACE_PLACE:
            return ColumnNamesEnum().PLACE_ID_A, ColumnNamesEnum().PLACE_ID_B
        elif self._table_name == TableNamesEnum().THING_ACTION:
            return ColumnNamesEnum().THING_ID, ColumnNamesEnum().ACTION_ID
        elif self._table_name == TableNamesEnum().THING_EVENT:
            return ColumnNamesEnum().THING_ID, ColumnNamesEnum().EVENT_ID
        elif self._table_name == TableNamesEnum().THING_PLACE:
            return ColumnNamesEnum().THING_ID, ColumnNamesEnum().PLACE_ID
        elif self._table_name == TableNamesEnum().THING_THING:
            return ColumnNamesEnum().THING_ID_A, ColumnNamesEnum().THING_ID_B


