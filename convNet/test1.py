import sys
import numpy as np

# the input volume(width=7, height=7, depth=3)
X = np.array([[	[0, 0, 0, 0, 0, 0, 0], 
				[0, 1, 0, 0, 0, 0, 0], 
				[0, 1, 0, 1, 2, 2, 0], 
				[0, 0, 0, 2, 1, 2, 0], 
				[0, 2, 2, 0, 2, 1, 0], 
				[0, 0, 2, 1, 1, 1, 0], 
				[0, 0, 0, 0, 0, 0, 0]],

			  [	[0, 0, 0, 0, 0, 0, 0], 
			  	[0, 2, 0, 2, 1, 1, 0], 
			  	[0, 1, 2, 2, 0, 0, 0], 
			  	[0, 1, 0, 2, 2, 0, 0], 
			  	[0, 0, 0, 1, 2, 0, 0], 
			  	[0, 0, 1, 2, 1, 1, 0], 
			  	[0, 0, 0, 0, 0, 0, 0]],

			  [	[0, 0, 0, 0, 0, 0, 0], 
			  	[0, 0, 0, 2, 2, 2, 0], 
			  	[0, 2, 1, 1, 1, 2, 0], 
			  	[0, 0, 1, 1, 0, 1, 0], 
			  	[0, 2, 1, 2, 0, 1, 0], 
			  	[0, 0, 2, 2, 2, 1, 0], 
			  	[0, 0, 0, 0, 0, 0, 0]]])

# the weight filter(receptive field=3*3)
# kernel=2
W = np.array([[[	[-1, 0, 1], 
					[1, 1, -1], 
					[-1, -1, 0]], 

			    [	[-1, -1, 0], 
			   		[-1, -1, -1], 
			   		[-1, -1, 0]], 

			    [	[1, -1, -1], 
			   		[-1, 0, 0], 
			   		[0, 0, 1]]], 



			   [[	[1, 0, 0], 
					[1, 0, 0], 
					[1, 1, 1]], 

			  	[	[0, 1, 1], 
			  		[-1, 0, 0], 
			  		[0, 0, 0]], 

			  	[	[-1, 0, -1], 
			  		[0, 1, 1], 
			  		[0, 1, -1]]]])

# output=3*3*2
V = np.zeros((2, 3, 3))

# bias=2*1
b = np.array([1, 0])

# slide=3
for dep in range(0, 2):
	for i in range(0, 3):
		res = 0
		for j in range(0, 3):
			res = 0
			for k in range(0, 3):
				#print "X: ", X[k, 2*i:2*i+3, 2*j:2*j+3]
				#print "W0", W[dep, k, :, :]
				res += np.sum(np.dot(X[k, 2*i:2*i+3, 2*j:2*j+3], W[dep, k, :, :]))
			res += b[dep]
			V[dep, j, i] = res

print V

