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
trials = 10000
trial = 0
while trial < trials:
    trial = trial + 1
    # Flip three coins
    result = 'H' if random.randint(0,1) == 0 else 'T'
    results.append(result)
    # If it's three heads, add it to the count
    h3 = h3 + int(result == ['H','H','H'])
    
# What proportion of trials produced 3x heads
print ("%.2f%%" % ((h3/trials)*100))

print (results)