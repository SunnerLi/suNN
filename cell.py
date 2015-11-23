import sys, random

"""
				Cell class
			_________________
	W1	==>	|				|
			|	Theta  		|
			|	W=[W1, W2]	|	=>
	W2	==>	|				|
			-----------------
"""

class Cell:
	"""
		the class to define the Cell in perceptron
	"""
	theta = 1.2			# Theta value, the constant of the line which x+y is
	numberOfInput = 0	# The number of Input
	weight = []			# The list of weight.

	#def __init__(self):
		#constructor
	#	pass

	def constructCell():
		"""
			The constructor of the Cell object.
		"""
		pass

	def weightGenerate(self):
		"""
			Randomly determine the each input's weight.
			The weight's range is from 0.5 to -0.5(float type)
		"""
		for i in range(0, self.numberOfInput):
			self.weight.append(random.random()-0.5)

	def computing(self, inputList):
		"""
			Compute the output of the cell.
			According to the perceptron's principle, there're two function:
				1. Summation
				2. Threshold
			Input 	=> list of input value
			Output 	=> 1 or -1
		"""
		r = 0	# The sum variable

		# Summation and Threshold function(Activate function)
		for i in range(0, self.numberOfInput):
			r += (int)(inputList[i]) * self.weight[i]
			#print "r= ", r
		if r > self.theta:
			return 1.0
		else:
			return -1.0;

	def weightRevise(self, n, inputList, outputItem, exceptItem):
		"""
			revise the weight during learning.
			perceptron's learning rule: W(differ) = n(eta) * [ D(desire) - Y(actual) ] * A(input)
			Input 	=> eta value, list of input value, the actual output, the desire output
		"""
		for i in range(0, self.numberOfInput):
			#print "outputItem: ", outputItem, "exceptItem: ", exceptItem
			#print "weight before: ", self.weight[i]
			self.weight[i] += n*(exceptItem-outputItem )*inputList[i]
			#print "weight after: ", self.weight[i]


class Layer:
	"""
		the class to define the layer in perceptron
	"""
	numberOfCell = 0
	cellList = []

	def __init__(self):
		pass

	def constructLayer(self, _numberOfCell):
		self.numberOfCell = _numberOfCell
		for i in range(0, _numberOfCell):
			cell = Cell()
			self.cellList.append(cell)

	def weightGenerate(self):
		for i in range(0, self.numberOfCell):
			self.cellList[i].weightGenerate()

	def computing(self, inputList):
		outputList = []
		for i in range(0, self.numberOfCell):
			outputList.append(self.cellList[i].computing(inputList))
		return outputList

	def weightRevise(self, n, inputList, outputItem, exceptItem):
		for i in range(0, self.numberOfCell):
			self.cellList[i].weightRevise(n, inputList, outputItem, exceptItem)


class Net:
	"""
		the class to define the net in perceptron
	"""
	numberOfLayer = 0
	layerList = []
	List_inputPattern = []
	List_outputPattern = []
	numberOftesttingCase = 0
	eta = 0.15

	#def __init__(self):
	#	pass

	def constructNet(self, _numberOfLayer):
		self.numberOfLayer = _numberOfLayer
		for i in range(0, _numberOfLayer):
			layer = Layer();
			self.layerList.append(layer)

	def constructLayer(self, index, _numberOfCell):
		self.layerList.constructLayer(_numberOfCell)

	def constructLayer(self, indexList):
		if len(indexList) == self.numberOfLayer:
			for i in range(0, self.numberOfLayer):
				self.layerList[i].constructLayer(indexList[i])
			self.firstLayerInputRevise();
			self.elseLayerInputRevise();

	def firstLayerInputRevise(self):
		for i in range(0, self.layerList[0].numberOfCell):
			self.layerList[0].cellList[i].numberOfInput = 1

	def elseLayerInputRevise(self):
		for i in range(1, self.numberOfLayer):
			for j in range(0, self.layerList[i].numberOfCell):
				self.layerList[i].cellList[j].numberOfInput = self.layerList[i-1].numberOfCell

	def weightGenerate(self):
		for i in range(0, self.numberOfLayer-1):
			self.layerList[i].weightGenerate()

	def tellPattern(self, List_inputPat, List_outputPat):
		self.List_inputPattern.append(List_inputPat)
		self.List_outputPattern.append(List_outputPat)
		self.numberOftesttingCase += 1

	def computing(self, inputList):
		outputList = inputList
		for i in range(1, self.numberOfLayer):
			#print "compute layer ", i
			#print "outlist size: ", len(outputList)
			outputList = self.layerList[i].computing(outputList)
		return outputList

	def learnning(self):
		learnningTimes = 0

		templearnningTimes = 1000
		while templearnningTimes>0:
			isJudgeTrue = True
			for i in range(0, self.numberOftesttingCase):
				outputList = self.computing(self.List_inputPattern[i])
				if outputList != self.List_outputPattern[i]:
					print outputList
					print self.List_outputPattern[i]
					isJudgeTrue = False

					_ = self.List_outputPattern[i]
					self.weightRevise(self.List_inputPattern[i], outputList[0], _[0])


			print "learning for ", learnningTimes, " times."
			learnningTimes += 1
			if isJudgeTrue == False and templearnningTimes>0:
				print "got wrong answer, learn again"
				templearnningTimes -= 1
			else:
				break
		print "learning complete!"

	def weightRevise(self, inputList, outputItem, exceptItem):
		for i in range(1, self.numberOfLayer):
			self.layerList[i].weightRevise(self.eta, inputList, outputItem, exceptItem)



