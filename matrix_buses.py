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



def prog3(filename, nodes):
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
	arrayofnodelat = sheet1.col_values(1)
	arrayofnodelong = sheet1.col_values(2)
	num=0
	# print arrayofnodelong
	# print arrayofnodelat
	sheet = workbook.sheet_by_index(num)
	arrayoflatitudes = sheet.col_values(1)
	arrayoflongitudes = sheet.col_values(2)
	speed1 = sheet.col_values(4)
	time1 = sheet.col_values(5)
	# print(arrayoflongitudes)
	# print(arrayoflatitudes)
	# Create a Pandas Excel writer using XlsxWriter as the engine.
	# del longi[:]
	# del lat[:]
	# del node[:]
	# del speed[:]
	# del time[:]
	# if(len(arrayoflongitudes)>2):
			
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





# for filename in glob.glob('/home/anubhav/Desktop/IP/data/*'):
# 	print filename
# 	if(filename[-7]!='_'):

# 		temp_nodes = '/home/anubhav/Desktop/IP/Node/Nodes_bus_' + filename[-7]+filename[-6] + '.xlsx'
# 		temp_final_file = '/home/anubhav/Desktop/IP/Avg_Time/avg_time_bus_' + filename[-18:-5] + '.xlsx'
# 		map_path = '/home/anubhav/Desktop/IP/Maps/Map_' + filename[-18:-5] + '.html'
# 	else:
# 		temp_nodes = '/home/anubhav/Desktop/IP/Node/Nodes_bus_' + filename[-6] + '.xlsx'
# 		temp_final_file = '/home/anubhav/Desktop/IP/Avg_Time/avg_time_bus_' + filename[-17:-5] + '.xlsx'
# 		map_path = '/home/anubhav/Desktop/IP/Maps/Map_' + filename[-17:-5] + '.html'
		
# 	print temp_nodes
# 	if(os.path.isfile(temp_nodes)):
# 		try: 

# 			prog2(filename, temp_nodes)
			
# 			workbook = xlrd.open_workbook('nodes_classify2.xlsx', on_demand=True)
# 			sheet = workbook.sheet_by_index(0)
# 			node = sheet.col_values(3)
# 			arrayspeed = sheet.col_values(4)
# 			arrayoflatitudes = sheet.col_values(1)
# 			# print arrayoflatitudes

# 			arrayoflongitudes = sheet.col_values(2)
# 			time1 = sheet.col_values(5)
# 			# x = sheet.row_values(10)
# 			# print x
# 			final_nodes = []
# 			longi = []
# 			lat = []
# 			speed = []
# 			timeeee = []
# 			node_final = []
# 			print node[1:] 
# 			if(len(arrayoflatitudes)!=1 and len(node[1:] )!=0):

# 				for i in range(1, len(node)-1):
# 					# print node[i]
# 					prev = node[i]
# 					if(int(node[i+1])!=int(int(node[i]))):
# 						longi.append(arrayoflongitudes[i])
# 						lat.append(arrayoflatitudes[i])
# 						speed.append(0)
# 						timeeee.append(time1[i])
# 						node_final.append(node[i])
# 						# node.append(j)
# 						# print 'hey'
# 					elif(i==(len(node)-1) and node[i+1]==node[i]):
# 						longi.append(arrayoflongitudes[i])
# 						lat.append(arrayoflatitudes[i])
# 						# speed.append(0)
# 						timeeee.append(time1[i])
# 						node_final.append(node[i])

# 				speed = []
# 				for i in range(len(longi)-1):
# 					FMT = '%H:%M:%S'
# 					# tdelta = datetime.strptime(time[i+1], FMT) - datetstr(ime.str)ptime(time[i], FMT)
# 					# t = time[i] - time[i+1]
# 					# print timeeee[i]
# 					t1 = datetime.strptime(timeeee[i].split('.')[0],'%H:%M:%S')
# 					t2 = datetime.strptime(timeeee[i+1].split('.')[0],'%H:%M:%S')
# 					t = t2-t1
# 					t = time.strptime(str(t), '%H:%M:%S')
# 					t = dt.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
# 					coords_1 = (lat[i], longi[i])
# 					coords_2 = (lat[i+1], longi[i+1])
# 					dis = geopy.distance.vincenty(coords_1, coords_2).km
# 					print dis
# 					print t

# 					speed.append(dis*3600/t)
# 					# print speed
# 				# s1 = '10:33:26'
# 				# s2 = '11:15:49' # for example

# 				speed.append(0)

# 				print len(longi)
# 				print len(lat)
# 				print len(node_final)
# 				print len(timeeee)
# 				print len(speed)
# 				print len(speed)

# 				print temp_final_file
# 				if(len(longi)!=0 and len(lat)!=0 and len(node_final)!=0 and len(timeeee)!=0):

# 					df = pd.DataFrame({'Latitude': lat,'Longitude': longi, 'Node': node_final, 'Speed': speed, 'Time': timeeee})
# 					writer = pd.ExcelWriter(temp_final_file, engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
# 					df.to_excel(writer, sheet_name='Sheet 1')
# 					writer.save()

# 					import psycopg2
# 					import gmplot

# 					print type(lat[0])

# 					lat2 = [float(i) for i in lat]
# 					longi2 = [float(i) for i in longi]

# 					print type(lat2[0])

# 					gmap = gmplot.GoogleMapPlotter(lat2[0],longi2[0],18)
# 					gmap.scatter(lat2, longi2, 'cornflowerblue', edge_width=10, title = 'heyy', marker=True)
					
# 					# Write the map in an HTML file
# 					gmap.draw(map_path)

# 		except IOError:
# 		    print('An error occurred trying to read the file.')

# 		except ValueError:
# 		    print('Non-numeric data found in the file.')

# 		except ImportError:
# 		    print "NO module found"

# 		except EOFError:
# 		    print('Why did you do an EOF on me?')

# 		except KeyboardInterrupt:
# 		    print('You cancelled the operation.')

# 		except:
# 		    print('An error occurred.')

total_nodes=0


def get_finalnodes():
	threshold = 0.1
	
	# longitudes = []
	# latitude = []
	final_long = []
	final_lat = []
	final_nodes = []
	count =0
	index = 1
	for filename in glob.glob('/home/anubhav/Desktop/IP/Node/*'):
		workbook = xlrd.open_workbook(filename, on_demand=True)
		sheet = workbook.sheet_by_index(0)
		arrayoflatitudes = sheet.col_values(0)	
		arrayoflongitudes = sheet.col_values(1)
		# longitudes = []
		# latitude = []
		
		if(count==0):

			for i in range(1, len(arrayoflongitudes)):

				final_nodes.append(index)
				final_lat.append(arrayoflatitudes[i])
				final_long.append(arrayoflongitudes[i])
				index+=1
				count+=1
		else:
			# print all_lat
			count+=1
			for i in range(1,len(arrayoflongitudes)):
				key = 0
				for j in range(0,len(final_long)):
					# print type(arrayoflongitudes[j])
					
					# print arrayoflatitudes[j]
					# x = float(arrayoflatitudes[j])
					# print arrayoflongitudes[j]
					# # print arrayoflongitudes[i][:-1]

					# y = arrayoflongitudes[j]
					import decimal
					D = decimal.Decimal
					coords_1 = (D(final_lat[j]),D(final_long[j]))
					coords_2 = (D(arrayoflatitudes[i]),D(arrayoflongitudes[i]))
					dist=geopy.distance.vincenty(coords_1, coords_2).km
					print dist

					if(dist<threshold):
						key = 1

				if(key==0):

					print 'heree'
					final_nodes.append(index)
					final_lat.append(arrayoflatitudes[i])
					final_long.append(arrayoflongitudes[i])
					index+=1


	print final_nodes
	print final_lat
	print final_long
	df = pd.DataFrame({'Latitude': final_lat,'Longitude': final_long, 'Node': final_nodes})
	writer = pd.ExcelWriter('final_nodes_all.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()
	total_nodes = index
	# x = input()

def get_finalnodes2():
	threshold = 0.3
	
	# longitudes = []
	# latitude = []
	final_long = []
	final_lat = []

	final_long2 = []
	final_lat2 = []
	final_node_ref = []
	final_nodes = []
	# count =0
	index = 1
	#for filename in glob.glob('/home/anubhav/Desktop/IP/Node/*'):
	filename = 'list_all_values2.xlsx'

	workbook = xlrd.open_workbook(filename, on_demand=True)
	sheet = workbook.sheet_by_index(0)
	arrayoflatitudes = sheet.col_values(1)	
	arrayoflongitudes = sheet.col_values(2)
	node = sheet.col_values(3)
	speed_array = sheet.col_values(4)
	time_array = sheet.col_values(5)
	
	filename = 'final_nodes_all.xlsx'

	workbook2 = xlrd.open_workbook(filename, on_demand=True)
	sheet2 = workbook2.sheet_by_index(0)
	arrayoflat = sheet2.col_values(1)	
	arrayoflong = sheet2.col_values(2)
	arrayofnode = sheet2.col_values(3)



	# longitudes = []
	# latitude = []
	
	# if(count==0):

	###############
	# i = 1
	# while(node[i]! = '[(0,0), (0,0)]' )
	# 	final_nodes.append(index)
	# 	final_lat.append(arrayoflatitudes[i])
	# 	final_long.append(arrayoflongitudes[i])
	# 	final_node_ref.append(node[i])
	# 	index+=1
	# 	count+=1
	# 	i+=1
	################
	
	ref = []

	# else:
		# print all_lat
	# count+=1
	ref.append((0,0))

	for i in range(1,len(arrayoflongitudes)):
		key = 0
		temp1 = 0
		temp2 = 0
		
		if(node[i]!= '[(0,0), (0,0)]' and node[i]!= '[(0, 0), (0, 0)]'):

			for j in range(1,len(arrayoflat)):
				
				D = decimal.Decimal
				#coords_1 = (D(final_lat[j][0][0]),D(final_long[j][0][1]))

				coords_1 = (D(arrayoflat[j]), D(arrayoflong[j]))
				print coords_1
				# print node[i]
				# print node[i][0]
				# print node[i][0][1]
				list1 = node[i].split(", ")
				a = (list1[0].split("("))
				b = (list1[1].split(")"))
				c = (list1[2].split("("))
				d = (list1[3].split(")"))
				# print a[1]
				# print b[0] 
				# print c[1]
				# print d[0]

				# print a[1].split('\'')

				print a[1].split('\'')[1]
				print b[0].split('\'')[1]

				print 

				coords_2 = (D(a[1].split('\'')[1]),D(b[0].split('\'')[1]))
				dist=geopy.distance.vincenty(coords_1, coords_2).km
				
				coords_3 = (D(c[1].split('\'')[1]),D(d[0].split('\'')[1]))

				dist2=geopy.distance.vincenty(coords_1, coords_3).km
				
				print dist,dist2

				if(dist<=threshold):
					#key = 1
					temp1 = arrayofnode[j] 
				
				if(dist2<=threshold):
					#key = 1
					temp2 = arrayofnode[j] 

				print temp1, temp2 

				if(temp1!=0 and temp2!=0):
					break

			ref.append((temp1, temp2))


	print ref 
	# x = input()




		# if(key==0):

		# 	print 'heree'


			# final_nodes.append(index)
			# final_lat.append(arrayoflatitudes[i])
			# final_long.append(arrayoflongitudes[i])
			# index+=1

	final_ref = []
	final_ref_index = []
	final_ref_ref = []
	index = 1
	index2 = []
	for i in range(1,len(ref)):
		key = 0	
		for j in range(1, len(final_ref)):

			if(ref[i]==final_ref[j]):
				key = 1
				final_ref_index.append(index2[j])
				final_ref_ref.append(final_ref[j])
		if(key==0):
			index2.append(index)
			final_ref_index.append(index)
			final_node_ref.append(index)
			final_ref_ref.append(ref[i])
			index+=1
			final_ref.append(ref[i])
#		key =0


	df = pd.DataFrame({ 'Nodes': index2, 'Lat_long': final_ref})
	writer = pd.ExcelWriter('final_nodes_all2.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()

	flag = 0
	final_final = []
	final_final2 = []
	final_speed = []
	final_time = []
	for i in range(1, len(arrayoflongitudes)):
		if(node[i]!= '[(0,0), (0,0)]' and node[i]!= '[(0, 0), (0, 0)]'):
			final_final.append(final_ref_index[flag])
			final_final2.append(final_ref_ref[flag])
			final_speed.append(speed_array[i])
			final_time.append(time_array[i])

			flag+=1



	print final_nodes
	print final_lat
	print final_long

	df = pd.DataFrame({'Edge_Data': final_final2,'Edge_no': final_final, 'Speed': final_speed, 'Time': final_time})
	writer = pd.ExcelWriter('list_all_values3.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()
	total_nodes = index
	# x = input()



all_lat = []
all_long = []
all_speed = []
all_nodes = []
all_time = []



for filename in glob.glob('/home/anubhav/Desktop/IP/Avg_Time/*'):
	workbook = xlrd.open_workbook(filename, on_demand=True)
	sheet = workbook.sheet_by_index(0)
	node = sheet.col_values(3)
	arrayspeed = sheet.col_values(4)
	arrayoflatitudes = sheet.col_values(1)
	arrayoflongitudes = sheet.col_values(2)
	arraytime = sheet.col_values(5)
	all_lat = np.append(all_lat, arrayoflatitudes[1:])
	all_long = np.append(all_long, arrayoflongitudes[1:])
	all_speed = np.append(all_speed, arrayspeed[1:])
	#all_nodes = np.append(all_nodes, node[1:])
	
	for i in range(1,(len(node)-1)):
		all_nodes.append([(arrayoflatitudes[i],arrayoflongitudes[i]), (arrayoflatitudes[i+1],arrayoflongitudes[i+1])])
	all_nodes.append([(0,0), (0,0)])

	all_time = np.append(all_time, arraytime[1:])


df = pd.DataFrame({'Latitude': all_lat,'Longitude': all_long, 'Node': all_nodes, 'Speed': all_speed, 'Time': all_time})
writer = pd.ExcelWriter('list_all_values2.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df.to_excel(writer, sheet_name='Sheet 1')
writer.save()

x  = input()

get_finalnodes()

get_finalnodes2()


x = input()



def prog3(filename, nodes):
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
	arrayofnodelat = sheet1.col_values(1)
	arrayofnodelong = sheet1.col_values(2)
	num=0
	
	# print arrayofnodelong
	# print arrayofnodelat
	
	sheet = workbook.sheet_by_index(num)
	arrayoflatitudes = sheet.col_values(1)
	arrayoflongitudes = sheet.col_values(2)
	speed1 = sheet.col_values(4)
	time1 = sheet.col_values(5)
	# print(arrayoflongitudes)
	# print(arrayoflatitudes)
	# Create a Pandas Excel writer using XlsxWriter as the engine.
	# del longi[:]
	# del lat[:]
	# del node[:]
	# del speed[:]
	# del time[:]
	# if(len(arrayoflongitudes)>2):
			
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





# prog3('list_all_values2.xlsx', 'final_nodes_all.xlsx')


def getindex(hour,mn):
	hour-=4
	return int(hour*6 + (mn/10))


hour,minute=4,0
row = []


while(hour<24): #every 10 minutes
	if(minute<=40):
		row.append(str(hour)+':'+str(minute)+'-'+str(hour)+':'+str(minute+10))
		minute+=10
	else :
		row.append(str(hour)+':'+str(minute)+'-'+str(hour+1)+':'+str(0))
		minute=0
		hour+=1


matrix = []

# for i in range(len(row)):
# 	matrix.append([row[i]])

final_nodes = []



workbook = xlrd.open_workbook('list_all_values3.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)
node = sheet.col_values(2)
arrayspeed = sheet.col_values(3)
arrayoflatlong = sheet.col_values(1)
# arrayoflongitudes = sheet.col_values(2)
time1 = sheet.col_values(4)

total_nodes = 384

# x = input()

matrix = np.zeros((len(row), total_nodes))

temp = np.zeros((len(row), total_nodes))


for i in range(1, len(node)):
	print 'heyy', time1[i]
	time_start = time1[i]
	h1=int(time_start[0])*10+int(time_start[1])
	m1=int(time_start[3])*10+int(time_start[4])
	m1=int(m1/10)*10 #nearest 10
	print h1, m1
	index = getindex(h1, m1)



	print index

	print row[index]
	#x = input()

	# print node[i]
	# print len(temp)
	# print len(node)

	temp[index, int(node[i])] = temp[index, int(node[i])] + 1
	
	matrix[int(index), int(node[i])] = float(arrayspeed[i])*(1/temp[int(index), int(node[i])]) + (float(matrix[int(index), int(node[i])])*(temp[index, int(node[i])] -1)/(temp[int(index), int(node[i])]))
	
	print type(temp[index, int(node[i])])
	
	# x = input()


print matrix 

print temp


df1 = pd.DataFrame({'Nodes': [i for i in range(total_nodes+1)]})
df = pd.DataFrame({'Nodes': [i for i in range(total_nodes+1)]})

final_matrix = []
final_freq = []

for i in range(len(row)):
	print 'heyy'
	t2_temp = np.append(row[i], temp[i])


	t_temp = np.append(row[i], matrix[i])
	# print t_temp
	# print len([i for i in range(38)])
	# print len(t2_temp)
	df[i]=t_temp
	df1[i]=t2_temp


writer = pd.ExcelWriter('matrix.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df.to_excel(writer, sheet_name='Sheet 1')

writer = pd.ExcelWriter('Freq_matrix.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df1.to_excel(writer, sheet_name='Sheet 1')

