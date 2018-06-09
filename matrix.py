import xlrd
import geopy.distance
import pandas as pd

def stoi(i):
	if(i<10):
		return "0"+str(i)
	else:
		return str(i)

def getindex(hour,mn):
	hour-=4
	return int(hour*6 + (mn/10))

def column(matrix, i):
    return [row[i] for row in matrix]

def prog2():
	
	fil = []
	out = []
	out1= []
	n=1;
	bus="425"
	mon="Oct"
	yr="2017"
	readd=0
	row=[]
	hour,minute=4,0
	while(hour<23): #every 10 minutes
		if(minute<=40):
			row.append(str(hour)+':'+str(minute)+'-'+str(hour)+':'+str(minute+10))
			minute+=10
		else :
			row.append(str(hour)+':'+str(minute)+'-'+str(hour+1)+':'+str(0))
			minute=0
			hour+=1
	workbook1 = xlrd.open_workbook('Stoppage_'+bus+"CLUp"+".xlsx", on_demand=True)
	sheet1= workbook1.sheet_by_index(0)
	workbook2 = xlrd.open_workbook('Stoppage_'+bus+"CLDown"+".xlsx", on_demand=True)
	sheet2= workbook2.sheet_by_index(0)
	up_nodes=sheet1.col_values(5)
	down_nodes=sheet2.col_values(5)
	up_size=len(up_nodes)-1
	down_size=len(down_nodes)-1
	up_nodes.pop(0)
	down_nodes.pop(0)
	for i in range(0,len(up_nodes)):
		up_nodes[i]+=1
	for i in range(0,len(down_nodes)):
		down_nodes[i]+=1
	while (n<=31):
		fil.append("Final_"+bus+"_"+stoi(n)+mon+yr+".xlsx")
		out.append("matrix_up_"+bus+"_"+stoi(n)+mon+yr+".xlsx")
		out1.append("matrix_down_"+bus+"_"+stoi(n)+mon+yr+".xlsx")	
		
		freq_up = [[0 for j in range(114)] for i in range(up_size)] # 19*6
		freq_down = [[0 for j in range(114)] for i in range(down_size)]
		workbook = xlrd.open_workbook(fil[readd], on_demand=True)
		sheet = workbook.sheet_by_index(0)
		time_start = sheet.col_values(6)
		time_end = sheet.col_values(2)
		route = sheet.col_values(5)
		node= sheet.col_values(3)
		i=1
		while(i<len(route)): #write to the matrix 
			h1=int(time_start[i][11])*10+int(time_start[i][12])
			m1=int(time_start[i][14])*10+int(time_start[i][15])
			m1=int(m1/10)*10 #nearest 10

			h2=int(time_end[i][11])*10+int(time_end[i][12])
			m2=int(time_end[i][14])*10+int(time_end[i][15])
			m2=int(m2/10)*10

			l=getindex(h1,m1)
			r=getindex(h2,m2)
			# print(i)
			if(route[i]=="up"):
				while(l<=r):
					freq_up[int(node[i]-1)][l]+=1
					l+=1
			elif(route[i]=="down"):
				while(l<=r):
					freq_down[int(node[i]-1)][l]+=1
					l+=1
			i+=1

		# print(freq_up)
		df = pd.DataFrame({'Nodes': up_nodes})
		df1 = pd.DataFrame({'Nodes': down_nodes})
		for i in range(0,114):
			df[row[i]]=column(freq_up,i)
			df1[row[i]]=column(freq_down,i)
		

		writer = pd.ExcelWriter(out[readd], engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
		df.to_excel(writer, sheet_name='Sheet 1')
		
		writer = pd.ExcelWriter(out1[readd], engine='xlsxwriter')	# Convert the dataframe to an XlsxWriter Excel object.	
		df1.to_excel(writer, sheet_name='Sheet 1')	
		# Close the Pandas Excel writer and output the Excel file.
		writer.save()
		n+=1
		readd+=1
		
prog2()