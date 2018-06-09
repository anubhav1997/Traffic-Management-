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
import numpy as np


def getindex(hour,mn):
	hour-=4
	return int(hour*6 + (mn/10))




def get_all_data():

	all_long = []
	all_lat = []
	all_nodes = []
	all_speed = []
	all_time = []

	filename1 = 'Stoppage_Ref_Nodes_425_up.xlsx'
	workbook2 = xlrd.open_workbook(filename1, on_demand=True)
	sheet2 = workbook2.sheet_by_index(0)
	arrayofnode2 = sheet2.col_values(1)

	filename4 = 'Stoppage_425CLUp.xlsx'
	workbook4 = xlrd.open_workbook(filename4, on_demand=True)
	sheet4 = workbook4.sheet_by_index(0)
	# arrayofnode4 = sheet4.col_values(5)
	arraylat4 = sheet4.col_values(3)
	arraylong4 = sheet4.col_values(4)
	
	filename3 = 'final_final_nodes_all_inc_buses.xlsx'
	workbook3 = xlrd.open_workbook(filename3, on_demand=True)
	sheet3 = workbook3.sheet_by_index(0)
	arrayofnode3 = sheet3.col_values(3)
	arraylat3 = sheet3.col_values(1)
	arraylong3 = sheet3.col_values(2)

	# arrayspeed3 = sheet3.col_values(1)
	# freq = np.zeros(len(array))


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

	matrix = [[[] for i in range(37+1)] for j in range(len(row))]


	for filename in glob.glob('/home/anubhav/Desktop/IP/Final/425_final/*'):
		workbook = xlrd.open_workbook(filename, on_demand=True)
		sheet = workbook.sheet_by_index(0)
		arrayofnode = sheet.col_values(3)
		arrayspeed = sheet.col_values(1)
		# arrayoflatitudes = sheet.col_values(1)
		# arrayoflongitudes = sheet.col_values(2)
		arraytimeStart = sheet.col_values(6)
		arraytimeEnd = sheet.col_values(2)
		arraydir = sheet.col_values(5)

		#all_nodes = np.append(all_nodes, node[1:])

		time_0 = 0


		for i in range(1,(len(arrayofnode)-1)):
			# print type(arrayofnode[i])
			# print arrayofnode[i]
			
			if(arrayofnode[i]==2.0 and arraydir[i]!='down'):
				
				m1 = int(arraytimeStart[i][-8]) +int(arraytimeStart[i][-9])*10
				h1 = int(arraytimeStart[i][-11]) + int(arraytimeStart[i][-12])*10
				s1 = int(arraytimeStart[i][-5]) +int(arraytimeStart[i][-6])*10

				time_0 = m1*60 + h1*3600 + s1
				print arraytimeStart[i],
				print time_0,
				print 'heyyy'

			elif(arrayofnode[i]!=1.0 and arrayofnode[i]!=2.0 and arraydir[i]!='down' ):
				# print i
				# print filename
				# print arrayofnode[i]
				# print arrayofnode2[int(arrayofnode[i])]
				# x = input()
				
				#all_nodes.append((arrayofnode2[int(arrayofnode[i])], arrayofnode2[int(arrayofnode[i+1])]))
				


				# all_lat.append(arrayoflatitudes[1:])
				# all_long.append(arrayoflongitudes[1:])

				#avgspeed = (arrayspeed[i+1] + arrayspeed[i])/float(2)
				
				# FMT = '%H:%M:%S'
				# # tdelta = datetime.strptime(time[i+1], FMT) - datetstr(ime.str)ptime(time[i], FMT)
				# # t = time[i] - time[i+1]
				# # print timeeee[i]
				# t1 = datetime.strptime(arraytimeStart[i].split('.')[0],'%H:%M:%S')
				# t2 = datetime.strptime(arraytimeEnd[i+1].split('.')[0],'%H:%M:%S')
				# t = t2-t1
				# t = time.strptime(str(t), '%H:%M:%S')
				# t = dt.timedelta(hours=t.tm_hour,minutes=t.tm_min,seconds=t.tm_sec).total_seconds()
				




				# m1 = int(arraytimeStart[i][-8]) +int(arraytimeStart[i][-9])*10
				# h1 = int(arraytimeStart[i][-11]) + int(arraytimeStart[i][-12])*10
				# s1 = int(arraytimeStart[i][-5]) +int(arraytimeStart[i][-6])*10

				# t1 = m1*60 + h1*3600 + s1

				if(time_0!=0):


					m2 = int(arraytimeEnd[i][-8])+int(arraytimeEnd[i][-9])*10 
					h2 = int(arraytimeEnd[i][-11])+ int(arraytimeEnd[i][-12])*10 
					s2 = int(arraytimeEnd[i][-5]) +int(arraytimeEnd[i][-6])*10

					t2 = m2*60 + h2*3600 + s2
					
					t = t2-time_0

					coords_1 = ((arraylat4[int(arrayofnode[i])], arraylong4[int(arrayofnode[i])]))
					#coords_2 = ((arraylat4[int(arrayofnode[i+1])], arraylong4[int(arrayofnode[i+1])]))
					coords_2 = ((arraylat4[2], arraylong4[2]))


					dis = geopy.distance.vincenty(coords_1, coords_2).km
					# print dis
					# print t

					sp = dis*3600/t

					print dis*3600/t, 'speed'


					if(sp>1):

						# print 'speed', dis*60/float(t)
						# speed.append()
						
						#freq[int(arrayofnode[i])]+=1
						matrix[int(getindex(h2,m2))][int(arrayofnode[i])].append(t)



						# if(t!=0):

						# 	# all_speed.append(dis*60/float(t))
						# 	all_speed.append((arrayspeed[i+1] + arrayspeed[i])/float(2))	
						
						# else:
						# 	all_speed.append((arrayspeed[i+1] + arrayspeed[i])/float(2))	
						# all_time.append(arraytimeEnd[i+1])


				if(arrayofnode[i]==37):
					time_0 = 0



		# all_nodes.append([(0,0), (0,0)])
			
	final = np.zeros((len(matrix), len(matrix[0])))
	final2 = np.zeros((len(matrix), len(matrix[0])))

	print matrix 
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			m = np.mean(matrix[i][j])
			v = np.var(matrix[i][j])
			print m, v
			final[i][j] = m
			final2[i][j] = v


	total_nodes = len(matrix[0])
	total_nodes = 38

	df1 = pd.DataFrame({'Nodes': [i for i in range(total_nodes+1)]})
	df = pd.DataFrame({'Nodes': [i for i in range(total_nodes+1)]})

	# final_matrix = []
	# final_ = []
	print len(row)
	print len(matrix)
	print len(matrix[0])
	x = input()

	for i in range(len(row)):
		print 'heyy'
		t2_temp = np.append(row[i], final[i])


		t_temp = np.append(row[i], final2[i])
		# print t_temp
		# print len([i for i in range(38)])
		# print len(t2_temp)
		print t_temp
		print len(t_temp)

		df[i]=t_temp
		df1[i]=t2_temp


	writer = pd.ExcelWriter('VARIANCE.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')

	writer = pd.ExcelWriter('MEAN.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df1.to_excel(writer, sheet_name='Sheet 1')





	# df = pd.DataFrame({'Edges': all_nodes,'Speed': all_speed, 'Time': all_time})
	# writer = pd.ExcelWriter('list_all_values_534_up.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	# df.to_excel(writer, sheet_name='Sheet 1')
	# writer.save()


get_all_data()







# def get_nodes():

# 	filename1 = 'list_all_values_534_up.xlsx'  ### chnage this to one as saved above 
# 	workbook2 = xlrd.open_workbook(filename1, on_demand=True)
# 	sheet2 = workbook2.sheet_by_index(0)
# 	ref = sheet2.col_values(1)
# 	speed_array = sheet2.col_values(2)
# 	time_array = sheet2.col_values(3)



# 	filename = 'final_nodes_all_inc_543_2_up.xlsx' # change this is previous saved list of all 
# 	workbook = xlrd.open_workbook(filename, on_demand=True)
# 	sheet = workbook.sheet_by_index(0)
# 	ref2 = sheet.col_values(1)
# 	index3 = sheet.col_values(2)
# 	final_ref = []
# 	index2 = []
# 	final_ref = np.append(final_ref, ref2[1:]).tolist()

# 	final_ref_index = []
# 	final_ref_ref = []
# 	index = len(index3)
# 	index2 = np.append(index2, index3[1:]).tolist()

# 	for i in range(1,len(ref)):
# 		key = 0	
# 		for j in range(0, len(final_ref)):

# 			if(ref[i]==final_ref[j]):
# 				key = 1
# 				final_ref_index.append(index2[j])
# 				final_ref_ref.append(final_ref[j])

# 		if(key==0):
# 			final_ref.append(ref[i])
			
# 			index2.append(index)
# 			final_ref_index.append(index)
# 			#final_node_ref.append(index)
# 			final_ref_ref.append(ref[i])
# 			index+=1

# #		key =0


# 	df = pd.DataFrame({ 'Nodes': index2, 'Lat_long': final_ref})
# 	writer = pd.ExcelWriter('final_final_nodes_all_inc.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
# 	df.to_excel(writer, sheet_name='Sheet 1')
# 	writer.save()

# 	#x = input()

# 	flag = 0
# 	final_final = []
# 	final_final2 = []
# 	final_speed = []
# 	final_time = []
# 	for i in range(1, len(ref)):
# 		if(ref[i]!= '[(0,0), (0,0)]' and ref[i]!= '[(0, 0), (0, 0)]'):
# 			final_final.append(final_ref_index[flag])
# 			final_final2.append(final_ref_ref[flag])
# 			final_speed.append(speed_array[i])
# 			final_time.append(time_array[i])

# 			flag+=1



# 	# print final_nodes
# 	# print final_lat
# 	# print final_long

# 	df = pd.DataFrame({'Edge_Data': final_final2,'Edge_no': final_final, 'Speed': final_speed, 'Time': final_time})
# 	writer = pd.ExcelWriter('list_all_values_534_edges_up.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
# 	df.to_excel(writer, sheet_name='Sheet 1')
# 	writer.save()
# 	#total_nodes = index
# 	# x = input()




# get_nodes()

# print 'heyyy'

# # x = input()


# def getindex(hour,mn):
# 	#hour-=4
# 	return int(hour*6 + (mn/10))


# hour,minute=0,0
# row = []


# while(hour<24): #every 10 minutes
# 	if(minute<=40):
# 		row.append(str(hour)+':'+str(minute)+'-'+str(hour)+':'+str(minute+10))
# 		minute+=10
# 	else :
# 		row.append(str(hour)+':'+str(minute)+'-'+str(hour+1)+':'+str(0))
# 		minute=0
# 		hour+=1

# matrix = []


# # for i in range(len(row)):
# # 	matrix.append([row[i]])

# final_nodes = []


# workbook2 = xlrd.open_workbook('list_all_values_534_edges_up.xlsx', on_demand=True)
# sheet2 = workbook2.sheet_by_index(0)
# node2 = sheet2.col_values(2)
# arrayspeed2 = sheet2.col_values(3)
# arrayoflatlong2 = sheet2.col_values(1)
# # arrayoflongitudes = sheet.col_values(2)
# time2 = sheet2.col_values(4)





# workbook = xlrd.open_workbook('list_all_values_all_543_up_trackntell.xlsx', on_demand=True) ### previous list all values 
# sheet = workbook.sheet_by_index(0)
# node = sheet.col_values(2)
# arrayspeed = sheet.col_values(3)
# arrayoflatlong = sheet.col_values(1)
# # arrayoflongitudes = sheet.col_values(2)
# time1 = sheet.col_values(4)


# node = np.append(node, node2[1:])
# arrayspeed = np.append(arrayspeed, arrayspeed2[1:])
# arrayoflatlong = np.append(arrayoflatlong, arrayoflatlong2[1:])
# time1 = np.append(time1, time2[1:])


# df = pd.DataFrame({'Edge_Data': arrayoflatlong[1:],'Edge_no': node[1:], 'Speed': arrayspeed[1:], 'Time': time1[1:]})
# writer = pd.ExcelWriter('list_all_values_all_534_up_trackntell.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
# df.to_excel(writer, sheet_name='Sheet 1')
# writer.save()

# # x = input()


# total_nodes = 1786


# # x = input()

# matrix = np.zeros((len(row), total_nodes))

# temp = np.zeros((len(row), total_nodes))

# print len(node)

# # x = input()


# for i in range(1, len(node)):

	
# 	print 'heyy', time1[i]
# 	time_start = time1[i]

# 	print 'len',len(time_start)

# 	if(len(time_start)!=23):
# 		print int(time_start[-11]),  int(time_start[-12])
# 		print int(time_start[-14]) 


# 		m1 = int(time_start[-11])+ int(time_start[-12])*10 
# 		h1 = int(time_start[-14]) + int(time_start[-15])*10
# 		m1=int(m1/10)*10 #nearest 10
# 		print h1, m1
# 		index = getindex(h1, m1)
# 	else: 
# 		m1 = int(time_start[-8]) +int(time_start[-9])*10
# 		h1 = int(time_start[-11]) + int(time_start[-12])*10
# 		m1=int(m1/10)*10 #nearest 10
# 		index = getindex(h1, m1)



# 	print index


# 	print len(row)

# 	print row[index]
# 	print arrayspeed[i]


# 	# print node[i]
# 	# print len(temp)
# 	# print len(node)
# 	print node[i]
# 	print type(int(float(node[i].item())))



# 	temp[index, int(float(node[i].item()))] = temp[index, int(float(node[i].item()))] + 1
	
# 	matrix[int(index), int(float(node[i].item()))] = float(arrayspeed[i])*(1/temp[int(index), int(float(node[i].item()))]) + (float(matrix[int(index), int(float(node[i].item()))])*(temp[index, int(float(node[i].item()))] -1)/(temp[int(index), int(float(node[i].item()))]))
# 	print float(arrayspeed[i])*(1/temp[int(index), int(float(node[i].item()))]) + (float(matrix[int(index), int(float(node[i].item()))])*(temp[index, int(float(node[i].item()))] -1)/(temp[int(index), int(float(node[i].item()))]))
	
# 	# x = input()



# 	print type(temp[index, int(float(node[i].item()))])
	
# 	# x = input()


# print matrix 

# print temp


# df1 = pd.DataFrame({'Nodes': [i for i in range(total_nodes+1)]})
# df = pd.DataFrame({'Nodes': [i for i in range(total_nodes+1)]})

# final_matrix = []
# final_freq = []

# for i in range(len(row)):
# 	print 'heyy'
# 	t2_temp = np.append(row[i], temp[i])


# 	t_temp = np.append(row[i], matrix[i])
# 	# print t_temp
# 	# print len([i for i in range(38)])
# 	# print len(t2_temp)
# 	df[i]=t_temp
# 	df1[i]=t2_temp


# writer = pd.ExcelWriter('matrix_final_final_all.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
# df.to_excel(writer, sheet_name='Sheet 1')

# writer = pd.ExcelWriter('Freq_matrix_final_final_all.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
# df1.to_excel(writer, sheet_name='Sheet 1')

