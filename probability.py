import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
from sympy.tensor.array import derive_by_array
import random

# # Count the number of 3xHeads results
# h3 = 0


# Create a list of all results
results = []

# loop through 10000 trials
trials = 50000
trial = 0
heads = 0
tails = 0

while trial < trials:
    trial = trial + 1
    result = random.randint(0,1)
    if result == 1: 
        heads += 1
    else:
        tails += 1
    results.append(result)
    

# print (results)
print('TRIAL = ', trial)
print('HEADS = ', heads)
print('TAILS = ', tails)
print("%.2f%%" % ((heads/trial)*100))