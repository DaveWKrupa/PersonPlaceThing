from datetime import datetime
from Constants import YYYY_MM_DD, YYYY_MM_DD_FORMAT
from Constants import HH_MM_SS, HH_MM_SS_FORMAT
from Constants import YYYY_MM_DD_HH_MM_SS_FORMAT, YYYY_MM_DD_HH_MM_SS

# The DateTimeManager class can be used by other classes
# that have dates and times as a component.

class DateTimeManager:
    def __init__(self, invalid_data_callback_func,
                 start_date_time=None, end_date_time=None):
        self.__invalid_data_callback_func = invalid_data_callback_func
        self.__start_date = None
        self.__start_time = None
        self.__end_date = None
        self.__end_time = None
        self.__start_date_time = start_date_time \
            if self.validate_date_time(start_date_time) else ''
        self.__end_date_time = end_date_time \
            if self.validate_date_time(end_date_time) else ''
        self.__duration_in_seconds = None
        self.__duration_days = None
        self.__duration_hours = None
        self.__duration_minutes = None
        self.__duration_seconds = None
        self.__init_date_time_values()

    @property
    def start_date(self):
        return self.__start_date if self.__start_date else ''

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value if self.validate_date(value) else ''
        self.__set_start_date_time_values("start_date")

    @property
    def start_time(self):
        return self.__start_time if self.__start_time else ''

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value if self.validate_time(value) else ''
        self.__set_start_date_time_values("start_time")

    @property
    def start_date_time(self):
        return self.__start_date_time if self.__start_date_time else ''

    @start_date_time.setter
    def start_date_time(self, value):
        self.__start_date_time = value \
            if self.validate_date_time(value) else ''
        self.__set_start_date_time_values("start_date_time")

    @property
    def end_date(self):
        return self.__end_date if self.__end_date else ''

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value if self.validate_date(value) else ''
        self.__set_end_date_time_values("end_date")

    @property
    def end_time(self):
        return self.__end_time if self.__end_time else ''

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value if self.validate_time(value) else ''
        self.__set_end_date_time_values("end_time")

    @property
    def end_date_time(self):
        return self.__end_date_time if self.__end_date_time else ''

    @end_date_time.setter
    def end_date_time(self, value):
        self.__end_date_time = value if self.validate_date_time(value) else ''
        self.__set_end_date_time_values("end_date_time")

    @property
    def duration_string(self):
        return self.__duration_to_string(self.__duration_in_seconds)

    @property
    def duration_in_seconds(self):
        return self.__duration_in_seconds

    def validate_date(self, date_text):
        if not date_text:
            return True  # a value of None is valid
        if not self.__validate_input(date_text, YYYY_MM_DD_FORMAT):
            self.__fire_invalid_data_callback_func(
                f"Date format should take the form {YYYY_MM_DD}")
        return True

    def validate_time(self, time_text):
        if not time_text:
            return True  # a value of None is valid
        if not self.__validate_input(time_text, HH_MM_SS_FORMAT):
            self.__fire_invalid_data_callback_func(
                "Time format should take the 24 hour form "
                f"with time zone {HH_MM_SS}")
        return True

    def validate_date_time(self, time_text):
        if not time_text:
            return True  # a value of None is valid
        if not self.__validate_input(time_text, YYYY_MM_DD_HH_MM_SS_FORMAT):
            self.__fire_invalid_data_callback_func(
                "Date-Time format should take the 24 hour form "
                f"with time zone {YYYY_MM_DD_HH_MM_SS}")
        return True

    def __validate_input(self, date_text, format_string):
        try:
            datetime.strptime(str(date_text), format_string)
            return True
        except ValueError:
            return False

    # turn the integer value for duration_in_seconds into a string
    # e.g. 1015 days, 4 hours, 27 minutes, 45 seconds
    def __duration_to_string(self, duration_in_seconds):
        self.__duration_days = int(duration_in_seconds / 86400)
        seconds_left = duration_in_seconds % 86400
        self.__duration_hours = int(seconds_left / 3600)
        seconds_left = seconds_left % 3600
        self.__duration_minutes = int(seconds_left / 60)
        self.__duration_seconds = int(seconds_left % 60)

        return f"{self.__duration_days} days, {self.__duration_hours} hours, " \
               f"{self.__duration_minutes} minutes, {self.__duration_seconds} seconds"

    def __validate_duration(self, duration_in_seconds):
        if not duration_in_seconds:
            return True  # None is a valid value for duration_in_seconds
        if isinstance(duration_in_seconds, int):
            if duration_in_seconds >= 0:
                return True
        return False

        # This function take the start date and times, end date and times
        # and duration values, compares them and sets duration_in_seconds
        # or end date and end time, depending on what is available

    def __set_duration(self):

        if not self.__start_date or not self.__end_date \
                or not self.__start_time or not self.__end_time:
            # if any dates and times don't exist then set duration_in_seconds = 0
            self.__duration_in_seconds = 0
        else:
            dt_start = datetime.strptime(str(self.__start_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
            dt_end = datetime.strptime(str(self.__end_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
            if dt_start > dt_end:
                self.end_date_time = self.__start_date_time
                # reset
                dt_start = datetime.strptime(str(self.__start_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
                dt_end = datetime.strptime(str(self.__end_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)

            # at this point we should have valid dates to compare
            self.__duration_in_seconds = \
                (dt_end - dt_start).total_seconds()

    def __init_date_time_values(self):
        if self.__start_date_time:
            dt = datetime.strptime(str(self.__start_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
            self.__start_date = dt.strftime(YYYY_MM_DD_FORMAT)
            self.__start_time = dt.strftime(HH_MM_SS_FORMAT)
        elif self.__start_date and self.__start_time:
            dt = datetime.strptime(str(self.__start_date), YYYY_MM_DD_FORMAT)
            dt_s = dt.strftime(YYYY_MM_DD_FORMAT)
            tm = datetime.strptime(str(self.__start_time), HH_MM_SS_FORMAT)
            tm_s = tm.strftime(HH_MM_SS_FORMAT)
            # now append the date and time together and set start_date_time
            self.__start_date_time = \
                datetime.strptime(str(dt_s) + " " + str(tm_s),
                                  YYYY_MM_DD_HH_MM_SS_FORMAT)

        if self.__end_date_time:
            dt = datetime.strptime(str(self.__end_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
            self.__end_date = dt.strftime(YYYY_MM_DD_FORMAT)
            self.__end_time = dt.strftime(HH_MM_SS_FORMAT)
        elif self.__end_date and self.__end_time:
            dt = datetime.strptime(str(self.__end_date), YYYY_MM_DD_FORMAT)
            dt_s = dt.strftime(YYYY_MM_DD_FORMAT)
            tm = datetime.strptime(str(self.__end_time), HH_MM_SS_FORMAT)
            tm_s = tm.strftime(HH_MM_SS_FORMAT)
            # now append the date and time together and set end_date_time
            self.__end_date_time = \
                datetime.strptime(str(dt_s) + " " + str(tm_s),
                                  YYYY_MM_DD_HH_MM_SS_FORMAT)

        self.__set_duration()

    def __set_start_date_time_values(self, source):
        # set corresponding values depending on what changed
        # and what is available

        if source == "start_date_time":
            if self.__start_date_time:
                dt1 = datetime.strptime(str(self.__start_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
                self.__start_date = dt1.strftime(YYYY_MM_DD_FORMAT)
                self.__start_time = dt1.strftime(HH_MM_SS_FORMAT)
            else:
                # start_date_time was set to None so do the same for date and time
                self.__start_date = ''
                self.__start_time = ''
        elif self.__start_date and self.__start_time:
            # if both start_date and start_time exist use those to set start_date_time
            dt = datetime.strptime(str(self.__start_date), YYYY_MM_DD_FORMAT)
            dt_s = dt.strftime(YYYY_MM_DD_FORMAT)
            tm = datetime.strptime(str(self.__start_time), HH_MM_SS_FORMAT)
            tm_s = tm.strftime(HH_MM_SS_FORMAT)
            # now append the date and time together and set start_date_time
            self.__start_date_time = \
                datetime.strptime(str(dt_s) + " " + str(tm_s),
                                  YYYY_MM_DD_HH_MM_SS_FORMAT)

        elif source == "start_date":
            if not self.__start_date:
                # the caller set start_date to None so set start_date_time = None
                # leave start_time alone
                self.__start_date_time = ''

        elif source == "start_time":
            if not self.__start_time:
                # the caller set start_time to None so set start_date_time = None
                # leave start_date alone
                self.__start_date_time = ''

        self.__set_duration()

    def __set_end_date_time_values(self, source):
        # set corresponding values depending on what changed
        # and what is available

        if source == "end_date_time":
            if self.__end_date_time:
                dt1 = datetime.strptime(str(self.__end_date_time), YYYY_MM_DD_HH_MM_SS_FORMAT)
                self.__end_date = dt1.strftime(YYYY_MM_DD_FORMAT)
                self.__end_time = dt1.strftime(HH_MM_SS_FORMAT)
            else:
                # end_date_time was set to None so do the same for date and time
                self.__end_date = ''
                self.__end_time = ''
        elif self.__end_date and self.__end_time:
            # if both end_date and end_time exist use those to set end_date_time
            dt = datetime.strptime(str(self.__end_date), YYYY_MM_DD_FORMAT)
            dt_s = dt.strftime(YYYY_MM_DD_FORMAT)
            tm = datetime.strptime(str(self.__end_time), HH_MM_SS_FORMAT)
            tm_s = tm.strftime(HH_MM_SS_FORMAT)
            # now append the date and time together and set end_date_time
            self.__end_date_time = \
                datetime.strptime(str(dt_s) + " " + str(tm_s),
                                  YYYY_MM_DD_HH_MM_SS_FORMAT)

        elif source == "end_date":
            if not self.__end_date:
                # the caller set end_date to '' so set end_date_time = ''
                # leave end_time alone
                self.__end_date_time = ''

        elif source == "end_time":
            if not self.__end_time:
                # the caller set end_time to None so set end_date_time = None
                # leave end_date alone
                self.__end_date_time = ''

        self.__set_duration()

    def __str__(self):
        lines = []
        dt_string = ("Start: " + str(self.start_date_time) + " ") if self.start_date_time else ''
        if dt_string != '':
            lines.append(dt_string)

        dt_string = ("End: " + str(self.end_date_time) + " ") if self.end_date_time else ''
        if dt_string != '':
            lines.append(dt_string)

        if self.__duration_in_seconds > 0:
            lines.append("Duration: " + self.duration_string)

        if len(lines) > 0:
            return '\n'.join(lines)
        else:
            return ''

    def __fire_invalid_data_callback_func(self, message):
        if self.__invalid_data_callback_func:
            self.__invalid_data_callback_func(message=message)
