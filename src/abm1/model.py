import random
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Initialise variable x1
x1 = random.randint(0, 99)
print("x1", x1)
# Initialise variable y1
y1 = random.randint(0, 99)
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4

euc= math.sqrt(pow(x1-x0, 2) + pow(y1-y0, 2)) #eucliar number calculation
print(euc)