#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:42:15 2018

@author: eloisechakour
"""

#import initializeSquare as isquare
import numpy as np
#import matplotlib.pyplot as plt





def tesseract(sideLen):
    
    tesseract = np.zeros((sideLen, sideLen, sideLen, sideLen))

    
    for x in range(sideLen):
        for y in range(sideLen):
            for z in range(sideLen):
                for t in range(sideLen):
                    tesseract[x, y, z, t] = 1
    
    
    
    return tesseract

def project4D(someShape, sideLen):
    
    cube = np.zeros((sideLen, sideLen, sideLen))
    
    for x in range(sideLen):
        for y in range(sideLen):
            for z in range(sideLen):
                count = 0
                for t in range(sideLen):
                    count += someShape[x, y, z, t]
                cube[x, y, z] = count
    
    return cube


Tesseract = tesseract(10)
Cube = project4D(Tesseract, 10)









