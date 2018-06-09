import glob
import xlrd
import geopy.distance
import pandas as pd
import numpy as np
from datetime import datetime
import datetime as dt
import time

# workbook = xlrd.open_workbook('.xlsx', on_demand=True)
# array = []
# for filename in glob.glob('/home/anubhav/Desktop/IP/data/*'):
# 	print filename[-6]
# 	if(filename[-6]=='0'):
# 		workbook2 = xlrd.open_workbook(filename, on_demand=True)
		
		
workbook = xlrd.open_workbook('nodes_classify.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)
node = sheet.col_values(3)
arrayspeed = sheet.col_values(4)
arrayoflatitudes = sheet.col_values(1)
print arrayoflatitudes

arrayoflongitudes = sheet.col_values(2)
time1 = sheet.col_values(5)
x = sheet.row_values(10)
# print x
final_nodes = []
longi = []
lat = []
speed = []
timeeee = []
node_final = []
print node[1:] 
for i in range(1, len(node)-1):
	# print node[i]
	prev = node[i]
	if(int(node[i+1])==int(int(node[i])+1)):
		longi.append(arrayoflongitudes[i])
		lat.append(arrayoflatitudes[i])
		speed.append(0)
		timeeee.append(time1[i])
		node_final.append(node[i])
		# node.append(j)
		# print 'hey'
	elif(i==(len(node)-1) and node[i+1]==node[i]):
		longi.append(arrayoflongitudes[i])
		lat.append(arrayoflatitudes[i])
		# speed.append(0)
		timeeee.append(time1[i])
		node_final.append(node[i])

speed = []
for i in range(len(longi)-1):
	FMT = '%H:%M:%S'
	# tdelta = datetime.strptime(time[i+1], FMT) - datetstr(ime.str)ptime(time[i], FMT)
	# t = time[i] - time[i+1]
	# print timeeee[i]
	t1 = datetime.strptime(timeeee[i].split('.')[0],'%H:%M:%S')
	t2 = datetime.strptime(timeeee[i+1].split('.')[0],'%H:%M:%S')
	t = t2-t1
	t = time.strptime(str(t), '%H:%M:%S')
	t = dt.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
	coords_1 = (lat[i], longi[i])
	coords_2 = (lat[i+1], longi[i+1])
	dis = geopy.distance.vincenty(coords_1, coords_2).km
	print dis
	print t

	speed.append(dis*3600/t)
	# print speed
# s1 = '10:33:26'
# s2 = '11:15:49' # for example

speed.append(0)


df = pd.DataFrame({'Latitude': lat,'Longitude': longi, 'Node': node_final, 'Speed': speed, 'Time': timeeee})
writer = pd.ExcelWriter('nodes_classify_final1.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df.to_excel(writer, sheet_name='Sheet 1')
writer.save()

import psycopg2
import gmplot

print type(lat[0])

lat2 = [float(i) for i in lat]
longi2 = [float(i) for i in longi]

print type(lat2[0])

gmap = gmplot.GoogleMapPlotter(lat2[0],longi2[0],18)
gmap.scatter(lat2, longi2, 'cornflowerblue', edge_width=10, title = 'heyy', marker=True)

# Write the map in an HTML file
gmap.draw('map.html')

