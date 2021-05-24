import random
from NeuralNet import buildNeuralNet

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