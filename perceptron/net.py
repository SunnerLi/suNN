import sys, random
from layer import *

"""
			Net class
	-------------------------
	|						|
	|	layer 		layer 	|
		-----		-----	|
	|	|	|		|	|	|
	|	|	| ..... |	|	|
	|	|	|		|	|	|
	|	-----		-----	|
	|						|
	-------------------------
"""

class Net:
	"""
		the class to define the net in perceptron
	"""
	#define the debug mode
	global debugMode

	def __init__(self):
		"""
			The init function of the class
			Initial the whole specific variables.
		"""
		self.numberOfLayer = 0			# The number of layer
		self.layerList = []				# The list of the layer object
		self.List_inputPattern = []		# The list of the input pattern
		self.List_outputPattern = []		# The list of the output pattern
		self.numberOftesttingCase = 0	# The number of test case
		self.eta = 0.1					# Learning speed(eta value), 0.15 is best

	def constructNet(self, _numberOfLayer):
		"""
			The constructor of the net.
			Append the layer into the layer list.
			Input 	=> the number of layer in the list
		"""
		self.numberOfLayer = _numberOfLayer
		for i in range(0, _numberOfLayer):
			layer = Layer();
			self.layerList.append(layer)

	def constructLayer(self, index, _numberOfCell):
		"""
			Construct the specific layer
			Assign the number of cell toward the specific layer.
			Input 	=> the index of specific layer, the number of cell in the layer

		"""
		self.layerList[index].constructLayer(_numberOfCell)
		# revise the number of input.
		if index == 0:
			self.firstLayerInputRevise()
		else:
			elseLayerInputRevise(index)	

	def constructLayer(self, indexList):
		"""
			Construct the each layers.
			Assign the number of cell toward each layer.
			Revise the number of input for each layer.
			Input => the list that contain the number of cell in each layer
		"""
		if len(indexList) == self.numberOfLayer:
			for i in range(0, self.numberOfLayer):
				self.layerList[i].constructLayer(indexList[i])
			self.firstLayerInputRevise();
			self.elseLayersInputRevise();

	def firstLayerInputRevise(self):
		"""
			Revise the number of input about first layer's cell.
			The number of input about first layer is all 1.
		"""
		for i in range(0, self.layerList[0].numberOfCell):
			self.layerList[0].cellList[i].numberOfInput = 1

	def elseLayersInputRevise(self):
		"""
			Revise the number of input about others layer's cell.
			call elseLayerInputRevise function to revise each layer.
		"""
		for i in range(1, self.numberOfLayer):
			self.elseLayerInputRevise(i)

	def elseLayerInputRevise(self, index):
		"""
			Revise the number of input about others specific layer's cell.
			Input 	=> the index of the layer.
		"""
		for j in range(0, self.layerList[index].numberOfCell):
			self.layerList[index].cellList[j].numberOfInput = self.layerList[index-1].numberOfCell

	def weightGenerate(self):
		"""
			Generate the weight of the net.
			For each layer, call the weightGenerate function.
		"""
		for i in range(0, self.numberOfLayer):
			self.layerList[i].weightGenerate()

	def tellPattern(self, List_inputPat, List_outputPat):
		"""
			Record the pattern that the net need to learn.
			Input 	=> the list of the input pattern, the list of the output pattern.
		"""
		self.List_inputPattern.append(List_inputPat)
		self.List_outputPattern.append(List_outputPat)
		self.numberOftesttingCase += 1

	def computing(self, inputList):
		"""
			Compute the output of the whole net.
			Call the computing function toward each layer.
			Input 	=> the list that contain each input value
			Output 	=> the list that contain each output value
		"""
		outputList = inputList

		for i in range(1, self.numberOfLayer):
			#print "compute layer ", i
			#print "outlist size: ", len(outputList)
			outputList = self.layerList[i].computing(outputList)
		return outputList

	def learnning(self):
		"""
			Learning main function.
		"""
		learnningTimes = 0			# The counter to record how many time we had done
		templearnningTimes = 100	# The upper time we should compute

		while templearnningTimes>0:
			isJudgeTrue = True 		# Boolean represent if computing fail
			for i in range(0, self.numberOftesttingCase):
				outputList = self.computing(self.List_inputPattern[i])

				# If compute fail, remind and revise weight
				if outputList != self.List_outputPattern[i]:
					print "Except output: ", self.List_outputPattern[i]
					print "Actual output: ", outputList
					print "Compute fail..."
					isJudgeTrue = False

					# cause the List_outputPattern is the list of the list, double getting the item.
					#_ = self.List_outputPattern[i]
					self.weightRevise(self.List_inputPattern[i], outputList, self.List_outputPattern[i])


			print "learning for ", learnningTimes, " times."
			learnningTimes += 1
			if isJudgeTrue == False and templearnningTimes>0:
				print "got wrong answer, learn again"
				templearnningTimes -= 1
			else:
				break
		print "learning complete!"

	def weightRevise(self, inputList, outputList, exceptList):
		"""
			Revise the weight during the learning period.
			Call the weightRevise function toward each layer.
			
			Input 	=> 	list of input value, 
						list of actual output, 
						list of desire output
		"""

		for i in range(1, self.numberOfLayer):
			self.layerList[i].weightRevise(self.eta, inputList, outputList, exceptList)

	def assignWeightDirectly(self):
		self.layerList[1].cellList[0].weight[0] = 0.5
		self.layerList[1].cellList[0].weight[1] = 0.5
		self.layerList[1].cellList[1].weight[0] = 0.5
		self.layerList[1].cellList[1].weight[1] = 0.5