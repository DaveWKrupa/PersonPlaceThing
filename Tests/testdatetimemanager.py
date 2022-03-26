from DateTimeManager import DateTimeManager

dtm = DateTimeManager()


date_string1 = "2022-01-23"
date_string2 = "2019-04-14"
time_string1 = "17:00:01-0700"
time_string2 = "12:32:16-0700"
date_time1_string = '2022-01-23 17:00:01-07:00'
date_time2_string = '2019-04-14 12:32:16-07:00'

print("First test load a start_date_time value to test start date functionality")
dtm.start_date_time = date_time1_string
assert str(dtm.start_date_time) == date_time1_string, "start_date_time failed to load correctly"
assert str(dtm.start_date) == date_string1, "start_date does not match expected value"
assert str(dtm.start_time) == time_string1, "start_time does not match expected value"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"
# 2022-01-23 17:00:00-0700
# 2022-01-23
# 17:00:00-0700
# 0 days, 0 hours, 0 minutes, 0 seconds

print("Test setting start_date_time to None")
dtm.start_date_time = None

assert not dtm.start_date_time, "start_date_time not None as expected"
assert not dtm.start_date, "start_date not None as expected"
assert not dtm.start_time, "start_time not None as expected"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"

print("Test setting just the start_date")
dtm.start_date = date_string2
assert dtm.start_date_time == '', "start_date_time not None as expected"
assert str(dtm.start_date) == date_string2, "start_date does not match expected value"
assert dtm.start_time == '', "start_time not None as expected"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"

print("Test setting start_time with date_time already set")
dtm.start_time = time_string2
assert str(dtm.start_date_time) == date_time2_string, "start_date_time does not match expected value"
assert str(dtm.start_date) == date_string2, "start_date does not match expected value"
assert str(dtm.start_time) == time_string2, "start_time does not match expected value"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"

print("Test end date by setting end_date_time")
dtm.end_date_time = date_time2_string
assert str(dtm.end_date_time) == date_time2_string, "end_date_time failed to load correctly"
assert str(dtm.end_date) == date_string2, "end_date does not match expected value"
assert str(dtm.end_time) == time_string2, "end_time does not match expected value"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"

print("Set to None using end_date_time")
dtm.end_date_time = None
assert not dtm.end_date_time, "end_date_time not None as expected"
assert not dtm.end_date, "end_date not None as expected"
assert not dtm.end_time, "end_time not None as expected"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"

print("add end date")
dtm.end_date = date_string1
assert str(dtm.end_date_time) == '', "end_date_time failed to load correctly"
assert str(dtm.end_date) == date_string1, "end_date does not match expected value"
assert str(dtm.end_time) == '', "end_time does not match expected value"
assert dtm.duration_string == "0 days, 0 hours, 0 minutes, 0 seconds", "duration_string not set correctly"

print("add end time")
dtm.end_time = time_string1
assert str(dtm.end_date_time) == date_time1_string, "end_date_time failed to load correctly"
assert str(dtm.end_date) == date_string1, "end_date does not match expected value"
assert str(dtm.end_time) == time_string1, "end_time does not match expected value"
assert dtm.duration_string == "1015 days, 4 hours, 27 minutes, 45 seconds", "duration_string not set correctly"
print(" ")
print(str(dtm))


