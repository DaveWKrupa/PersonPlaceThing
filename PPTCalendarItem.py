from PPTBaseItem import PPTBaseItem
from DateTimeManager import DateTimeManager
from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import ColumnNamesEnum
from Constants import RECORD_NOT_FOUND, ERROR_LOADING_RECORD, \
    RECORD_LOADED, RECORD_SAVED, DatabaseResult

# The PPTCalendarItem class extends the PPTBaseItem class
# with DateTime fields and methods


class PPTCalendarItem(PPTBaseItem):
    def __init__(self, table_name, data_saved_callback_func,
                 invalid_data_callback_func,
                 record_id=None, last_updated=None,
                 short_description=None, long_description=None,
                 start_date_time=None, end_date_time=None, tags=None):
        super().__init__(table_name, data_saved_callback_func,
                         invalid_data_callback_func,
                         record_id, last_updated,
                         short_description, long_description, tags)
        self.__time_span = DateTimeManager(invalid_data_callback_func,
                                           start_date_time, end_date_time)

    @property
    def start_date(self):
        return self.__time_span.start_date

    @start_date.setter
    def start_date(self, value):
        self.__time_span.start_date = value

    @property
    def start_time(self):
        return self.__time_span.start_time

    @start_time.setter
    def start_time(self, value):
        self.__time_span.start_time = value

    @property
    def start_date_time(self):
        return self.__time_span.start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        self.__time_span.start_date_time = value

    @property
    def end_date(self):
        return self.__time_span.end_date

    @end_date.setter
    def end_date(self, value):
        self.__time_span.end_date = value

    @property
    def end_time(self):
        return self.__time_span.end_time

    @end_time.setter
    def end_time(self, value):
        self.__time_span.end_time = value

    @property
    def end_date_time(self):
        return self.__time_span.end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        self.__time_span.end_date_time = value

    @property
    def duration_string(self):
        return self.__time_span.duration_string

    @property
    def duration_in_seconds(self):
        return self.__time_span.duration_in_seconds

    @property
    def time_span(self):
        return str(self.__time_span)

    def _init_ppt_calendar_item(self):
        self._init_ppt_base_item()
        self.__time_span = DateTimeManager(self._invalid_data_callback_func)

    def _get_ppt_calendar_item_string(self):
        lines = self._get_ppt_base_item_string()
        if self.start_date_time:
            lines.append(f"Start Date: {str(self.__time_span.start_date_time)}")
        if self.end_date_time:
            lines.append(f"End Date: {str(self.__time_span.end_date_time)}")
        return lines

    def _load_ppt_calendar_item(self, record_id):
        data = PersonPlaceThingDB().read(self._table_name, {}, record_id)
        if len(data) == 1:
            self._record_id = record_id
            self.short_description = data[0][ColumnNamesEnum.SHORT_DESCRIPTION]
            self.long_description = data[0][ColumnNamesEnum.LONG_DESCRIPTION]
            self.start_date_time = data[0][ColumnNamesEnum.START_DATE_TIME]
            self.end_date_time = data[0][ColumnNamesEnum.END_DATE_TIME]
            self._tags = data[0][ColumnNamesEnum.TAGS]
            self._last_updated = data[0][ColumnNamesEnum.LAST_UPDATED]
            return DatabaseResult(True, self._record_id, RECORD_LOADED, "")
        else:
            self._fire_invalid_data_callback_func(RECORD_NOT_FOUND
                                                     + " " + self._table_name
                                                     + " " + RECORD_NOT_FOUND)
            self._init_ppt_calendar_item()
            return DatabaseResult(False, self._record_id,
                                  ERROR_LOADING_RECORD,
                                  self._table_name + " " + RECORD_NOT_FOUND)

    def _save_ppt_calendar_item(self):
        data = {ColumnNamesEnum.START_DATE_TIME: self.start_date_time,
                ColumnNamesEnum.END_DATE_TIME: self.end_date_time}

        return_val = self._save_record(data)
        if return_val.succeeded:
            self._load_ppt_calendar_item(return_val.record_id)
            self._fire_data_saved_callback_func(self._table_name
                                                   + ": " + RECORD_SAVED)
        return return_val
