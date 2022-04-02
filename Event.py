from Enums import TableNamesEnum, ColumnNamesEnum
from PPTCalendarItem import PPTCalendarItem


class Event(PPTCalendarItem):
    def __init__(self, record_id=None, last_updated=None,
                 short_description=None, long_description=None,
                 start_date_time=None, end_date_time=None, tags=None):
        super().__init__(TableNamesEnum.EVENT, record_id, last_updated, short_description, long_description,
                         start_date_time, end_date_time, tags)

    def load(self, record_id):
        if super()._load_ppt_calendar_item(record_id):
            return True
        else:
            super()._init_ppt_calendar_item()
            return False

    def save(self):
        return super()._save_ppt_calendar_item()

    def delete(self):
        if super()._delete_record():
            super()._init_ppt_calendar_item()
            return True
        else:
            return False

    def __str__(self):
        lines = super()._get_ppt_calendar_item_string()

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
