#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:34:21 2018

@author: eloisechakour
"""
import initializeSquare as isquare
import numpy as np
import matplotlib.pyplot as plt


def squareTriangle(sideLength): 
    shape = isquare.makeSquare(sideLength)
    
    #counter = 0
    for i in range(len(shape)):
        for j in range(len(shape)):
            if i < j:
                shape[i, j] = 0
                #print (counter)
        
    
    
    return shape#, fullShape



def equilateralTriangle(sideLength):

    numberCells = sideLength*10
    #cellSize = 1/(numberCells)
    shape = np.zeros((numberCells, numberCells))

    
    count = sideLength
    stepNb = 0
    
    for j in range(len(shape)):
        for i in range(len(shape)):
            if i >= stepNb: 
                if i <= count:
                    shape[i, j] = 1
        stepNb += 1
        count -= 1
    
    
    
    return shape











theta = np.pi /1.0


tri = squareTriangle(10)
"""Will need to fix the rotation function for triangles""" 
#rotated = isquare.rotateShape(tri, theta)
line, newLine = isquare.project(tri)

#tri = equilateralTriangle(100)
#line, newLine = isquare.project(tri)



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