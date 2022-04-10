from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import ColumnNamesEnum
from RecordID import RecordID
from Constants import ERROR_LOADING_RECORD, NOTHING_TO_DELETE, \
    ERROR_DELETING_RECORD, RECORD_NOT_FOUND, \
    RECORD_LOADED, RECORD_SAVED, NULL_RECORD_ID, DatabaseResult
from Person import Person
from Event import Event
from Action import Action
from Place import Place
from Role import Role
from Thing import Thing
from RelationshipType import RelationshipType


class PPTBaseConnector:
    def __init__(self, table_name,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 record_id_left_name=None,
                 record_id_right_name=None,
                 connector_table_id=None,
                 record_id_left=None,
                 record_id_right=None,
                 relationship_type_id=None,
                 role_id=None,
                 description=None,
                 last_updated=None):
        self._table_name = table_name
        self._data_saved_callback_func = data_saved_callback_func
        self._invalid_data_callback_func = invalid_data_callback_func
        self._record_id_left_name = record_id_left_name
        self._record_id_right_name = record_id_right_name
        self._connector_table_id = RecordID(connector_table_id).record_id
        self._record_id_left = record_id_left
        self._record_id_right = record_id_right
        self.relationship_type_id = relationship_type_id
        self.role_id = role_id
        self.description = description
        self._last_updated = last_updated

    def _get_person(self, person_id):
        person = Person(self._data_saved_callback_func,
                        self._invalid_data_callback_func)
        person.load(person_id)
        return person

    def _get_event(self, event_id):
        event = Event(self._data_saved_callback_func,
                      self._invalid_data_callback_func)
        event.load(event_id)
        return event

    def _get_action(self, action_id):
        action = Action(self._data_saved_callback_func,
                        self._invalid_data_callback_func)
        action.load(action_id)
        return action

    def _get_thing(self, thing_id):
        thing = Thing(self._data_saved_callback_func,
                      self._invalid_data_callback_func)
        thing.load(thing_id)
        return thing

    def _get_place(self, place_id):
        place = Place(self._data_saved_callback_func,
                      self._invalid_data_callback_func)
        place.load(place_id)
        return place

    def _get_role(self, role_id):
        role = Role(self._data_saved_callback_func,
                    self._invalid_data_callback_func)
        role.load(role_id)
        return role

    def _get_relationship_type(self, relationship_type_id):
        relationship_type = \
            RelationshipType(self._data_saved_callback_func,
                             self._invalid_data_callback_func)
        relationship_type.load(relationship_type_id)
        return relationship_type

    def _init_ppt_base_connector_item(self):
        self._connector_table_id = None
        self._record_id_left = None
        self._record_id_right = None
        self.relationship_type_id = None
        self.role_id = None
        self.description = None
        self._last_updated = None

    def _save(self):
        if not self._record_id_right_name:
            # the person_role table has one less column than the others
            data = {self._record_id_left_name: self._record_id_left,
                    ColumnNamesEnum.RELATIONSHIP_TYPE_ID: self.relationship_type_id,
                    ColumnNamesEnum.DESCRIPTION: self.description,
                    ColumnNamesEnum.ROLE_ID: self.role_id}
        else:
            data = {self._record_id_left_name: self._record_id_left,
                    self._record_id_right_name: self._record_id_right,
                    ColumnNamesEnum.RELATIONSHIP_TYPE_ID: self.relationship_type_id,
                    ColumnNamesEnum.DESCRIPTION: self.description,
                    ColumnNamesEnum.ROLE_ID: self.role_id}

        return_val = PersonPlaceThingDB().save(self._table_name,
                                               self._connector_table_id,
                                               self._last_updated, data)

        if return_val.succeeded:
            # reload the base item data
            self._load_ppt_base_connection_item(return_val.record_id)
            self._fire_data_saved_callback_func(self._table_name
                                                    + ": " + RECORD_SAVED)
        elif not data:
            self._fire_invalid_data_callback_func(self._table_name
                                                  + ": " + return_val.message +
                                                  " " + return_val.error)

        return return_val

    def _delete(self):
        if self._connector_table_id and self._connector_table_id != NULL_RECORD_ID:
            return_val = \
                PersonPlaceThingDB().delete(self._table_name, self._connector_table_id)
            if return_val.succeeded:
                self._fire_data_saved_callback_func(return_val.message)
                self._init_ppt_base_connector_item()
            else:
                self._fire_invalid_data_callback_func(return_val.message
                                                      + " " +
                                                      return_val.error)
            return return_val
        else:
            self._fire_invalid_data_callback_func(ERROR_DELETING_RECORD
                                                  + " " +
                                                  NOTHING_TO_DELETE)
            return DatabaseResult(False, self._connector_table_id,
                                  ERROR_DELETING_RECORD, NOTHING_TO_DELETE)

    def _load_ppt_base_connection_item(self, record_id):
        data = PersonPlaceThingDB().read(self._table_name, {}, record_id)
        if len(data) == 1:
            self._connector_table_id = record_id
            self.description = \
                data[0][ColumnNamesEnum.DESCRIPTION]

            self._record_id_left = data[0][self._record_id_left_name]
            if self._record_id_right_name in data[0]:
                self._record_id_right = data[0][self._record_id_right_name]

            self.relationship_type_id = data[0][ColumnNamesEnum.RELATIONSHIP_TYPE_ID]
            self.role_id = data[0][ColumnNamesEnum.ROLE_ID]
            self._last_updated = data[0][ColumnNamesEnum.LAST_UPDATED]
            return DatabaseResult(True, self._connector_table_id, RECORD_LOADED, "")
        else:
            self._fire_invalid_data_callback_func(RECORD_NOT_FOUND
                                                  + " " + self._table_name
                                                  + " " + RECORD_NOT_FOUND)
            self._init_ppt_base_connector_item()
            return DatabaseResult(False, self._connector_table_id,
                                  ERROR_LOADING_RECORD,
                                  self._table_name + " " +
                                  RECORD_NOT_FOUND)

    def _fire_data_saved_callback_func(self, message):
        if self._data_saved_callback_func:
            self._data_saved_callback_func(table_name=self._table_name,
                                            record_id=self._connector_table_id,
                                            message=message)

    def _fire_invalid_data_callback_func(self, message):
        if self._invalid_data_callback_func:
            self._invalid_data_callback_func(table_name=self._table_name,
                                              record_id=self._connector_table_id,
                                              message=message)
