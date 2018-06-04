import numpy as np
#import matplotlib.pyplot as plt



def makeSquare(sideLength):
    numberCells = sideLength*10
    #cellSize = 1/(numberCells)
    square = np.zeros((numberCells, numberCells))
    
    for i in range(numberCells):
        for j in range(numberCells):
            square[i, j] = 1
    
    return square


def rotateShape(shape, theta):
    numberCells = len(shape)
    
    cos = np.cos(theta)
    sin = np.sin(theta)
    nsin = (-1)*np.sin(theta)
    
    rotMatrix = np.zeros((2, 2))
    rotMatrix[0, 0] = cos
    rotMatrix[0, 1] = nsin
    rotMatrix[1, 0] = sin
    rotMatrix[1, 1] = cos
    
    newLen = int(np.ceil(np.sqrt(2)*numberCells))
    newShape = np.zeros((newLen, newLen))
    
    for i in range(numberCells):
      for j in range(numberCells):
          value = shape[i,j]
          
          position = np.zeros(2)
          position[0] = i
          position[1] = j
          
          newPos = np.dot(position, rotMatrix)
          x = int(np.floor(newPos[0]))
          y = int(np.floor(newPos[1]))
          newShape[x, y] = value
          
    return newShape

def project(shape):
    
    newNumberCells = len(shape)
    
    line = np.zeros(newNumberCells)

    for i in range(newNumberCells):
        count = 0
        for j in range(newNumberCells):
            count += shape[i, j]
        line[i] = count
    
    line = list(line)
    while min(line) == 0:
        line.remove(0)
    
    line = np.asarray(line)
    
    total = 0
    newLine = []
    
    binSize = 6.0
    
    for i in range(len(line)):
        if i%binSize != 0: 
            total += line[i]
        else: 
            value = total/binSize
            newLine.append(value)
            value = 0
            total = 0
    
    
    while min(newLine) == 0:
        newLine.remove(0)
    
            
    
    newLine = np.asarray(newLine)

    return line, newLine
    

def indexMap(sideLength):
    
    xSquare = np.zeros((sideLength, sideLength))
    ySquare = np.zeros((sideLength, sideLength))
    
    for i in range(sideLength):
        for j in range(sideLength):
            xSquare[i, j] = i
            ySquare[i, j] = j
    
    
    half = sideLength/2

    for i in range(sideLength):
        for j in range(sideLength):
            xSquare[i, j] = i-half
            ySquare[i, j] = j-half
    
    return xSquare, ySquare


    
    
        
    
    
"""
theta = np.pi /4.0

square = makeSquare(1)
rotated = rotateShape(square, theta)
line, newLine = project(rotated)

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
"""








