from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from Enums import TableNamesEnum, ColumnNamesEnum
from DateTimeManager import DateTimeManager


class Action:
    def __init__(self, record_id=None,
                 short_description=None, long_description=None,
                 start_date=None, start_time=None,
                 end_date=None, end_time=None,
                 start_date_time=None, end_date_time=None):
        self.__record_id = RecordID(record_id).record_id
        self.short_description = short_description
        self.long_description = long_description
        self.__action_time_span = DateTimeManager(start_date, start_time,
                                                  end_date, end_time,
                                                  start_date_time, end_date_time)

    @property
    def record_id(self):
        return self.__record_id

    @property
    def start_date(self):
        return self.__action_time_span.start_date

    @start_date.setter
    def start_date(self, value):
        self.__action_time_span.start_date = value

    @property
    def start_time(self):
        return self.__action_time_span.start_time

    @start_time.setter
    def start_time(self, value):
        self.__action_time_span.start_time = value

    @property
    def start_date_time(self):
        return self.__action_time_span.start_date_time

    @start_date_time.setter
    def start_date_time(self, value):
        self.__action_time_span.start_date_time = value

    @property
    def end_date(self):
        return self.__action_time_span.end_date

    @end_date.setter
    def end_date(self, value):
        self.__action_time_span.end_date = value

    @property
    def end_time(self):
        return self.__action_time_span.end_time

    @end_time.setter
    def end_time(self, value):
        self.__action_time_span.end_time = value

    @property
    def end_date_time(self):
        return self.__action_time_span.end_date_time

    @end_date_time.setter
    def end_date_time(self, value):
        self.__action_time_span.end_date_time = value

    @property
    def duration_string(self):
        return self.__action_time_span.duration_string

    @property
    def duration_in_seconds(self):
        return self.__action_time_span.duration_in_seconds

    @property
    def action_time_span(self):
        return str(self.__action_time_span)

    def load(self, record_id):
        data = PersonPlaceThingDB().read(TableNamesEnum().ACTION, {}, record_id)
        if len(data) == 1:
            self.__record_id = record_id
            self.short_description = data[0][ColumnNamesEnum().SHORT_DESCRIPTION]
            self.long_description = data[0][ColumnNamesEnum().LONG_DESCRIPTION]
            self.start_date = data[0][ColumnNamesEnum().START_DATE]
            self.start_time = data[0][ColumnNamesEnum().START_TIME]
            self.end_date = data[0][ColumnNamesEnum().END_DATE]
            self.end_time = data[0][ColumnNamesEnum().END_TIME]

            return True
        else:
            self.__init_action()
            return False

    def save(self):
        data = {ColumnNamesEnum().SHORT_DESCRIPTION: self.short_description,
                ColumnNamesEnum().LONG_DESCRIPTION: self.long_description,
                ColumnNamesEnum().START_DATE: self.start_date,
                ColumnNamesEnum().START_TIME: self.start_time,
                ColumnNamesEnum().END_DATE: self.end_date,
                ColumnNamesEnum().END_TIME: self.end_time}
        self.__record_id = \
            PersonPlaceThingDB().save(TableNamesEnum().ACTION,
                                      self.__record_id, data)

    def delete(self, record_id=None):
        if record_id:
            PersonPlaceThingDB().delete(TableNamesEnum().ACTION, record_id)
        else:
            PersonPlaceThingDB().delete(TableNamesEnum().ACTION, self.record_id)
        self.__init_action()

    def __init_action(self):
        self.__record_id = RecordID().record_id
        self.short_description = None
        self.long_description = None
        self.__action_time_span = DateTimeManager()

    def __str__(self):
        lines = []
        if self.short_description != '':
            lines.append(self.short_description)
        if self.long_description != '':
            lines.append(self.long_description)

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''
