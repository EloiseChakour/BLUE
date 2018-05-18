#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:50:37 2018

@author: eloisechakour
"""
import initializeSquare as isquare
import numpy as np
import matplotlib.pyplot as plt


def circle(radius):
    shape = isquare.makeSquare(3*radius)
    
    for i in range(3*radius):
        for j in range(3*radius):
            if i^2+j^2 >= radius^2: 
                shape[i, j] = 0
    
    return shape





theta = np.pi /6.0

#square = makeSquare(1)
circle = circle(1)
rotated = isquare.rotateShape(circle, 0)
line, newLine = isquare.project(rotated)

for i in range(len(newLine)):
    print (newLine[i])

print ("Original")

for i in range(len(line)):
    print (line[i])

plt.plot(newLine, 'ro')
plt.show()

testLine = [newLine]
plt.imshow(testLine, interpolation='bicubic')
plt.show()