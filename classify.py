import xlrd
import geopy.distance
import pandas as pd

def prog2():
	longi = []
	lat = []
	node = []
	speed = []
	time = []
	threshold=0.1 #kms
	workbook = xlrd.open_workbook('position_2017-12-16_0.xlsx', on_demand=True)
	workbook1 = xlrd.open_workbook('nodes1.xlsx', on_demand=True)
	# workbook2=xlrd.open_workbook('nodes_classify.xlsx',on_demand=True)
	sheet1 = workbook1.sheet_by_index(0)
	arrayofnodelat = sheet1.col_values(0)
	arrayofnodelong = sheet1.col_values(1)
	num=0
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

	for i in range(2,len(arrayoflongitudes)):
		
		for j in range(1,len(arrayofnodelong)):
			
			coords_1 = (arrayoflatitudes[i],arrayoflongitudes[i])
			coords_2 = (arrayofnodelat[j],arrayofnodelong[j])
			dist=geopy.distance.vincenty(coords_1, coords_2).km
			if(dist<threshold):
				longi.append(arrayoflongitudes[i])
				lat.append(arrayoflatitudes[i])
				speed.append(speed1[i])
				time.append(time1[i])
				node.append(j)
				break

		df = pd.DataFrame({'Latitude': lat,'Longitude': longi, 'Node': node, 'Speed': speed, 'Time': time})
		writer = pd.ExcelWriter('nodes_classify2.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
		df.to_excel(writer, sheet_name='Sheet 1')
		# workbook2.add_sheet('Sheet'+str(num+1))	
	# Close the Pandas Excel writer and output the Excel file.
	writer.save()

		
prog2()

