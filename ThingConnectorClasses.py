from PPTBaseConnector import PPTBaseConnector
from Enums import TableNamesEnum, ColumnNamesEnum

# A Thing can be connected to an Event
# using the ThingEventConnector class


class ThingEventConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 thing_event_description=None,
                 thing_id=None,
                 event_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 thing_event_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.THING_EVENT,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.THING_ID,
                         ColumnNamesEnum.EVENT_ID,
                         thing_event_id,
                         thing_id,
                         event_id,
                         relationship_type_id,
                         role_id,
                         thing_event_description,
                         last_updated)

        self.thing_id = thing_id
        self.event_id = event_id
        self.thing_event_id = thing_event_id

    def get_thing(self):
        return self._get_thing(self.thing_id)

    def get_event(self):
        return self._get_event(self.event_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.thing_id
        self._record_id_right = self.event_id
        return_val = self._save()
        self.thing_event_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_thing_event()
        return return_val

    def load(self, thing_event_id):
        self._load_ppt_base_connection_item(thing_event_id)
        self.thing_id = self._record_id_left
        self.event_id = self._record_id_right
        self.thing_event_id = thing_event_id

    def __init_thing_event(self):
        self.thing_id = None
        self.event_id = None
        self.thing_event_id = None

# A Thing can be connected to an Action
# using the ThingActionConnector class


class ThingActionConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 thing_action_description=None,
                 thing_id=None,
                 action_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 thing_action_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.THING_ACTION,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.THING_ID,
                         ColumnNamesEnum.ACTION_ID,
                         thing_action_id,
                         thing_id,
                         action_id,
                         relationship_type_id,
                         role_id,
                         thing_action_description,
                         last_updated)

        self.thing_id = thing_id
        self.action_id = action_id
        self.thing_action_id = thing_action_id

    def get_thing(self):
        return self._get_thing(self.thing_id)

    def get_action(self):
        return self._get_action(self.action_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.thing_id
        self._record_id_right = self.action_id
        return_val = self._save()
        self.thing_action_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_thing_action()
        return return_val

    def load(self, thing_action_id):
        self._load_ppt_base_connection_item(thing_action_id)
        self.thing_id = self._record_id_left
        self.action_id = self._record_id_right
        self.thing_action_id = thing_action_id

    def __init_thing_action(self):
        self.thing_id = None
        self.action_id = None
        self.thing_action_id = None

# A Thing can be connected to a Place
# using the ThingPlaceConnector class


class ThingPlaceConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 thing_place_description=None,
                 thing_id=None,
                 place_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 thing_place_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.THING_PLACE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.THING_ID,
                         ColumnNamesEnum.PLACE_ID,
                         thing_place_id,
                         thing_id,
                         place_id,
                         relationship_type_id,
                         role_id,
                         thing_place_description,
                         last_updated)

        self.thing_id = thing_id
        self.place_id = place_id
        self.thing_place_id = thing_place_id

    def get_thing(self):
        return self._get_thing(self.thing_id)

    def get_place(self):
        return self._get_place(self.place_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.thing_id
        self._record_id_right = self.place_id
        return_val = self._save()
        self.thing_place_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_thing_place()
        return return_val

    def load(self, thing_place_id):
        self._load_ppt_base_connection_item(thing_place_id)
        self.thing_id = self._record_id_left
        self.place_id = self._record_id_right
        self.thing_place_id = thing_place_id

    def __init_thing_place(self):
        self.thing_id = None
        self.place_id = None
        self.thing_place_id = None
        
# A Thing can be connected to another Thing
# using the ThingThingConnector class


class ThingThingConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 thing_thing_description=None,
                 thing_id_a=None,
                 thing_id_b=None,
                 role_id=None,
                 relationship_type_id=None,
                 thing_thing_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.THING_THING,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.THING_ID_A,
                         ColumnNamesEnum.THING_ID_B,
                         thing_thing_id,
                         thing_id_a,
                         thing_id_b,
                         relationship_type_id,
                         role_id,
                         thing_thing_description,
                         last_updated)

        self.thing_id_a = thing_id_a
        self.thing_id_b = thing_id_b
        self.thing_thing_id = thing_thing_id

    def get_thing_left(self):
        return self._get_thing(self.thing_id_a)

    def get_thing_right(self):
        return self._get_thing(self.thing_id_b)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.thing_id_a
        self._record_id_right = self.thing_id_b
        return_val = self._save()
        self.thing_thing_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_thing_thing()
        return return_val

    def load(self, thing_thing_id):
        self._load_ppt_base_connection_item(thing_thing_id)
        self.thing_id_a = self._record_id_left
        self.thing_id_b = self._record_id_right
        self.thing_thing_id = thing_thing_id

    def __init_thing_thing(self):
        self.thing_id_a = None
        self.thing_id_b = None
        self.thing_thing_id = None
