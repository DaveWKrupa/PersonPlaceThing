from PersonPlaceThingDB import PersonPlaceThingDB

# This is the base class for all connection factory classes.


class PPTBaseConnectorFactory:
    def __init__(self, table_name,
                 record_id_a_name, record_id_b_name=None):
        self.table_name = table_name
        self._record_id_a_name = record_id_a_name
        self._record_id_b_name = record_id_b_name

    def _get_all(self):
        return PersonPlaceThingDB().read(self.table_name, {})

    def _get_where_id_equals(self, record_id_a=None, record_id_b=None):

        data_params = {}
        if record_id_a:
            data_params[self._record_id_a_name] = record_id_a
        if record_id_b:
            data_params[self._record_id_b_name] = record_id_b

        return PersonPlaceThingDB().read(self.table_name, data_params)

