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
	numberOfLayer = 0			# The number of layer
	layerList = []				# The list of the layer object
	List_inputPattern = []		# The list of the input pattern
	List_outputPattern = []		# The list of the output pattern
	numberOftesttingCase = 0	# The number of test case
	eta = 0.15					# Learning speed(eta value)

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