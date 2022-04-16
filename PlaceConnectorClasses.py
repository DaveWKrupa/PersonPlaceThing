from PPTBaseConnector import PPTBaseConnector
from Enums import TableNamesEnum, ColumnNamesEnum

# A Place can be connected to another Place
# using the PlacePlaceConnector


class PlacePlaceConnector(PPTBaseConnector):
    def __init__(self,
                 data_saved_callback_func,
                 invalid_data_callback_func,
                 place_place_description=None,
                 place_id_a=None,
                 place_id_b=None,
                 role_id=None,
                 relationship_type_id=None,
                 place_place_id=None,
                 last_updated=None):
        super().__init__(TableNamesEnum.PLACE_PLACE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         ColumnNamesEnum.PLACE_ID_A,
                         ColumnNamesEnum.PLACE_ID_B,
                         place_place_id,
                         place_id_a,
                         place_id_b,
                         relationship_type_id,
                         role_id,
                         place_place_description,
                         last_updated)

        self.place_id_a = place_id_a
        self.place_id_b = place_id_b
        self.place_place_id = place_place_id

    def get_place_left(self):
        return self._get_place(self.place_id_a)

    def get_place_right(self):
        return self._get_place(self.place_id_b)

    def get_role(self):
        return self._get_role(self.role_id)

    def get_relationship_type(self):
        return self._get_relationship_type(self.relationship_type_id)

    def save(self):
        self._record_id_left = self.place_id_a
        self._record_id_right = self.place_id_b
        return_val = self._save()
        self.place_place_id = return_val.record_id
        return return_val

    def delete(self):
        return_val = self._delete()
        if return_val.succeeded:
            self.__init_place_place()
        return return_val

    def load(self, place_place_id):
        self._load_ppt_base_connection_item(place_place_id)
        self.place_id_a = self._record_id_left
        self.place_id_b = self._record_id_right
        self.place_place_id = place_place_id

    def __init_place_place(self):
        self.place_id_a = None
        self.place_id_b = None
        self.place_place_id = None
