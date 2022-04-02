from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import ColumnNamesEnum


class PPTBaseFactory:
    def __init__(self, table_name):
        self.table_name = table_name

    def _get_all(self):
        return PersonPlaceThingDB().read(self.table_name, {})

    def _get_where_like(self, short_description=None, long_description=None):

        data_params = {}
        if short_description:
            data_params[ColumnNamesEnum.SHORT_DESCRIPTION] = short_description
        if long_description:
            data_params[ColumnNamesEnum.LONG_DESCRIPTION] = long_description

        return PersonPlaceThingDB().read_where_like(self.table_name, data_params)

    def _get_by_tags(self, *args):
        tags = list()
        for arg in args:
            if not isinstance(arg, list):
                tags.append(str(arg).lower())
            else:
                lower_case_tags = map(lambda x: x.lower(), arg)
                tags.extend(list(lower_case_tags))

        return PersonPlaceThingDB().read_with_tags(self.table_name, tags)

