#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:57:31 2018

@author: eloisechakour
"""

#import numpy as np
#import matplotlib.pyplot as plt
import tesseract as tess



def fourBall(radius):
    sideLen = 3*radius
    shape = tess.tesseract(sideLen)
    
    for x in range(sideLen):
        for y in range(sideLen):
            for z in range(sideLen):
                for t in range(sideLen):
                    i = x - sideLen/2
                    j = y - sideLen/2
                    k = z - sideLen/2
                    m = t - sideLen/2
                    point = i**2 + j**2 + k**2 + m**2
                    
                    if point > radius**2:
                        shape[x, y, z, t] = 0
    
    
    return shape


ball = fourBall(20)
projection = tess.project4D(ball, 60)
""" Ok yay this works but I should know how to represent it and play with it! """









