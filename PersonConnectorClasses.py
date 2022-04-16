from PPTBaseConnector import PPTBaseConnector
from Enums import TableNamesEnum, ColumnNamesEnum

# A Person can be connected to an Event
# using the PersonEventConnector class


class PersonEventConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 person_event_description=None,
                 person_id=None,
                 event_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 person_event_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PERSON_EVENT,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.EVENT_ID,
                         person_event_id,
                         person_id,
                         event_id,
                         relationship_type_id,
                         role_id,
                         person_event_description,
                         last_updated)

        self.person_id = person_id
        self.event_id = event_id
        self.person_event_id = person_event_id

    def get_person(self):
        return self._get_person(self.person_id)

    def get_event(self):
        return self._get_event(self.event_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.person_id
        self._record_id_right = self.event_id
        return_val = self._save()
        self.person_event_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_person_event()
        return return_val

    def load(self, person_event_id):
        self._load_ppt_base_connection_item(person_event_id)
        self.person_id = self._record_id_left
        self.event_id = self._record_id_right
        self.person_event_id = person_event_id

    def __init_person_event(self):
        self.person_id = None
        self.event_id = None
        self.person_event_id = None

# A Person can be connected to an Action
# using the PersonActionConnector


class PersonActionConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 person_action_description=None,
                 person_id=None,
                 action_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 person_action_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PERSON_ACTION,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.ACTION_ID,
                         person_action_id,
                         person_id,
                         action_id,
                         relationship_type_id,
                         role_id,
                         person_action_description,
                         last_updated)

        self.person_id = person_id
        self.action_id = action_id
        self.person_action_id = person_action_id

    def get_person(self):
        return self._get_person(self.person_id)

    def get_action(self):
        return self._get_action(self.action_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.person_id
        self._record_id_right = self.action_id
        return_val = self._save()
        self.person_action_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_person_action()
        return return_val

    def load(self, person_action_id):
        self._load_ppt_base_connection_item(person_action_id)
        self.person_id = self._record_id_left
        self.action_id = self._record_id_right
        self.person_action_id = person_action_id

    def __init_person_action(self):
        self.person_id = None
        self.action_id = None
        self.person_action_id = None

# A person can be connected to a Place
# using the PersonPlaceConnector


class PersonPlaceConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 person_place_description=None,
                 person_id=None,
                 place_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 person_place_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PERSON_PLACE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.PLACE_ID,
                         person_place_id,
                         person_id,
                         place_id,
                         relationship_type_id,
                         role_id,
                         person_place_description,
                         last_updated)

        self.person_id = person_id
        self.place_id = place_id
        self.person_place_id = person_place_id

    def get_person(self):
        return self._get_person(self.person_id)

    def get_place(self):
        return self._get_place(self.place_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.person_id
        self._record_id_right = self.place_id
        return_val = self._save()
        self.person_place_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_person_place()
        return return_val

    def load(self, person_place_id):
        self._load_ppt_base_connection_item(person_place_id)
        self.person_id = self._record_id_left
        self.place_id = self._record_id_right
        self.person_place_id = person_place_id

    def __init_person_place(self):
        self.person_id = None
        self.place_id = None
        self.person_place_id = None

# A person can be connected to a Thing
# using the PersonThingConnector


class PersonThingConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 person_thing_description=None,
                 person_id=None,
                 thing_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 person_thing_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PERSON_THING,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.THING_ID,
                         person_thing_id,
                         person_id,
                         thing_id,
                         relationship_type_id,
                         role_id,
                         person_thing_description,
                         last_updated)

        self.person_id = person_id
        self.thing_id = thing_id
        self.person_thing_id = person_thing_id

    def get_person(self):
        return self._get_person(self.person_id)

    def get_thing(self):
        return self._get_thing(self.thing_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.person_id
        self._record_id_right = self.thing_id
        return_val = self._save()
        self.person_thing_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_person_thing()
        return return_val

    def load(self, person_thing_id):
        self._load_ppt_base_connection_item(person_thing_id)
        self.person_id = self._record_id_left
        self.thing_id = self._record_id_right
        self.person_thing_id = person_thing_id

    def __init_person_thing(self):
        self.person_id = None
        self.thing_id = None
        self.person_thing_id = None

# A Person can be connected to another person
# using the PersonPersonConnector


class PersonPersonConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 person_person_description=None,
                 person_id_a=None,
                 person_id_b=None,
                 role_id=None,
                 relationship_type_id=None,
                 person_person_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PERSON_PERSON,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PERSON_ID_A,
                         ColumnNamesEnum.PERSON_ID_B,
                         person_person_id,
                         person_id_a,
                         person_id_b,
                         relationship_type_id,
                         role_id,
                         person_person_description,
                         last_updated)

        self.person_id_a = person_id_a
        self.person_id_b = person_id_b
        self.person_person_id = person_person_id

    def get_person_a(self):
        return self._get_person(self.person_id_a)

    def get_person_b(self):
        return self._get_person(self.person_id_b)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.person_id_a
        self._record_id_right = self.person_id_b
        return_val = self._save()
        self.person_person_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_person_person()
        return return_val

    def load(self, person_person_id):
        self._load_ppt_base_connection_item(person_person_id)
        self.person_id_a = self._record_id_left
        self.person_id_b = self._record_id_right
        self.person_person_id = person_person_id

    def __init_person_person(self):
        self.person_id_a = None
        self.person_id_b = None
        self.person_person_id = None


class PersonRoleConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 person_role_description=None,
                 person_id=None,
                 role_id=None,
                 relationship_type_id=None,
                 person_role_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PERSON_ROLE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PERSON_ID,
                         None,
                         person_role_id,
                         person_id,
                         None,
                         relationship_type_id,
                         role_id,
                         person_role_description,
                         last_updated)
        self.person_id = person_id
        self.person_role_id = person_role_id

    def get_person(self):
        return self._get_person(self.person_id)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.person_id
        return_val = self._save()
        self.person_role_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_person_role()
        return return_val

    def load(self, person_role_id):
        self._load_ppt_base_connection_item(person_role_id)
        self.person_id = self._record_id_left
        self.person_role_id = person_role_id

    def __init_person_role(self):
        self.person_id = None
        self.person_role_id = None


