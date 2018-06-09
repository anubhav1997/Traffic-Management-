import xlrd
# import geopy.distance
import pandas as pd

def prog2():

	node = []
	avg_speed = []
	time1 = []
	time2 = []
	# threshold=0.1 #kms
	# workbook = xlrd.open_workbook('419.xlsx', on_demand=True)
	# workbook1 = xlrd.open_workbook('nodes.xlsx', on_demand=True)
	workbook2=xlrd.open_workbook('nodes_classify.xlsx',on_demand=True)
	sheet = workbook2.sheet_by_index(0)
	arraynode = sheet.col_values(3)
	arrayspeed = sheet.col_values(4)
	arraytime = sheet.col_values(5)
	i=1
	j=1
	while(i<len(arraynode)):
		count=0
		j=i+1
		time1.append(arraytime[i])
		node.append(arraynode[i])
		speedsum=float(arrayspeed[i])	
		while (j<len(arraynode) and arraynode[j]==arraynode[i]	):
			speedsum=speedsum+float(arrayspeed[j])
			count=count+1;
			j=j+1;
		time2.append(arraytime[j-1])
		if (count):
			speedsum=speedsum/count;
		avg_speed.append(speedsum);
		i=j
	df = pd.DataFrame({'Node': node, 'Speed': avg_speed, 'Start Time': time1, 'End Time': time2})
	writer = pd.ExcelWriter('finalplot.xlsx', engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
	df.to_excel(writer, sheet_name='Sheet 1')
		# workbook2.add_sheet('Sheet'+str(num+1))	
	# Close the Pandas Excel writer and output the Excel file.
	writer.save()

		
prog2()
