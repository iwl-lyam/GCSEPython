'''
neural.py
A "quick" rewrite of an old project
'''
import math
import numpy
import random

def s(x):
    return 1 / (1 + math.exp(-x))

class NeuralNetwork:
    def __init__(self, inputs, outputs, target):
        # self.inputs = inputs
        self.inputs = []
        self.outputs = []
        self.weights = []
        # self.outputs = outputs
        for _ in inputs:
            self.inputs.append(random.uniform(-1, 1))
        for i,_ in enumerate(outputs):
            self.outputs.append(random.uniform(-1, 1))
            for j,_ in enumerate(inputs):
                self.weights.append({"input": j, "output": i, "value": random.uniform(-10, 10)})
        self.target = target

    
    
    def _cost(self, actual_out, inputs):
        #(s(INPUT1 * vx + INPUT2 * vz) - OUTPUT1) ** 2 + (s(INPUT1 * vy + INPUT2 * va) - OUTPUT2) ** 2
        cost = 0
        for i,output in enumerate(actual_out):
            cost += (output - self.target[i]) ** 2

    def _f_propagate(self, inp):
        pass
        
