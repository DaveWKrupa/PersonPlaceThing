from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import ColumnNamesEnum
from RecordID import RecordID


class TableConnector:
    def __init__(self, table_name,
                 record_id_left_name, record_id_right_name=None,
                 connector_table_id=None,
                 record_id_left=None,
                 record_id_right=None,
                 relationship_type_id=None,
                 role_id=None,
                 person_event_description=None,
                 relationship_type_short_description=None):
        self._table_name = table_name
        self._record_id_left_name = record_id_left_name
        self._record_id_right_name = record_id_right_name
        self._connector_table_id = RecordID(connector_table_id).record_id
        self.record_id_left = record_id_left
        self.record_id_right = record_id_right
        self.relationship_type_id = relationship_type_id
        self.role_id = role_id
        self.person_event_description = person_event_description
        self.relationship_type_short_description = relationship_type_short_description

    def _save(self):
        if not self._record_id_right_name:
            # the person_role table has one less column than the others
            data = {self.record_id_left: self.record_id_left,
                    ColumnNamesEnum.RELATIONSHIP_TYPE_ID: self.relationship_type_id,
                    ColumnNamesEnum.DESCRIPTION: self.person_event_description,
                    ColumnNamesEnum.ROLE_ID: self.role_id}
        else:
            data = {self.record_id_left: self.record_id_left,
                    self._record_id_right_name: self.record_id_right,
                    ColumnNamesEnum.RELATIONSHIP_TYPE_ID: self.relationship_type_id,
                    ColumnNamesEnum.DESCRIPTION: self.person_event_description,
                    ColumnNamesEnum.ROLE_ID: self.role_id}

        return PersonPlaceThingDB().save(self._table_name,
                                         self._connector_table_id, data)

    def _delete(self):
        return PersonPlaceThingDB().delete(self._table_name, self._connector_table_id)

