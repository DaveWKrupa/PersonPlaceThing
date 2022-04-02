from PersonPlaceThingDB import PersonPlaceThingDB
from PPTBaseFactory import PPTBaseFactory
from Enums import TableNamesEnum, ColumnNamesEnum
from Person import Person
from Place import Place
from Thing import Thing
from Event import Event
from Action import Action
from Role import Role
from RelationshipType import RelationshipType


class TagsList:

    @staticmethod
    def get_tags_list():
        return PersonPlaceThingDB().get_distinct_tags_list()


class PersonFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.PERSON)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, first_name=None, last_name=None, phone_number=None,
                       city=None, state=None, zip_code=None):

        data_params = {}
        if first_name:
            data_params[ColumnNamesEnum.FIRST_NAME] = first_name
        if last_name:
            data_params[ColumnNamesEnum.LAST_NAME] = last_name
        if phone_number:
            data_params[ColumnNamesEnum.PHONE_NUMBER] = phone_number
        if city:
            data_params[ColumnNamesEnum.CITY] = city
        if state:
            data_params[ColumnNamesEnum.STATE] = state
        if zip_code:
            data_params[ColumnNamesEnum.ZIP_CODE] = zip_code

        data = PersonPlaceThingDB().read_where_like(TableNamesEnum.PERSON, data_params)

        return self.__load_dictionary(data)

    def get_by_tags(self, tags):
        return self.__load_dictionary(self._get_by_tags(tags))

    def get_where_event(self, event_id):
        pass
        # data_params = {"event_id": event_id}
        # data = PersonPlaceThingDB().read_where_like(TableNamesEnum.PERSON_EVENT, data_params)
        # return self.__load_dictionary(data)

    def __load_dictionary(self, data):
        person_dictionary = dict()
        for person_dict in data:
            person = Person(person_dict[ColumnNamesEnum.ID],
                            person_dict[ColumnNamesEnum.LAST_UPDATED],
                            person_dict[ColumnNamesEnum.FIRST_NAME],
                            person_dict[ColumnNamesEnum.MIDDLE_NAME],
                            person_dict[ColumnNamesEnum.LAST_NAME],
                            person_dict[ColumnNamesEnum.PREFIX_NAME],
                            person_dict[ColumnNamesEnum.SUFFIX_NAME],
                            person_dict[ColumnNamesEnum.PHONE_NUMBER],
                            person_dict[ColumnNamesEnum.STREET],
                            person_dict[ColumnNamesEnum.STREET2],
                            person_dict[ColumnNamesEnum.CITY],
                            person_dict[ColumnNamesEnum.STATE],
                            person_dict[ColumnNamesEnum.ZIP_CODE],
                            person_dict[ColumnNamesEnum.TAGS])
            person_dictionary[person_dict[ColumnNamesEnum.ID]] = person
        return person_dictionary


class PlaceFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.PLACE)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, short_description=None, long_description=None,
                       phone_number=None, city=None, state=None, zip_code=None):

        data_params = {}
        if short_description:
            data_params[ColumnNamesEnum.SHORT_DESCRIPTION] = short_description
        if long_description:
            data_params[ColumnNamesEnum.LONG_DESCRIPTION] = long_description
        if phone_number:
            data_params[ColumnNamesEnum.PHONE_NUMBER] = phone_number
        if city:
            data_params[ColumnNamesEnum.CITY] = city
        if state:
            data_params[ColumnNamesEnum.STATE] = state
        if zip_code:
            data_params[ColumnNamesEnum.ZIP_CODE] = zip_code

        data = PersonPlaceThingDB().read_where_like(TableNamesEnum.PLACE, data_params)

        return self.__load_dictionary(data)

    def get_by_tags(self, tags):
        return self.__load_dictionary(self._get_by_tags(tags))

    def __load_dictionary(self, data):
        place_dictionary = dict()
        for place_dict in data:
            place = Place(place_dict[ColumnNamesEnum.ID],
                          place_dict[ColumnNamesEnum.LAST_UPDATED],
                          place_dict[ColumnNamesEnum.SHORT_DESCRIPTION],
                          place_dict[ColumnNamesEnum.LONG_DESCRIPTION],
                          place_dict[ColumnNamesEnum.PHONE_NUMBER],
                          place_dict[ColumnNamesEnum.STREET],
                          place_dict[ColumnNamesEnum.STREET2],
                          place_dict[ColumnNamesEnum.CITY],
                          place_dict[ColumnNamesEnum.STATE],
                          place_dict[ColumnNamesEnum.ZIP_CODE],
                          place_dict[ColumnNamesEnum.TAGS])
            place_dictionary[place_dict[ColumnNamesEnum.ID]] = place
        return place_dictionary


class ThingFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.THING)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, short_description=None, long_description=None):
        return self.__load_dictionary(self._get_where_like(short_description, long_description))

    def get_by_tags(self, tags):
        return self.__load_dictionary(self._get_by_tags(tags))

    def __load_dictionary(self, data):
        thing_dictionary = dict()
        for thing_dict in data:
            thing = Thing(thing_dict[ColumnNamesEnum.ID],
                          thing_dict[ColumnNamesEnum.LAST_UPDATED],
                          thing_dict[ColumnNamesEnum.SHORT_DESCRIPTION],
                          thing_dict[ColumnNamesEnum.LONG_DESCRIPTION],
                          thing_dict[ColumnNamesEnum.TAGS])
            thing_dictionary[thing_dict[ColumnNamesEnum.ID]] = thing
        return thing_dictionary


class EventFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.EVENT)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, short_description=None, long_description=None):
        return self.__load_dictionary(self._get_where_like(short_description, long_description))

    def get_by_tags(self, tags):
        return self.__load_dictionary(self._get_by_tags(tags))

    def get_person_events(self, person_id):
        pass

    def __load_dictionary(self, data):
        event_dictionary = dict()
        for event_dict in data:
            event = Event(event_dict[ColumnNamesEnum.ID],
                          event_dict[ColumnNamesEnum.LAST_UPDATED],
                          event_dict[ColumnNamesEnum.SHORT_DESCRIPTION],
                          event_dict[ColumnNamesEnum.LONG_DESCRIPTION],
                          event_dict[ColumnNamesEnum.START_DATE_TIME],
                          event_dict[ColumnNamesEnum.END_DATE_TIME],
                          event_dict[ColumnNamesEnum.TAGS])

            event_dictionary[event_dict[ColumnNamesEnum.ID]] = event
        return event_dictionary


class ActionFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.ACTION)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, short_description=None, long_description=None):
        return self.__load_dictionary(self._get_where_like(short_description, long_description))

    def get_by_tags(self, tags):
        return self.__load_dictionary(self._get_by_tags(tags))

    def __load_dictionary(self, data):
        action_dictionary = dict()
        for action_dict in data:
            action = Action(action_dict[ColumnNamesEnum.ID],
                            action_dict[ColumnNamesEnum.LAST_UPDATED],
                            action_dict[ColumnNamesEnum.SHORT_DESCRIPTION],
                            action_dict[ColumnNamesEnum.LONG_DESCRIPTION],
                            action_dict[ColumnNamesEnum.START_DATE_TIME],
                            action_dict[ColumnNamesEnum.END_DATE_TIME],
                            action_dict[ColumnNamesEnum.TAGS])

            action_dictionary[action_dict[ColumnNamesEnum.ID]] = action
        return action_dictionary


class RoleFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.ROLE)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, short_description=None, long_description=None):
        return self.__load_dictionary(self._get_where_like(short_description, long_description))

    def get_by_tags(self, tags):
        return self.__load_dictionary(self._get_by_tags(tags))

    def __load_dictionary(self, data):
        if data:
            role_dictionary = dict()
            for role_dict in data:
                role = Role(role_dict[ColumnNamesEnum.ID],
                            role_dict[ColumnNamesEnum.LAST_UPDATED],
                            role_dict[ColumnNamesEnum.SHORT_DESCRIPTION],
                            role_dict[ColumnNamesEnum.LONG_DESCRIPTION],
                            role_dict[ColumnNamesEnum.TAGS])
                role_dictionary[role_dict[ColumnNamesEnum.ID]] = role
            return role_dictionary
        else:
            return None


class RelationshipTypeFactory(PPTBaseFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.RELATIONSHIP_TYPE)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_like(self, short_description=None, long_description=None):
        return self.__load_dictionary(self._get_where_like(short_description, long_description))

    def get_by_tags(self, *args):
        return self.__load_dictionary(self._get_by_tags(*args))

    def __load_dictionary(self, data):
        relationship_type_dictionary = dict()
        for relationship_type_dict in data:
            relationship_type = \
                RelationshipType(relationship_type_dict[ColumnNamesEnum.ID],
                                 relationship_type_dict[ColumnNamesEnum.SHORT_DESCRIPTION],
                                 relationship_type_dict[ColumnNamesEnum.LONG_DESCRIPTION],
                                 relationship_type_dict[ColumnNamesEnum.TAGS])
            relationship_type_dictionary[relationship_type_dict[ColumnNamesEnum.ID]] = relationship_type
        return relationship_type_dictionary
