#! /usr/bin/env python


import numpy as np


def get_sundays(n, m):

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
	for year in range(1900, m + 1, 1):

		if year % 400 == 0:		
			Feb = 29
		elif year % 4 == 0 and year % 100 == 0:
			Feb = 28
		elif year % 4 == 0:
			Feb = 29	
		else:
			Feb = 28

		months = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
		# month_no = 0
		for month in months:
			# month_no = month_no + 1
			for day in range(month):
				day = day + 1	# shift counter by one to start days on 1st
				day_count = day_count + 1
				if day_count % 7 == 0 and day == 1 and year >= n:
						total_sundays = total_sundays + 1
						# print year, month_no


	print("The number of Sundays that fell on the first of the month during 1 Jan " + str(n) + " to 31 Dec " + str(m) + " was " + str(total_sundays) + ".")

get_sundays(1901, 2000)	