
import glob
import xlrd
import geopy.distance
import pandas as pd
import numpy as np
from datetime import datetime
import datetime as dt
import time
import os
import decimal

def prog2(filename, nodes):
	longi = []
	lat = []
	node = []
	speed = []
	timee = []
	threshold=0.3 #kms
	# workbook = xlrd.open_workbook('position_2017-12-16_0.xlsx', on_demand=True)
	# workbook1 = xlrd.open_workbook('nodes1.xlsx', on_demand=True)
	
	workbook = xlrd.open_workbook(filename, on_demand=True)
	workbook1 = xlrd.open_workbook(nodes, on_demand=True)
	
	# workbook2=xlrd.open_workbook('nodes_classify.xlsx',on_demand=True)
	sheet1 = workbook1.sheet_by_index(0)
	arrayofnodelat = sheet1.col_values(0)
	arrayofnodelong = sheet1.col_values(1)
	num=0
	# print arrayofnodelong
	# print arrayofnodelat
	sheet = workbook.sheet_by_index(num)
	arrayoflatitudes = sheet.col_values(1)	
	arrayoflongitudes = sheet.col_values(2)
	speed1 = sheet.col_values(3)
	time1 = sheet.col_values(4)
	# print(arrayoflongitudes)
	# print(arrayoflatitudes)
	# Create a Pandas Excel writer using XlsxWriter as the engine.
	# del longi[:]
	# del lat[:]
	# del node[:]
	# del speed[:]
	# del time[:]
	if(len(arrayoflongitudes)>2):
			
		for i in range(2,len(arrayoflongitudes)):
			
			for j in range(1,len(arrayofnodelong)):
				# print 'heyy'
				coords_1 = (arrayoflatitudes[i],arrayoflongitudes[i])
				coords_2 = (arrayofnodelat[j],arrayofnodelong[j])
				dist=geopy.distance.vincenty(coords_1, coords_2).km
				print dist
				if(dist<threshold):
					print 'heree' 
					longi.append(arrayoflongitudes[i])
					lat.append(arrayoflatitudes[i])
					speed.append(speed1[i])
					timee.append(time1[i])
					node.append(j)
					break

			df = pd.DataFrame({'Latitude': lat,'Longitude': longi, 'Node': node, 'Speed': speed, 'Time': timee})
			writer = pd.ExcelWriter('nodes_classify2.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
			df.to_excel(writer, sheet_name='Sheet 1')
			# workbook2.add_sheet('Sheet'+str(num+1))	
		# Close the Pandas Excel writer and output the Excel file.
		writer.save()


for filename in glob.glob('/home/anubhav/Desktop/IP/data/*'):
	print filename

	nodes = 
	
	temp_final_file = '/home/anubhav/Desktop/IP/Avg_Time/avg_time_bus_' + filename[-17:-5] + '.xlsx'
	map_path = '/home/anubhav/Desktop/IP/Maps/Map_' + filename[-17:-5] + '.html'
	
	print temp_nodes

	if(os.path.isfile(temp_nodes)):
		try: 

			prog2(filename, temp_nodes)
			
			workbook = xlrd.open_workbook('nodes_classify2.xlsx', on_demand=True)
			sheet = workbook.sheet_by_index(0)
			node = sheet.col_values(3)
			arrayspeed = sheet.col_values(4)
			arrayoflatitudes = sheet.col_values(1)
			# print arrayoflatitudes

			arrayoflongitudes = sheet.col_values(2)
			time1 = sheet.col_values(5)
			# x = sheet.row_values(10)
			# print x
			final_nodes = []
			longi = []
			lat = []
			speed = []
			timeeee = []
			node_final = []
			print node[1:] 
			if(len(arrayoflatitudes)!=1 and len(node[1:] )!=0):

				for i in range(1, len(node)-1):
					# print node[i]
					prev = node[i]
					if(int(node[i+1])!=int(int(node[i]))):
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

				print len(longi)
				print len(lat)
				print len(node_final)
				print len(timeeee)
				print len(speed)
				print len(speed)

				print temp_final_file
				if(len(longi)!=0 and len(lat)!=0 and len(node_final)!=0 and len(timeeee)!=0):

					df = pd.DataFrame({'Latitude': lat,'Longitude': longi, 'Node': node_final, 'Speed': speed, 'Time': timeeee})
					writer = pd.ExcelWriter(temp_final_file, engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
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
					gmap.draw(map_path)

		except IOError:
		    print('An error occurred trying to read the file.')

		except ValueError:
		    print('Non-numeric data found in the file.')

		except ImportError:
		    print "NO module found"

		except EOFError:
		    print('Why did you do an EOF on me?')

		except KeyboardInterrupt:
		    print('You cancelled the operation.')

		except:
		    print('An error occurred.')
