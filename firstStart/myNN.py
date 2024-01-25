from random import seed
from random import random
from random import gauss
import math
import myNum

# https://www.askpython.com/python/examples/backpropagation-in-python
# https://www.kaggle.com/code/soham1024/basic-neural-network-from-scratch-in-python


class Neuron:
    once = False
    def __init__(self,inputDim) :
        self.input = myNum.vector(inputDim)
        self.weight = myNum.vector(inputDim)
        self.output = 0.0
        self.goal = 0.0
        self.alpha = 0.1
    def getInputSize(self) :
        return self.input.length()
    def setRandomWeights(self) :
        if ( False == self.once ) :
            seed(1)
            self.once = True
        for i in range(self.weight.length()) :
            self.weight.set(i,gauss(0,1))
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
    def activationFunc(self,inputVal,type) :
        val = inputVal
        if ( 1 == type) :
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

class NeuralNet :
    def __init__(self,inputDim) :
        self.a = 0

def TestNeuron() :        
    n = Neuron(3)
    n.setRandomWeights()
    print(n.strWeights())
    iv = myNumTest.vector(3)
    iv.setArray([1,2,3])
    n.setInput(iv)
    print(n.strInput())
    print(n.forwardProp())

def TestBackProp() :
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

TestBackProp()            