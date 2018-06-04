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
    sideLength =3*radius
    
    shape = isquare.makeSquare(sideLength)
    #effectiveRadius = 10*radius
    
    for i in range(len(shape)):
        for j in range(len(shape)):
            x = i - sideLength/2
            y = j - sideLength/2
            
            #x = xSquare[i, j]
            #y = ySquare[i, j]
            
            if x**2+y**2 > radius**2: 
                #print ("Outside Circle")
                shape[i, j] = 0
    
    return shape



theta = np.pi /6.0

#xSquare, ySquare = isquare.indexMap(3)


#square = makeSquare(1)
circle = circle(30)
line, newLine = isquare.project(circle)




#for i in range(len(newLine)):
    #print (newLine[i])

#print ("Original")

#for i in range(len(line)):
    #print (line[i])

plt.plot(newLine, 'ro')
plt.show()

testLine = [newLine]
plt.imshow(testLine, interpolation='bicubic')
plt.show()