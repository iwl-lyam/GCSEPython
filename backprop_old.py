# Backpropagation example ooooooo
import time
import numpy as np
import math
import matplotlib.pyplot as plt

print("BACKPROPAGATION CALCULATOR v1.0")
print("SETTING UP...")

def s(x):
    return 1 / (1 + math.exp(-x))


INPUT1 = 0.1
INPUT2 = 0.45679878675544
OUTPUT1 = 0.1
OUTPUT2 = 0.9645

TOP = 12
BOTTOM = -12
STEP = 0.5
RANGE = int((TOP + abs(BOTTOM)) / STEP)
IDIMENSIONS=4

x = np.arange(BOTTOM, TOP, STEP)
y = np.arange(BOTTOM, TOP, STEP)
z = np.arange(BOTTOM, TOP, STEP)
a = np.arange(BOTTOM, TOP, STEP)

data = []

'''
4 NEUTRONS - 2I 2O
4 WEIGHTS - 5 DIMENSIONS

x: N1-N3
y: N1-N4
z: N2-N3
a: N2-N4
'''

print("CALCULATING DATA POINTS -", RANGE, "PER INPUT DIMENSION -", RANGE*IDIMENSIONS, "IN TOTAL...")

START = time.perf_counter()

count = 0
for vx in x:
    print(".", end="")
    for vy in y:
        for vz in z:
            for va in a:
                res = (s(INPUT1 * vx + INPUT2 * vz) - OUTPUT1) ** 2 + (s(INPUT1 * vy + INPUT2 * va) - OUTPUT2) ** 2
                data.append({"w1": vx, "w2": vy, "w3": vz, "w4": va, "cost": res})
                count += 1
                # print({"w1": vx, "w2": vy, "w3": vz, "w4": va, "cost": res})

DEND = time.perf_counter()

print("\nDATA POINTS CALCULATED, ORGANISING...")

lowest = {'cost': 999999999999999}
for d in data:
    if d['cost'] < lowest['cost']:
        lowest = d
        # print(".", end="")

BEND = time.perf_counter()

print("\n\nNEW NETWORK CONFIGURATION AFTER BACKPROPAGATION:")
print("COST:", lowest['cost'])

print("\nWEIGHTS:")
print("N1-N3:", lowest['w1'])
print("N1-N4:", lowest['w2'])
print("N2-N3:", lowest['w3'])
print("N2-N4:", lowest['w4'])

print("\nINPUT ACTIVATIONS:")
print("INPUT1:", INPUT1)
print("INPUT2:", INPUT2, "\n")

print("EXPECTED OUTPUT1:", OUTPUT1)
print("CALCULATED OUTPUT1:", s(lowest['w1'] * INPUT1 + lowest['w3'] * INPUT2))
print("DIFFERENCE FOR OUTPUT1:", abs(OUTPUT1 - s(lowest['w1'] * INPUT1 + lowest['w3'] * INPUT2)))

print("\nEXPECTED OUTPUT2:", OUTPUT2)
print("CALCULATED OUTPUT2:", s(lowest['w2'] * INPUT1 + lowest['w4'] * INPUT2))
print("DIFFERENCE FOR OUTPUT2:", abs(OUTPUT2 - s(lowest['w2'] * INPUT1 + lowest['w4'] * INPUT2)))

print("\nTIME TO GENERATE DATA:", DEND-START,"s")
print("TIME TO ORGANISE DATA:", BEND-DEND,"s")
print("TOTAL BACKPROPAGATION TIME:", BEND-START,"s")