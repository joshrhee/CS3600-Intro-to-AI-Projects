from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
from math import pow, sqrt

import random


def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData, maxItr = 200, hiddenLayerList = hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200,hiddenLayerList = hiddenLayers)

testCarData()



# Q7(xorData) code
def testXOR():
    xorData = [[[0, 0], [1, 0]], [[0, 1], [0, 1]], [[1, 0], [0, 1]], [[1, 1], [1, 0]]]

    xorData = xorData * 125

    # shuffle the data
    random.shuffle(xorData)

    # 70:30 train:test
    trainNumber = 0.7 * len(xorData)

    xorTrain = xorData[:int(trainNumber)]
    xorTest = xorData[int(trainNumber):]
    xorData = [xorTrain, xorTest]

    perceptronCount = 0
    hiddenLayers = [perceptronCount]
    result = buildNeuralNet(xorData, maxItr = 500, hiddenLayerList = hiddenLayers)

    perceptronCount = 1
    hiddenLayers = [perceptronCount]
    result = buildNeuralNet(xorData, maxItr = 500, hiddenLayerList = hiddenLayers)

    perceptronCount = 2
    hiddenLayers = [perceptronCount]
    result = buildNeuralNet(xorData, maxItr = 500, hiddenLayerList = hiddenLayers)

    perceptronCount = 3
    hiddenLayers = [perceptronCount]
    result = buildNeuralNet(xorData, maxItr = 500, hiddenLayerList = hiddenLayers)
    return result
