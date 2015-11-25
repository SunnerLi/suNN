<!---
layout: intro
title: SunNN
-->

# SunNN 

SunNN is a small project about neural network. This project only implement the perceptron now. It can implement the simple perceptron like AND or OR gate.

## Require
1. Python 2.7.6 (recomment!)

* Note: This program is implemented on Ubuntu14.04

## API Usage
1. Create the Net object first. Ex: ```net = Net()```

2. Assign the number of layer in the net. Ex: ```net.constructNet(2)``` refer to construct the 2-layers network.

3. Assign the number of cell in each layer. You can assign by a list or assign layer by layer.
Ex: ```net.constructLayer([2, 1])```

4. Tell the network the pattern you want to train. Mind it didn't have try except technique, so you should be careful the number of the input and output. use function ```net.tellPattern``` to store the pattern rule.

5. Use ```net.computing``` to computer the output that had been trained. Print the return list to check if meet your need.


## Limitation
   After construct the layer, the weight is generated randomly. You didn't need to generate the weight necessarily.
To generate the weight, use function ```net.weightGenerate```. The following code is wrong example:
```
	net.constructLayer([2, 1])
	net.tellPattern([0.0, 0.0, 1.0], [(float)(-1.0)])
```
   Cause perceptron is the neural netwotk that cannot solve the non-linear seperate problem, You would test some case that would tain 
fail if you give the such non-linear pattern. To develop the perceptron program, you should avoid this situation.
