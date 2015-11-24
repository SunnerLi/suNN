import sys, random
from cell import *

"""
	 Layer class
	-------------
	|	cell1	|
	|	-----	|
	|	|	|	|
	|	-----	|
	|	  . 	|
	|	  . 	|
	|	  . 	|
	|	cell2	|
	|	-----	|
	|	|	|	|
	|	-----	|
	-------------
"""

class Layer:
	"""
		the class to define the layer in perceptron
	"""
	#define the debug mode
	global debugMode

	def __init__(self):
		"""
			The init function of the class
			Initial the number of cell and cell list.
		"""
		self.numberOfCell = 0	# The number of Input
		self.cellList = []		# The list of the cell object

	def constructLayer(self, _numberOfCell):
		"""
			The constructor of the layer.
			Append the cell into the cell list.
			Input 	=> the number of cell in the list
		"""
		self.numberOfCell = _numberOfCell
		for i in range(0, _numberOfCell):
			cell = Cell()
			_l = []
			_l.append(cell)
			#self.cellList.append(cell)
			self.cellList += _l

	def weightGenerate(self):
		"""
			Generate the weight of the layer.
			For each cell, call the weightGenerate function.
		"""
		for i in range(0, self.numberOfCell):
			self.cellList[i].weightGenerate()

	def computing(self, inputList):
		"""
			Compute the output of the whole layer.
			Call the computing function toward each cell.
			Input 	=> the list that contain each input value
			Output 	=> the list that contain each output value
		"""
		outputList = []
		for i in range(0, self.numberOfCell):
			outputList.append(self.cellList[i].computing(inputList))
			#print "Net computing: ", outputList, "number of cell: ", self.numberOfCell
		return outputList

	def weightRevise(self, n, inputList, outputList, exceptList):
		"""
			Revise the weight during the learning period.
			Call the weightRevise function toward each cell.

			Input 	=> 	eta value, 
						list of input value, 
						the actual output, 
						the desire output
		"""
		for i in range(0, self.numberOfCell):
			#print "weight list0: ", self.cellList[0].weight[0], " ", self.cellList[0].weight[1]
			#print "weight list1: ", self.cellList[1].weight[0], " ", self.cellList[1].weight[1]

			self.cellList[i].weightRevise(n, inputList, outputList[i], exceptList[i])

