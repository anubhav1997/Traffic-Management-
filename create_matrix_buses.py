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

def get_all_data():

	all_long = []
	all_lat = []
	all_nodes = []
	all_speed = []
	all_time = []

	filename1 = 'Stoppage_Ref_Nodes_425.xlsx'
	workbook2 = xlrd.open_workbook(filename1, on_demand=True)
	sheet2 = workbook2.sheet_by_index(0)
	arrayofnode2 = sheet2.col_values(1)
	
	for filename in glob.glob('/home/anubhav/Desktop/IP/Final/425_final/*'):
		workbook = xlrd.open_workbook(filename, on_demand=True)
		sheet = workbook.sheet_by_index(0)
		arrayofnode = sheet.col_values(2)
		arrayspeed = sheet.col_values(1)
		# arrayoflatitudes = sheet.col_values(1)
		# arrayoflongitudes = sheet.col_values(2)
		arraytime = sheet.col_values(3)
		#all_nodes = np.append(all_nodes, node[1:])


		for i in range(1,(len(arrayofnode)-1)):
			print type(arrayofnode[i])
			print arrayofnode[i]
			if(arrayofnode[i+1]!=1.0):
				print i
				print filename
				print arrayofnode[i]
				print arrayofnode2[int(arrayofnode[i])]
				# x = input()
				all_nodes.append((arrayofnode2[int(arrayofnode[i])], arrayofnode2[int(arrayofnode[i+1])]))
				# all_lat.append(arrayoflatitudes[1:])
				# all_long.append(arrayoflongitudes[1:])

				avgspeed = (arrayspeed[i+1] + arrayspeed[i])/float(2)
				all_speed.append(avgspeed)
				all_time.append(arraytime[i+1])


		# all_nodes.append([(0,0), (0,0)])
			
	
	df = pd.DataFrame({'Edges': all_nodes,'Speed': all_speed, 'Time': all_time})
	writer = pd.ExcelWriter('list_all_values_425.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()



def get_nodes():

	filename1 = 'list_all_values_425.xlsx'
	workbook2 = xlrd.open_workbook(filename1, on_demand=True)
	sheet2 = workbook2.sheet_by_index(0)
	ref = sheet2.col_values(1)
	speed_array = sheet2.col_values(2)
	time_array = sheet2.col_values(3)



	filename = 'final_nodes_all2.xlsx'
	workbook = xlrd.open_workbook(filename, on_demand=True)
	sheet = workbook.sheet_by_index(0)
	ref2 = sheet.col_values(1)
	index3 = sheet.col_values(2)
	final_ref = []
	index2 = []
	final_ref = np.append(final_ref, ref2[1:]).tolist()

	final_ref_index = []
	final_ref_ref = []
	index = len(index3)
	index2 = np.append(index2, index3[1:]).tolist()

	for i in range(1,len(ref)):
		key = 0	
		for j in range(0, len(final_ref)):

			if(ref[i]==final_ref[j]):
				key = 1
				final_ref_index.append(index2[j])
				final_ref_ref.append(final_ref[j])

		if(key==0):
			final_ref.append(ref[i])
			
			index2.append(index)
			final_ref_index.append(index)
			#final_node_ref.append(index)
			final_ref_ref.append(ref[i])
			index+=1

#		key =0


	df = pd.DataFrame({ 'Nodes': index2, 'Lat_long': final_ref})
	writer = pd.ExcelWriter('final_nodes_all_inc_425_2.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()

	#x = input()

	flag = 0
	final_final = []
	final_final2 = []
	final_speed = []
	final_time = []
	for i in range(1, len(ref)):
		if(ref[i]!= '[(0,0), (0,0)]' and ref[i]!= '[(0, 0), (0, 0)]'):
			final_final.append(final_ref_index[flag])
			final_final2.append(final_ref_ref[flag])
			final_speed.append(speed_array[i])
			final_time.append(time_array[i])

			flag+=1



	# print final_nodes
	# print final_lat
	# print final_long

	df = pd.DataFrame({'Edge_Data': final_final2,'Edge_no': final_final, 'Speed': final_speed, 'Time': final_time})
	writer = pd.ExcelWriter('list_all_values_425_edges.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
	writer.save()
	#total_nodes = index
	# x = input()


#get_all_data()


# get_nodes()

# print 'heyyy'

# x = input()


def getindex(hour,mn):
	#hour-=4
	return int(hour*6 + (mn/10))


hour,minute=0,0
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


workbook2 = xlrd.open_workbook('list_all_values_425_edges.xlsx', on_demand=True)
sheet2 = workbook2.sheet_by_index(0)
node2 = sheet2.col_values(2)
arrayspeed2 = sheet2.col_values(3)
arrayoflatlong2 = sheet2.col_values(1)
# arrayoflongitudes = sheet.col_values(2)
time2 = sheet2.col_values(4)





workbook = xlrd.open_workbook('list_all_values3.xlsx', on_demand=True)
sheet = workbook.sheet_by_index(0)
node = sheet.col_values(2)
arrayspeed = sheet.col_values(3)
arrayoflatlong = sheet.col_values(1)
# arrayoflongitudes = sheet.col_values(2)
time1 = sheet.col_values(4)


node = np.append(node, node2[1:])
arrayspeed = np.append(arrayspeed, arrayspeed2[1:])
arrayoflatlong = np.append(arrayoflatlong, arrayoflatlong2[1:])
time1 = np.append(time1, time2[1:])


df = pd.DataFrame({'Edge_Data': arrayoflatlong[1:],'Edge_no': node[1:], 'Speed': arrayspeed[1:], 'Time': time1[1:]})
writer = pd.ExcelWriter('list_all_values_all_425_trackntell.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df.to_excel(writer, sheet_name='Sheet 1')
writer.save()

# x = input()


total_nodes = 765


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
	print node[i]
	print type(int(float(node[i].item())))
	temp[index, int(float(node[i].item()))] = temp[index, int(float(node[i].item()))] + 1
	
	matrix[int(index), int(float(node[i].item()))] = float(arrayspeed[i])*(1/temp[int(index), int(float(node[i].item()))]) + (float(matrix[int(index), int(float(node[i].item()))])*(temp[index, int(float(node[i].item()))] -1)/(temp[int(index), int(float(node[i].item()))]))
	
	print type(temp[index, int(float(node[i].item()))])
	
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


writer = pd.ExcelWriter('matrix_425_trackntell.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df.to_excel(writer, sheet_name='Sheet 1')

writer = pd.ExcelWriter('Freq_matrix_425_trackntell.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
df1.to_excel(writer, sheet_name='Sheet 1')

