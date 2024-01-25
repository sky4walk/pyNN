from random import seed
from random import random
from random import gauss
import math
import myNum

# https://www.askpython.com/python/examples/backpropagation-in-python
# https://www.kaggle.com/code/soham1024/basic-neural-network-from-scratch-in-python


class Neuron:
    once = False
    number = 0
    def __init__(self,inputDim) :
        self.input = myNum.vector(inputDim)
        self.weight = myNum.vector(inputDim)
        self.output = 0.0
        self.goal = 0.0
        self.alpha = 0.1
        self.activationType = 0
        self.neuronNr = Neuron.number
        Neuron.number = Neuron.number + 1
    def getNeuronNr(self) :
        return Neuron.number
    def getInputSize(self) :
        return self.input.length()
    def setRandomWeights(self) :
        if ( False == self.once ) :
            seed(1)
            self.once = True
        for i in range(self.weight.length()) :
            self.weight.set(i,gauss(0,1))
    def setActivationType(self,nr) :
        self.activationType = nr
    def setWeights(self,weights) :
        self.weight.setVector(weights)
    def strWeights(self) :
        return self.weight.str()
    def setInput(self,vecInput) :
        self.input.setVector(vecInput) 
    def setGoal(self,goal) :
        self.goal = goal 
    def setAlpha(self,alpha) :
        self.alpha = alpha
    def activationFunc(self,inputVal) :
        val = inputVal
        if ( 1 == self.activationType) :
            val =  1 / (1 + math.exp(-inputVal))
        return val
    def forwardProp(self) :
        self.output = self.weight.dot(self.input)
        self.output = self.activationFunc(self.output,0)
        return self.output
    def strWeights(self) :
        return self.weight.str()
    def strInput(self) :
        return self.input.str()
    def backpropStep(self) :
        pred = self.forwardProp()
        delta = pred - self.goal
        error = delta ** 2
        derivate = self.input.mulScalar(delta)
        derivateAlpha = derivate.mulScalar(self.alpha)
        self.weight = self.weight.subVector(derivateAlpha)
        return [pred,delta,error]

class NeuralLayer :
    def __init__(self,cntNeurons,cntInputs) :
        self.neuronList = []
        self.inputSize = cntInputs
        for it in range(cntNeurons) :
            self.neuronList.append(Neuron(cntInputs))
    def getNeuron(self, nr) :
        assert ( nr < self.getLayerSize() )
        assert ( 0 <= nr  )
        return self.neuronList[nr]
    def getLayerSize(self) :
        return len(self.neuronList)
    def getInputSize(self) :
        return self.inputSize

def TestNeuron() :        
    n = Neuron(3)
    n.setRandomWeights()
    print(n.strWeights())
    iv = myNumTest.vector(3)
    iv.setArray([1,2,3])
    n.setInput(iv)
    print(n.strInput())
    print(n.forwardProp())

def TestBackProp1() :
    n = Neuron(1)
    
    weights = myNum.vector(1)
    weights.setArray([0.5])
    n.setWeights(weights)

    input = myNum.vector(1)
    input.setArray([2])
    n.setInput(input)

    n.setGoal(0.8)
    for iter in range(20) :
        print(n.backpropStep())

def TestBackProp2() :
    nl = NeuralLayer(1,1)

TestBackProp2()            