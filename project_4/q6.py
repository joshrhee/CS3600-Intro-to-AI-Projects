import NeuralNet
import Testing

file = open("q6Result.txt", "w")

accuracyPen = [[] for i in range(0, 41, 5)]
hiddenLayerPen = [[i] for i in range(0, 41, 5)]

file.write("          ----------Data for Pens----------\n")
for neuronCount in range(0, 45, 5):

    accuraciesPen = []
    
    for i in range(5):
        print ("Pen iteration: " + str(i + 1) + "neuronCount: " + str(neuronCount))
        accuraciesPen.append(Testing.testPenData()[1])

    print ("max: " + str(max(accuraciesPen)))
    print ("average: " + str(Testing.average(accuraciesPen)))
    print ("standard deviation: " + str(Testing.stDeviation(accuraciesPen)))

    if (neuronCount <= 9):
        line = "Neuron Count: " + str(neuronCount) + "           Average Accuracy: " + str(Testing.average(accuraciesPen))
    else:
        line = "Neuron Count: " + str(neuronCount) + "          Average Accuracy: " + str(Testing.average(accuraciesPen))
        
    file.write(line + "\n")

file.write("\n----------Data for Cars----------\n")
for neuronCount in range(0, 45, 5):
    
    accuraciesCar = []
    
    for i in range(5):
        print ("Car iteration: " + str(i + 1) + "neuronCount: " + str(neuronCount))
        accuraciesCar.append(Testing.testCarData()[1])

    print ("max: " + str(max(accuraciesCar)))
    print ("average: " + str(Testing.average(accuraciesCar)))
    print ("standard deviation: " + str(Testing.stDeviation(accuraciesCar)))
    
    if (neuronCount <= 9):
        line = "Neuron Count: " + str(neuronCount) + "           Average Accuracy: " + str(Testing.average(accuraciesCar))
    else:
        line = "Neuron Count: " + str(neuronCount) + "          Average Accuracy: " + str(Testing.average(accuraciesCar))
        
    file.write(line + "\n")

file.close()