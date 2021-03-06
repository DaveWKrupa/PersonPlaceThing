from Enums import TableNamesEnum
from PPTCalendarItem import PPTCalendarItem

# Actions are the things a Person has done, is doing,
# or will do. Actions do not have to be associated with a person
# as it may not be known who has or will take that Action
# Actions are a PPTCalendarItem as they have
# start and end date.


class Action(PPTCalendarItem):
    def __init__(self, data_saved_callback_func,
                 invalid_data_callback_func,
                 record_id=None,
                 last_updated=None,
                 short_description=None, long_description=None,
                 start_date_time=None, end_date_time=None, tags=None):
        super().__init__(TableNamesEnum.ACTION,  data_saved_callback_func,
                         invalid_data_callback_func,
                         record_id, last_updated,
                         short_description, long_description,
                         start_date_time, end_date_time,  tags)

    def load(self, record_id):
        return super()._load_ppt_calendar_item(record_id)

    def save(self):
        return super()._save_ppt_calendar_item()

    def delete(self):
        return super()._delete_record()

    def __str__(self):
        lines = super()._get_ppt_calendar_item_string()

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''



