from Enums import TableNamesEnum
from PPTBaseItem import PPTBaseItem


class RelationshipType(PPTBaseItem):
    def __init__(self, data_saved_callback_func=None,
                 invalid_data_callback_func=None,
                 record_id=None, last_updated=None,
                 short_description=None, long_description=None, tags=None):
        super().__init__(TableNamesEnum.RELATIONSHIP_TYPE,
                         data_saved_callback_func,
                         invalid_data_callback_func,
                         record_id, last_updated,
                         short_description, long_description, tags)

    def load(self, record_id):
        return super()._load_ppt_base_item(record_id)

    def save(self):
        return super()._save_record()

    def delete(self):
        return super()._delete_record()

    def __str__(self):
        lines = super()._get_ppt_base_item_string()

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
