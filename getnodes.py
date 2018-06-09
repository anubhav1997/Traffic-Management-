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
			


def get_finalnodes():
	

	threshold = 0.1
	
	# longitudes = []
	# latitude = []
	final_long = []
	final_lat = []
	final_nodes = []
	count =0
	
#	for filename in glob.glob('/home/anubhav/Desktop/IP/Node/*'):
	filename = 'final_nodes_all_inc_buses_543_up.xlsx'

	workbook = xlrd.open_workbook(filename, on_demand=True)
	sheet = workbook.sheet_by_index(0)
	arrayoflatitudes = sheet.col_values(1)	
	arrayoflongitudes = sheet.col_values(2)
	arraynodes = sheet.col_values(3)
	# longitudes = []
	# latitude = []
	

	filename = 'Stoppage_534UP.xlsx'

	workbook2 = xlrd.open_workbook(filename, on_demand=True)
	sheet2 = workbook2.sheet_by_index(0)
	arrayoflatitudes2 = sheet2.col_values(3)	
	arrayoflongitudes2 = sheet2.col_values(4)
	arraynodes2 = sheet2.col_values(5)

	# longitudes = []
	# latitude = []
	

	final_long = np.append(final_long,arrayoflongitudes).tolist()
	final_lat = np.append(final_lat, arrayoflatitudes).tolist()
	final_nodes = np.append(final_nodes, arraynodes).tolist()


	print final_nodes

	#x = input()

	node_refernce = []
	node_refernce.append(0)

	index = len(final_nodes)

	count+=1
	for i in range(1,len(arrayoflongitudes2)):
		key = 0
		for j in range(1,len(final_long)):
			import decimal
			D = decimal.Decimal
			coords_1 = (D(final_lat[j]),D(final_long[j]))
			coords_2 = (D(arrayoflatitudes2[i]),D(arrayoflongitudes2[i]))
			dist=geopy.distance.vincenty(coords_1, coords_2).km
			print dist

			if(dist<threshold):
				key = 1
				node_refernce.append(final_nodes[i])

		if(key==0):

			print 'heree'
			final_nodes.append(index)
			node_refernce.append(final_nodes[j+1])
			
			final_lat.append(arrayoflatitudes2[i])
			final_long.append(arrayoflongitudes2[i])
			index+=1



	print final_nodes
	print final_lat
	print final_long
	df = pd.DataFrame({'Latitude': final_lat[1:],'Longitude': final_long[1:], 'Node': final_nodes[1:]})
	writer = pd.ExcelWriter('final_final_nodes_all_inc_buses.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()
	total_nodes = index




	print len(arraynodes2)
	print len(node_refernce)
	print node_refernce

	print arraynodes2


	df = pd.DataFrame({'actual Node': arraynodes2[1:],'Nodes': node_refernce[1:]})
	writer = pd.ExcelWriter('Stoppage_Ref_Nodes_534_up.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()




	
get_finalnodes()




