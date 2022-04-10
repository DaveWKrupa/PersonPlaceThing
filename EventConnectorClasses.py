from PPTBaseConnector import PPTBaseConnector
from Enums import TableNamesEnum, ColumnNamesEnum


class EventPlaceConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 event_place_description=None,
                 event_id=None,
                 place_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 event_place_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.EVENT_PLACE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.EVENT_ID,
                         ColumnNamesEnum.PLACE_ID,
                         event_place_id,
                         event_id,
                         place_id,
                         relationship_type_id,
                         role_id,
                         event_place_description,
                         last_updated)

        self.event_id = event_id
        self.place_id = place_id
        self.event_place_id = event_place_id

    def get_event(self):
        return self._get_event(self.event_id)

    def get_place(self):
        return self._get_place(self.place_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.event_id
        self._record_id_right = self.place_id
        return_val = self._save()
        self.event_place_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_event_place()
        return return_val

    def load(self, event_place_id):
        self._load_ppt_base_connection_item(event_place_id)
        self.event_id = self._record_id_left
        self.place_id = self._record_id_right
        self.event_place_id = event_place_id

    def __init_event_place(self):
        self.event_id = None
        self.place_id = None
        self.event_place_id = None


class EventEventConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 event_event_description=None,
                 event_id_a=None,
                 event_id_b=None,
                 role_id=None,
                 relationship_type_id=None,
                 event_event_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.EVENT_EVENT,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.EVENT_ID_A,
                         ColumnNamesEnum.EVENT_ID_B,
                         event_event_id,
                         event_id_a,
                         event_id_b,
                         relationship_type_id,
                         role_id,
                         event_event_description,
                         last_updated)

        self.event_id_a = event_id_a
        self.event_id_b = event_id_b
        self.event_event_id = event_event_id

    def get_event_left(self):
        return self._get_event(self.event_id_a)

    def get_event_right(self):
        return self._get_event(self.event_id_b)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.event_id_a
        self._record_id_right = self.event_id_b
        return_val = self._save()
        self.event_event_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_event_event()
        return return_val

    def load(self, event_event_id):
        self._load_ppt_base_connection_item(event_event_id)
        self.event_id_a = self._record_id_left
        self.event_id_b = self._record_id_right
        self.event_event_id = event_event_id

    def __init_event_event(self):
        self.event_id_a = None
        self.event_id_b = None
        self.event_event_id = None
