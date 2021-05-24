from NeuralNet import NeuralNet, buildNeuralNet
import Testing
import sys

if __name__ == '__main__':
    accuraciesPen = []
    accuraciesCar = []

    for i in range(5):
        testPen = Testing.testPenData()
        accuraciesPen.append(testPen[1])

    for i in range(5):
        testCar = Testing.testCarData()
        accuraciesCar.append(testCar[1])

    print ('\n')
    print ('-----------STATS FOR PENS-----------')
    print ('max is: ', max(accuraciesPen))
    print ('avg is: ', Testing.average(accuraciesPen))
    print ('std is: ', Testing.stDeviation(accuraciesPen))


    print ('-----------STATS FOR CARS-----------')
    print ('max is: ', max(accuraciesCar))
    print ('avg is: ', Testing.average(accuraciesCar))
    print ('std is: ', Testing.stDeviation(accuraciesCar))

    with open('q5Result.txt', 'w') as f:
        f.write('------STATS FOR PENS------\n')
        f.write('max is: ' + str(max(accuraciesPen)) + '\n')
        f.write('avg is: ' + str(Testing.average(accuraciesPen)) + '\n')
        f.write('std is: ' + str(Testing.stDeviation(accuraciesPen)) + '\n')
        f.write('\n')

        f.write('------STATS FOR CARS------\n')
        f.write('max is: ' + str(max(accuraciesCar)) + '\n')
        f.write('avg is: ' + str(Testing.average(accuraciesCar)) + '\n')
        f.write('std is: ' + str(Testing.stDeviation(accuraciesCar)) + '\n')
        f.write('\n')