###############################################################################
# exhaust.py
# Exhaust.py opens a csv file and imports the raw data, changes the time stamps
# and plots the data. 
# 
# Created by RJ Stevens
# 6/18/2014
# v1.1
###############################################################################

#import libraries
import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
from StringIO import StringIO
from dateutil import parser

# set path to file
file='/home/stevens/code/CLASS.csv'

# python opens a csv file one line at a time. The first step is to read the
# header and then skip a blank line and then iteratively collect the data.

# get variable names from header
csvfile = open( file, "rb" ) #open csv file
reader = csv.reader(csvfile) #create reader for file
head = reader.next() #read first row
blank = reader.next() #skips blank row
blank2 = reader.next()
names=[] #create names array since append is the easiest way to iterate through
#         the reader. This will be done for all arrays for data.

for item in head:
	names.append(unicode(item, errors='ignore'))
dt=[]
date=[]
# For this file the timestamp is column 1, so counting from 0, I only grab 
# column 0. 
for line in reader:
	dt.append(line[0])
for time in dt:
	date.append(parser.parse(time)) #use parser to create datetime objects

mpl_date = mpl.dates.date2num(date) #turn datetime objects into doubles

# For this file the time is column one and the data is 2 and 3. Starting from
# 0, the data is column 1 and 2, so I grab only those two for the data matrix.
data1 = np.genfromtxt(file, delimiter = ',',skip_header=3,usecols=(1))
data2 = np.genfromtxt(file, delimiter = ',',skip_header=3,usecols=(2))

# For this dataset only every 4th row has data. so slice out the 4th rows
date2=date[0::4]
data11=data1[0::4]
data22=data2[0::4]

#for i in range(len(data1)):
y1=data11[:]
y2=data22[:]
x=date2[:]
fig = plt.figure()
ax1= fig.add_subplot(111)
ax1.plot(x,y1);
ax1.set_ylabel(names[1]);
ax1.set_ylim([10,80])
ax2 = ax1.twinx()
ax2.plot(x,y2, 'r')
ax2.set_ylim([10,80])
ax2.set_ylabel(names[2]);
plt.title('test')
ax2.set_xlabel('Date')
dateFmt = mpl.dates.DateFormatter('%Y-%m-%d')
ax2.xaxis.set_major_formatter(dateFmt)
MonthLoc=mpl.dates.MonthLocator()
WeekLoc=mpl.dates.WeekdayLocator()
ax2.xaxis.set_major_locator(MonthLoc)
ax2.xaxis.set_minor_locator(WeekLoc)
plt.show()
#	fig.savefig('C:\Users\Stevens\Desktop\cchrc_plots\\' + names[i] + '.png', dpi=fig.dpi)
#	print i
#	return []


