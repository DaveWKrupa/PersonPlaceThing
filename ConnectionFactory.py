from Enums import TableNamesEnum, ColumnNamesEnum
from PPTBaseConnectorFactory import PPTBaseConnectorFactory
from PersonEventConnector import PersonEventConnector


class PersonEventFactory(PPTBaseConnectorFactory):
    def __init__(self):
        super().__init__(TableNamesEnum.PERSON_EVENT_VIEW,
                         ColumnNamesEnum.PERSON_ID,
                         ColumnNamesEnum.EVENT_ID)

    def get_all(self):
        return self.__load_dictionary(self._get_all())

    def get_where_id_equals(self, person_id=None, event_id=None):
        return self.__load_dictionary(self._get_where_id_equals(person_id, event_id))

    def __load_dictionary(self, data):
        pe_dictionary = dict()
        for pe_dict in data:
            person_event = \
                PersonEventConnector(first_name=
                                     pe_dict[ColumnNamesEnum.FIRST_NAME],
                                     middle_name=
                                     pe_dict[ColumnNamesEnum.MIDDLE_NAME],
                                     last_name=
                                     pe_dict[ColumnNamesEnum.LAST_NAME],
                                     prefix_name=
                                     pe_dict[ColumnNamesEnum.PREFIX_NAME],
                                     suffix_name=
                                     pe_dict[ColumnNamesEnum.SUFFIX_NAME],
                                     phone_number
                                     =pe_dict[ColumnNamesEnum.PHONE_NUMBER],
                                     street=
                                     pe_dict[ColumnNamesEnum.STREET],
                                     street2=
                                     pe_dict[ColumnNamesEnum.STREET2],
                                     city=
                                     pe_dict[ColumnNamesEnum.CITY],
                                     state=
                                     pe_dict[ColumnNamesEnum.STATE],
                                     zip_code=
                                     pe_dict[ColumnNamesEnum.ZIP_CODE],
                                     person_tags=
                                     pe_dict[ColumnNamesEnum.PERSON_TAGS],
                                     event_short_description=
                                     pe_dict[ColumnNamesEnum.EVENT_SHORT_DESCRIPTION],
                                     event_long_description=
                                     pe_dict[ColumnNamesEnum.EVENT_LONG_DESCRIPTION],
                                     event_start_date_time=
                                     pe_dict[ColumnNamesEnum.EVENT_START_DATE_TIME],
                                     event_end_date_time=
                                     pe_dict[ColumnNamesEnum.EVENT_END_DATE_TIME],
                                     event_tags=
                                     pe_dict[ColumnNamesEnum.EVENT_TAGS],
                                     relationship_type_short_description=
                                     pe_dict[ColumnNamesEnum.RELATIONSHIP_TYPE_SHORT_DESCRIPTION],
                                     relationship_type_long_description=
                                     pe_dict[ColumnNamesEnum.RELATIONSHIP_TYPE_LONG_DESCRIPTION],
                                     relationship_type_tags=
                                     pe_dict[ColumnNamesEnum.RELATIONSHIP_TYPE_TAGS],
                                     role_short_description=
                                     pe_dict[ColumnNamesEnum.ROLE_SHORT_DESCRIPTION],
                                     role_long_description=
                                     pe_dict[ColumnNamesEnum.ROLE_LONG_DESCRIPTION],
                                     role_tags=
                                     pe_dict[ColumnNamesEnum.ROLE_TAGS],
                                     person_event_description=
                                     pe_dict[ColumnNamesEnum.PERSON_EVENT_DESCRIPTION],
                                     person_id=
                                     pe_dict[ColumnNamesEnum.PERSON_ID],
                                     event_id=
                                     pe_dict[ColumnNamesEnum.EVENT_ID],
                                     role_id=
                                     pe_dict[ColumnNamesEnum.ROLE_ID],
                                     relationship_type_id=
                                     pe_dict[ColumnNamesEnum.RELATIONSHIP_TYPE_ID],
                                     person_event_id=
                                     pe_dict[ColumnNamesEnum.PERSON_EVENT_ID])

            pe_dictionary[pe_dict[ColumnNamesEnum.PERSON_EVENT_ID]] = person_event
        return pe_dictionary
