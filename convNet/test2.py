import numpy as np

# the input volume(width=4, height=4, depth=2)
X = np.array([[	[0, 0, 0, 0], 
				[0, 1, 1, 0],
				[0, 1, 1, 0],
				[0, 0, 0, 0]],

			  [	[0, 0, 0, 1],
			  	[0, 2, 2, 0],
			  	[0, 2, 2, 0],
			  	[1, 0, 0, 0]]])

# the weight filter(receptive field=2*2)
# kernel=1
W = np.array([[	[1, 0],
				[0, 1],],

			  [	[2, 1],
			  	[1, 2]]])

# output=2*2*1
V = np.zeros([2, 2])

# bias=1
b = 1

# slide=2
for i in range(0, 2):
	res = 0
	for j in range(0, 2):
		res = 0
		for k in range(0, 2):
			res += np.sum(np.dot(X[k, 2*i:2*i+2, 2*j:2*j+2], W[k, :, :]))
		res += b
		V[i, j] = res

print V
