from PPTBaseConnectorFactory import PPTBaseConnectorFactory
from Enums import TableNamesEnum, ColumnNamesEnum
from PersonConnectorClasses import PersonRoleConnector, \
    PersonPersonConnector, PersonEventConnector, \
    PersonActionConnector, PersonPlaceConnector, PersonThingConnector
from ActionConnectorClasses import ActionActionConnector, \
    ActionEventConnector, ActionPlaceConnector
from EventConnectorClasses import EventEventConnector, EventPlaceConnector
from PlaceConnectorClasses import PlacePlaceConnector
from ThingConnectorClasses import ThingThingConnector, ThingEventConnector, \
    ThingPlaceConnector, ThingActionConnector


class ActionActionConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.ACTION_ACTION,
                         ColumnNamesEnum.ACTION_ID_A,
                         ColumnNamesEnum.ACTION_ID_B)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, action_id_a=None, action_id_b=None):
        return self.__load_data(
            self._get_where_id_equals(action_id_a, action_id_b))

    def __load_data(self, data):
        action_action_list = list()
        for row in data:
            aac = ActionActionConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                action_action_description=row[ColumnNamesEnum.DESCRIPTION],
                action_id_a=row[ColumnNamesEnum.ACTION_ID_A],
                action_id_b=row[ColumnNamesEnum.ACTION_ID_B],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                action_action_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            action_action_list.append(aac)
        return action_action_list


class ActionEventConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.ACTION_EVENT,
                         ColumnNamesEnum.ACTION_ID,
                         ColumnNamesEnum.EVENT_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, action_id=None, event_id=None):
        return self.__load_data(
            self._get_where_id_equals(action_id, event_id))

    def __load_data(self, data):
        action_event_list = list()
        for row in data:
            aac = ActionEventConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                action_event_description=row[ColumnNamesEnum.DESCRIPTION],
                action_id=row[ColumnNamesEnum.ACTION_ID],
                event_id=row[ColumnNamesEnum.EVENT_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                action_event_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            action_event_list.append(aac)
        return action_event_list


class ActionPlaceConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.ACTION_PLACE,
                         ColumnNamesEnum.ACTION_ID,
                         ColumnNamesEnum.PLACE_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, action_id=None, place_id=None):
        return self.__load_data(self._get_where_id_equals(action_id, place_id))

    def __load_data(self, data):
        action_place_list = list()
        for row in data:
            apc = ActionPlaceConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                action_place_description=row[ColumnNamesEnum.DESCRIPTION],
                action_id=row[ColumnNamesEnum.ACTION_ID],
                place_id=row[ColumnNamesEnum.PLACE_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                action_place_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            action_place_list.append(apc)
        return action_place_list


class EventEventConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.EVENT_EVENT,
                         ColumnNamesEnum.EVENT_ID_A,
                         ColumnNamesEnum.EVENT_ID_B)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, event_id_a=None, event_id_b=None):
        return self.__load_data(self._get_where_id_equals(event_id_a, event_id_b))

    def __load_data(self, data):
        event_event_list = list()
        for row in data:
            eec = EventEventConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                event_event_description=row[ColumnNamesEnum.DESCRIPTION],
                event_id_a=row[ColumnNamesEnum.EVENT_ID_A],
                event_id_b=row[ColumnNamesEnum.EVENT_ID_B],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                event_event_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            event_event_list.append(eec)
        return event_event_list


class EventPlaceConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.EVENT_PLACE,
                         ColumnNamesEnum.EVENT_ID,
                         ColumnNamesEnum.PLACE_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, event_id=None, place_id=None):
        return self.__load_data(self._get_where_id_equals(event_id, place_id))

    def __load_data(self, data):
        event_place_list = list()
        for row in data:
            epc = EventPlaceConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                event_place_description=row[ColumnNamesEnum.DESCRIPTION],
                event_id=row[ColumnNamesEnum.EVENT_ID],
                place_id=row[ColumnNamesEnum.PLACE_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                event_place_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            event_place_list.append(epc)
        return event_place_list


class PersonPersonConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PERSON_PERSON,
                         ColumnNamesEnum.PERSON_ID_A,
                         ColumnNamesEnum.PERSON_ID_B)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, person_id_a=None, person_id_b=None):
        return self.__load_data(self._get_where_id_equals(person_id_a, person_id_b))

    def __load_data(self, data):
        person_person_list = list()
        for row in data:
            ppc = PersonPersonConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                person_person_description=row[ColumnNamesEnum.DESCRIPTION],
                person_id_a=row[ColumnNamesEnum.PERSON_ID_A],
                person_id_b=row[ColumnNamesEnum.PERSON_ID_B],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                person_person_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            person_person_list.append(ppc)
        return person_person_list


class PersonActionConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PERSON_ACTION,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.ACTION_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, person_id=None, action_id=None):
        return self.__load_data(self._get_where_id_equals(person_id, action_id))

    def __load_data(self, data):
        person_action_list = list()
        for row in data:
            pec = PersonActionConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                person_action_description=row[ColumnNamesEnum.DESCRIPTION],
                person_id=row[ColumnNamesEnum.PERSON_ID],
                action_id=row[ColumnNamesEnum.ACTION_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                person_action_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            person_action_list.append(pec)
        return person_action_list


class PersonEventConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PERSON_EVENT,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.EVENT_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, person_id=None, event_id=None):
        return self.__load_data(self._get_where_id_equals(person_id, event_id))

    def __load_data(self, data):
        person_event_list = list()
        for row in data:
            pec = PersonEventConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                person_event_description=row[ColumnNamesEnum.DESCRIPTION],
                person_id=row[ColumnNamesEnum.PERSON_ID],
                event_id=row[ColumnNamesEnum.EVENT_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                person_event_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            person_event_list.append(pec)
        return person_event_list


class PersonPlaceConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PERSON_PLACE,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.PLACE_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, person_id=None, place_id=None):
        return self.__load_data(self._get_where_id_equals(person_id, place_id))

    def __load_data(self, data):
        person_place_list = list()
        for row in data:
            pec = PersonPlaceConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                person_place_description=row[ColumnNamesEnum.DESCRIPTION],
                person_id=row[ColumnNamesEnum.PERSON_ID],
                place_id=row[ColumnNamesEnum.PLACE_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                person_place_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            person_place_list.append(pec)
        return person_place_list


class PersonThingConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PERSON_THING,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.THING_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, person_id=None, thing_id=None):
        return self.__load_data(self._get_where_id_equals(person_id, thing_id))

    def __load_data(self, data):
        person_thing_list = list()
        for row in data:
            pec = PersonThingConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                person_thing_description=row[ColumnNamesEnum.DESCRIPTION],
                person_id=row[ColumnNamesEnum.PERSON_ID],
                thing_id=row[ColumnNamesEnum.THING_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                person_thing_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            person_thing_list.append(pec)
        return person_thing_list


class PersonRoleConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PERSON_ROLE,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.ROLE_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, person_id=None, role_id=None):
        return self.__load_data(self._get_where_id_equals(person_id, role_id))

    def __load_data(self, data):
        person_role_list = list()
        for row in data:
            prc = PersonRoleConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                person_role_description=row[ColumnNamesEnum.DESCRIPTION],
                person_id=row[ColumnNamesEnum.PERSON_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                person_role_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            person_role_list.append(prc)
        return person_role_list


class PlacePlaceConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.PLACE_PLACE,
                         ColumnNamesEnum.PLACE_ID_A,
                         ColumnNamesEnum.PLACE_ID_B)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, place_id_a=None, place_id_b=None):
        return self.__load_data(self._get_where_id_equals(place_id_a, place_id_b))

    def __load_data(self, data):
        place_place_list = list()
        for row in data:
            ppc = PlacePlaceConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                place_place_description=row[ColumnNamesEnum.DESCRIPTION],
                place_id_a=row[ColumnNamesEnum.PLACE_ID_A],
                place_id_b=row[ColumnNamesEnum.PLACE_ID_B],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                place_place_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            place_place_list.append(ppc)
        return place_place_list


class ThingThingConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.THING_THING,
                         ColumnNamesEnum.THING_ID_A,
                         ColumnNamesEnum.THING_ID_B)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, thing_id_a=None, thing_id_b=None):
        return self.__load_data(self._get_where_id_equals(thing_id_a, thing_id_b))

    def __load_data(self, data):
        thing_thing_list = list()
        for row in data:
            ppc = ThingThingConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                thing_thing_description=row[ColumnNamesEnum.DESCRIPTION],
                thing_id_a=row[ColumnNamesEnum.THING_ID_A],
                thing_id_b=row[ColumnNamesEnum.THING_ID_B],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                thing_thing_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            thing_thing_list.append(ppc)
        return thing_thing_list


class ThingActionConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.THING_ACTION,
                         ColumnNamesEnum.THING_ID,
                         ColumnNamesEnum.ACTION_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, thing_id=None, action_id=None):
        return self.__load_data(self._get_where_id_equals(thing_id, action_id))

    def __load_data(self, data):
        thing_action_list = list()
        for row in data:
            pec = ThingActionConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                thing_action_description=row[ColumnNamesEnum.DESCRIPTION],
                thing_id=row[ColumnNamesEnum.THING_ID],
                action_id=row[ColumnNamesEnum.ACTION_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                thing_action_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            thing_action_list.append(pec)
        return thing_action_list


class ThingEventConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.THING_EVENT,
                         ColumnNamesEnum.THING_ID,
                         ColumnNamesEnum.EVENT_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, thing_id=None, event_id=None):
        return self.__load_data(self._get_where_id_equals(thing_id, event_id))

    def __load_data(self, data):
        thing_event_list = list()
        for row in data:
            pec = ThingEventConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                thing_event_description=row[ColumnNamesEnum.DESCRIPTION],
                thing_id=row[ColumnNamesEnum.THING_ID],
                event_id=row[ColumnNamesEnum.EVENT_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                thing_event_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            thing_event_list.append(pec)
        return thing_event_list


class ThingPlaceConnectorFactory(PPTBaseConnectorFactory):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func):
        super().__init__(TableNamesEnum.THING_PLACE,
                         ColumnNamesEnum.THING_ID,
                         ColumnNamesEnum.PLACE_ID)
        self.data_saved_callback_func = data_saved_callback_func
        self.invalid_data_callback_func = invalid_data_callback_func

    def get_all(self):
        return self.__load_data(self._get_all())

    def get_where_id_equals(self, thing_id=None, place_id=None):
        return self.__load_data(self._get_where_id_equals(thing_id, place_id))

    def __load_data(self, data):
        thing_place_list = list()
        for row in data:
            pec = ThingPlaceConnector(
                self.data_saved_callback_func,
                self.invalid_data_callback_func,
                thing_place_description=row[ColumnNamesEnum.DESCRIPTION],
                thing_id=row[ColumnNamesEnum.THING_ID],
                place_id=row[ColumnNamesEnum.PLACE_ID],
                role_id=row[ColumnNamesEnum.ROLE_ID],
                relationship_type_id=row[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                thing_place_id=row[ColumnNamesEnum.ID],
                last_updated=row[ColumnNamesEnum.LAST_UPDATED])
            thing_place_list.append(pec)
        return thing_place_list

