from Event import Event

date_string1 = "2022-01-23"
date_string2 = "2019-04-14"
time_string1 = "17:00:01-0700"
time_string2 = "12:32:16-0700"
date_time1_string = '2022-01-23 17:00:01-07:00'
date_time2_string = '2019-04-14 12:32:16-07:00'

event = Event(None, "My event", "event Long", date_string2, time_string2, date_string1, time_string1)

print(event.start_date)
print(event.end_date)
print(event.start_date_time)
print(event.end_date_time)
print(event.duration_in_seconds)
print(event.duration_string)
print(event.event_time_span)
# 2019-04-14
# 2022-01-23
# 2019-04-14 12:32:16-07:00
# 2022-01-23 17:00:01-07:00
# 1015 days, 4 hours, 27 minutes, 45 seconds
# Start: 2019-04-14 12:32:16-07:00
# End: 2022-01-23 17:00:01-07:00
# Duration: 1015 days, 4 hours, 27 minutes, 45 seconds

# bump start date by 1
event.start_date = "2019-04-15"
print(event.start_date)
print(event.end_date)
print(event.start_date_time)
print(event.end_date_time)
print(event.duration_in_seconds)
print(event.duration_string)
print(event.event_time_span)
# 2019-04-15
# 2022-01-23
# 2019-04-15 12:32:16-07:00
# 2022-01-23 17:00:01-07:00
# 1014 days, 4 hours, 27 minutes, 45 seconds
# Start: 2019-04-15 12:32:16-07:00
# End: 2022-01-23 17:00:01-07:00
# Duration: 1014 days, 4 hours, 27 minutes, 45 seconds