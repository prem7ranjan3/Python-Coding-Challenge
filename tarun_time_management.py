data_set = {"startTime": "11:00AM", "endTime": "11:30AM"}, {"startTime": "11:30AM", "endTime": "12:30AM"}, {
    "startTime": "01:00PM", "endTime": "01:30PM"}, {"startTime": "01:30PM", "endTime": "03:30PM"}, {
               "startTime": "02:00PM", "endTime": "02:30PM"}, {"startTime": "02:00PM", "endTime": "04:30PM"}
total_size = len(data_set)

for i in data_set:
    print(i.values())
