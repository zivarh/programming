import random
import math
import matplotlib.pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)
n_agents = 10
n_iterations = 100
# Initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

# Move agents

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99
# Apply movement constraints.

for i in range(n_agents):
    if agents[i][0] < x_min:
        agents[i][0] = x_min
    if agents[i][1] < y_min:
        agents[i][1] = y_min
    if agents[i][0] > x_max:
        agents[i][0] = x_max
    if agents[i][1] > y_max:
        agents[i][1] = y_max
print(agents)



# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Return the Sum the squared differences square rooted.
    euc = math.sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
    return euc

x0 = 0
y0 = 0
x1 = 3
y1 = 4

print(get_distance(x0,y0,x1,y1))

# Plot
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()



#max distance calculation


def get_distances(agents):
    max_distance = 0
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            max_distance = max(max_distance, distance)
            min_distance = min(min_distance, distance)
    return (min_distance, max_distance)

min_distance, max_distance = get_distances(agents)
print("Maximum distance between any two agents:", max_distance)
print("Minimum distance between any two agents:", min_distance)
