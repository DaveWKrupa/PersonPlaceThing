from Enums import TableNamesEnum
from PPTBaseItem import PPTBaseItem

# The Role class can be used to describe
# an attribute or association.
# The Person class has a connection class with Role
# and can be used to describe such things as
# a profession or occupation.
# The Role class can also be used by the connector
# classes to further describe how one class is
# related to another.
# For example for a Thing-Thing relationship
# as steering wheel thing is a part of a vehicle thing,
# and its role is 'directional control mechanism'.
# The RelationshipType for steering wheel and vehicle
# would be something like 'is a component of'.


class Role(PPTBaseItem):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func,
                 record_id=None, last_updated=None,
                 short_description=None, long_description=None, tags=None):
        super().__init__(TableNamesEnum.ROLE, data_saved_callback_func,
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
