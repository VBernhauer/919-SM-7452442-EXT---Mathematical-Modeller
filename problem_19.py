#! /usr/bin/env python

import numpy as np


Jan = 31
Mar = 31
Apr = 30
May = 31
Jun = 30
Jul = 31
Aug = 31
Sep = 30
Oct = 31
Nov = 30
Dec = 31

day_count = 0
total_sundays = 0
for year in range(1900, 2001, 1):

	if year % 400 == 0:		
			Feb = 29
	elif year % 4 == 0 and year % 100 == 0:
			Feb = 28
	elif year % 4 == 0:
		Feb = 29	
	else:
		Feb = 28

	months = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
	for month in months:
		for day in range(month):
			day = day + 1
			day_count = day_count + 1
			if day_count % 7 == 0 and day == 1 and year > 1900:
					total_sundays = total_sundays + 1


print("The number of Sundays that fell on the first of the month during the \
twentieth century (1 Jan 1901 to 31 Dec 2000) was " + str(total_sundays))