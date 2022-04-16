from PPTBaseConnector import PPTBaseConnector
from Enums import TableNamesEnum, ColumnNamesEnum

# Actions can be tied to Events using the
# ActionEventConnector class


class ActionEventConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 action_event_description=None,
                 action_id=None,
                 event_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 action_event_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.ACTION_EVENT,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.ACTION_ID,
                         ColumnNamesEnum.EVENT_ID,
                         action_event_id,
                         action_id,
                         event_id,
                         relationship_type_id,
                         role_id,
                         action_event_description,
                         last_updated)

        self.action_id = action_id
        self.event_id = event_id
        self.action_event_id = action_event_id

    def get_action(self):
        return self._get_action(self.action_id)

    def get_event(self):
        return self._get_event(self.event_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.action_id
        self._record_id_right = self.event_id
        return_val = self._save()
        self.action_event_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_action_event()
        return return_val

    def load(self, action_event_id):
        self._load_ppt_base_connection_item(action_event_id)
        self.action_id = self._record_id_left
        self.event_id = self._record_id_right
        self.action_event_id = action_event_id

    def __init_action_event(self):
        self.action_id = None
        self.event_id = None
        self.action_event_id = None
        

# Actions can be tied to Places using the
# ActionPlaceConnector class


class ActionPlaceConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 action_place_description=None,
                 action_id=None,
                 place_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 action_place_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.ACTION_PLACE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.ACTION_ID,
                         ColumnNamesEnum.PLACE_ID,
                         action_place_id,
                         action_id,
                         place_id,
                         relationship_type_id,
                         role_id,
                         action_place_description,
                         last_updated)

        self.action_id = action_id
        self.place_id = place_id
        self.action_place_id = action_place_id

    def get_action(self):
        return self._get_action(self.action_id)

    def get_place(self):
        return self._get_place(self.place_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.action_id
        self._record_id_right = self.place_id
        return_val = self._save()
        self.action_place_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_action_place()
        return return_val

    def load(self, action_place_id):
        self._load_ppt_base_connection_item(action_place_id)
        self.action_id = self._record_id_left
        self.place_id = self._record_id_right
        self.action_place_id = action_place_id

    def __init_action_place(self):
        self.action_id = None
        self.place_id = None
        self.action_place_id = None
        

# Actions can be tied to other Actions using the
# ActionActionConnector class

class ActionActionConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 action_action_description=None,
                 action_id_a=None,
                 action_id_b=None,
                 role_id=None,
                 relationship_type_id=None,
                 action_action_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.ACTION_ACTION,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.ACTION_ID_A,
                         ColumnNamesEnum.ACTION_ID_B,
                         action_action_id,
                         action_id_a,
                         action_id_b,
                         relationship_type_id,
                         role_id,
                         action_action_description,
                         last_updated)

        self.action_id_a = action_id_a
        self.action_id_b = action_id_b
        self.action_action_id = action_action_id

    def get_action_left(self):
        return self._get_action(self.action_id_a)

    def get_action_right(self):
        return self._get_action(self.action_id_b)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.action_id_a
        self._record_id_right = self.action_id_b
        return_val = self._save()
        self.action_action_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_action_action()
        return return_val

    def load(self, action_action_id):
        self._load_ppt_base_connection_item(action_action_id)
        self.action_id_a = self._record_id_left
        self.action_id_b = self._record_id_right
        self.action_action_id = action_action_id

    def __init_action_action(self):
        self.action_id_a = None
        self.action_id_b = None
        self.action_action_id = None
