#decentrelized db like lib that alows you to use simple python syntax like there is a local db althou it is all stored in the #blockchain



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
#class ipfshandler:
