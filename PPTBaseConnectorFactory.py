from PersonPlaceThingDB import PersonPlaceThingDB


class PPTBaseConnectorFactory:
    def __init__(self, table_name,
                 record_id_left_name, record_id_right_name=None):
        self.table_name = table_name
        self._record_id_left_name = record_id_left_name
        self._record_id_right_name = record_id_right_name

    def _get_all(self):
        return PersonPlaceThingDB().read(self.table_name, {})

    def _get_where_id_equals(self, record_id_left=None, record_id_right=None):

        data_params = {}
        if record_id_left:
            data_params[self._record_id_left_name] = record_id_left
        if record_id_right:
            data_params[self._record_id_right_name] = record_id_right

        return PersonPlaceThingDB().read(self.table_name, data_params)

