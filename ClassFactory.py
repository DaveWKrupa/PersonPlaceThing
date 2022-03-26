from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum


class DataFactory:
    def __init__(self, table_name):
        self.__table_name = table_name

    def get_all(self):
        ppt = PersonPlaceThingDB()
        return ppt.read(self.__table_name, {})


class PersonFactory(DataFactory):
    def __init__(self):
        super().__init__(TableNamesEnum().PERSON)

    def get_by(self, record_id=None, first_name=None, last_name=None, phone_number=None,
               city=None, state=None, zip_code=None):
        ppt = PersonPlaceThingDB()
        if record_id:
            return ppt.read(TableNamesEnum().PERSON, {}, record_id)
        else:
            data_params = {}
            if first_name:
                data_params[ColumnNamesEnum().FIRST_NAME] = first_name
            if last_name:
                data_params[ColumnNamesEnum().LAST_NAME] = last_name
            if phone_number:
                data_params[ColumnNamesEnum().PHONE_NUMBER] = phone_number
            if city:
                data_params[ColumnNamesEnum().CITY] = city
            if state:
                data_params[ColumnNamesEnum().STATE] = state
            if zip_code:
                data_params[ColumnNamesEnum().ZIP_CODE] = zip_code

            return ppt.read(TableNamesEnum().PERSON, data_params)


class PlaceFactory(DataFactory):
    def __init__(self):
        super().__init__(TableNamesEnum().PLACE)


class ThingFactory(DataFactory):
    def __init__(self):
        super().__init__(TableNamesEnum().THING)


class EventFactory(DataFactory):
    def __init__(self):
        super().__init__(TableNamesEnum().EVENT)


class ActionFactory(DataFactory):
    def __init__(self):
        super().__init__(TableNamesEnum().ACTION)

