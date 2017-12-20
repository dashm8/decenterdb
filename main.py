import ipfsapi


class Table:

	#col is a list of colum names
	#data is a list of lists of data
	def __init__(self,col,tname):
		self.col = col 
		self.tname = tname
		self.data = []

	def AddEntry(self,values):
		if len(values) != len(self.col):
			return 1
		self.data.append(values)

	def AddListEntry(self,valueList):
		for values in valueList:
			if len(values) == len(self.col):
				self.data.append(values)

	#if colnum is -1 it returns all colums
	def Select(self,colnum=-1):
		if colnum == -1:
			return self.data
		ret = []
		for entry in self.data:
			ret.append(entry[colnum])
		return ret

	def SelectWh(self,value,colwh):
		ret = []
		for entry in self.data:
			if value==entry[colwh]:			
				ret.append(entry)
				
	def SelectLi(self,value,colwh):
		ret = []
		for entry in self.data:
			if value in entry[colwh]:			
				ret.append(entry)		
				
	def Delete(self,value,colwh):
		for entry in self.data:
			if value==entry[colwh]:			
				ret.append(entry)
		
	


#TODO:
class ipfshandler:
	def __init__(self,port):
		self.port = port
		self.api = ipfsapi.connect("127.0.0.1",port)

	def UpdateDb(self,table):
		Formatter.FormatToFile(table)
		api.add(table.name)

	def GetDbEntry

class Formatter:

	def FormatToFile(table):
		f = open(table.name,'w')
		colum = ""
		for cols in table.col:
			colum += cols + ','
		f.write(colum)
		for data in table.data:
			line = ""
			for col in data:
				line+=col + ','
			f.write(line)
		f.close()

	def FormatFromFile(self,fname):
		f = open(fname,'r')
		col = []
		data = []
		count = 1
		for line in f:
			if count == 1:
				col = line.split(',')[-1]
				count+=1
			else:
				data.append(line.split(',')[-1])
		tbl = Table(col,fname)
		tbl.data = data
		return tbl
