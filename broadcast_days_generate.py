list = []
for y in range(2018,2031):
	for x in range(1,12):
		import calendar
		month_range = calendar.monthrange(y,x)
		import datetime
		date_corrected = datetime.date(y,x, 1)
		delta = (calendar.MONDAY - month_range[0]) % 7
		curr_broadcast_monday = date_corrected + datetime.timedelta(days = delta)
		if(curr_broadcast_monday.day!=1):
			curr_broadcast_monday = curr_broadcast_monday - datetime.timedelta(days = 7)
		import calendar
		month_range_1 = calendar.monthrange(y,x+1)
		import datetime
		date_corrected_1 = datetime.date(y,x+1, 1)
		delta_1 = (calendar.MONDAY - month_range_1[0]) % 7
		next_broadcast_monday = date_corrected_1 + datetime.timedelta(days = delta_1)
		if(next_broadcast_monday.day!=1):
			next_broadcast_monday = next_broadcast_monday - datetime.timedelta(days = 7)
		curr_broadcast_sunday = next_broadcast_monday - datetime.timedelta(days = 1)
		list.append((str(y),str(x),str(curr_broadcast_monday),str(curr_broadcast_sunday)))

import csv

with open('file.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['year','month','broadcast_monday','broadcast_sunday'])
    for row in list:
        csv_out.writerow(row)