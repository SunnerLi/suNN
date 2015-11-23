import sys
from net import *

net = Net()
net.constructNet(2)
net.constructLayer([2, 1])
print "Net has ", net.numberOfLayer, " layers"
print "the first layer has ", net.layerList[0].numberOfCell, " cell"
print "the first layer has ", net.layerList[1].numberOfCell, " cell"
net.weightGenerate();
net.tellPattern([0.0, 0.0], [(float)(-1.0)])
net.tellPattern([0.0, 1.0], [(float)(-1.0)])
net.tellPattern([1.0, 0.0], [(float)(-1.0)])
net.tellPattern([1.0, 1.0], [(float)(1.0)])
net.learnning()

print "testing: (0, 0)"
ll = net.computing([0, 0])
print ll
print "testing: (1, 0)"
ll = net.computing([1, 0])
print ll
print "testing: (0, 1)"
ll = net.computing([0, 1])
print ll
print "testing: (1, 1)"
ll = net.computing([1, 1])
print ll