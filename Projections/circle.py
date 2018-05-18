#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:50:37 2018

@author: eloisechakour
"""
import initializeSquare as isquare
import numpy as np
import matplotlib.pyplot as plt


def circle(radius, xSquare, ySquare):
    sideLength =30*radius
    
    shape = isquare.makeSquare(sideLength)
    
    for i in range(sideLength):
        for j in range(sideLength):
            
            x = xSquare[i, j]
            y = ySquare[i, j]
            
            if x**2+y**2 >= radius**2: 
                print ("Outside Circle")
                shape[i, j] = 0
    
    return shape





theta = np.pi /6.0

xSquare, ySquare = isquare.indexMap(30)


#square = makeSquare(1)
circle = circle(1, xSquare, ySquare)
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