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
	numberOfCell = 0	# The number of Input
	cellList = []		# The list of the cell object

	#def __init__(self):
	#	pass

	def constructLayer(self, _numberOfCell):
		"""
			The constructor of the layer.
			Append the cell into the cell list.
			Input 	=> the number of cell in the list
		"""
		self.numberOfCell = _numberOfCell
		for i in range(0, _numberOfCell):
			cell = Cell()
			self.cellList.append(cell)

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
		return outputList

	def weightRevise(self, n, inputList, outputItem, exceptItem):
		"""
			Revise the weight during the learning period.
			Call the weightRevise function toward each cell.
			Input 	=> eta value, list of input value, the actual output, the desire output
		"""
		for i in range(0, self.numberOfCell):
			self.cellList[i].weightRevise(n, inputList, outputItem, exceptItem)
