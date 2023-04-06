import random
import math
import matplotlib.pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io

#read data
environment, n_rows, n_cols = io.read_data()

# Set the pseudo-random seed for reproducibility
random.seed(0)

n_agents = 10
n_iterations = 100

# Initialise agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i, environment, n_rows, n_cols))


#Define function that adds up all the store values in all the agents.
def sum_agent_stores():
    return sum([agent.store for agent in agents])
#Define a function  that adds up all the values in environment
def sum_environment():
    return sum(sum(environment,[]))      


# Move agents

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = n_cols -1
# The maximum y coordinate.
y_max = n_rows -1
# Apply movement constraints.
for iteration in range(n_iterations):
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
    #Print out sums and check that the total amount of resource and store in the system is not changing after each iteration of the model.    
    print("Iteration", iteration, "Total resource:", (sum_agent_stores() + sum_environment()), "Total store:", sum_agent_stores())      
    
print(agents)
#a function to write out the values of environment to a file 
io.write_data('/Users/zivarhagverdiyeva/Documents/python/data/input/write.txt', environment)





# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4

def get_distance(x0, y0, x1, y1):
    euc = math.sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
    return euc

x0 = 0
y0 = 0
x1 = 3
y1 = 4

print(get_distance(x0,y0,x1,y1))

# Plot
plt.imshow(environment)
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)
plt.show()



#max  and min distance calculation


def get_distances(agents):
    max_distance = 0
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
            max_distance = max(max_distance, distance)
            min_distance = min(min_distance, distance)
    return (min_distance, max_distance)

min_distance, max_distance = get_distances(agents)
print("Maximum distance between any two agents:", max_distance)
print("Minimum distance between any two agents:", min_distance)
   