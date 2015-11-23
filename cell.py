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
			Generate the weight at initial.
		"""
		self.weightGenerate()

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
