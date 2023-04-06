import imageio
import os
import random
import math
import matplotlib.pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry


#Define function that adds up all the store values in all the agents.
def sum_agent_stores():
    return sum([agent.store for agent in agents])
#Define a function  that adds up all the values in environment
def sum_environment():
    return sum(sum(environment,[]))      

# Create directory to write images to.
try:
    os.makedirs('../../data/output/images')
except FileExistsError:
    print("path exists")


#max distance
def max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = geometry.get_distance(a.x, a.y, b.x, b.y)
            max_distance = max(max_distance, distance)
    return (max_distance)





if __name__ == '__main__':
    #read file
    environment, n_rows, n_cols = io.read_data()
    # Set the pseudo-random seed for reproducibility
    random.seed(0)
    
    n_agents = 10
    n_iterations = 10
    
    # Initialise agents
    agents = []
    # For storing images
    global ite
    ite = 1
    images = []
    for i in range(n_agents):
    # Create an agent
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
    # Variables for constraining movement.
    # The minimum x coordinate.
    x_min = 0
    # The minimum y coordinate.
    y_min = 0
    # The maximum x coordinate.
    x_max = n_cols -1
    # The maximum y coordinate.
    y_max = n_rows -1
    neighbourhood = 50

    # Main simulation loop
    for ite in range(1, n_iterations + 1):
        print("Iteration", ite)
        # Move agents
        print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store_shares to store and set store_shares back to zero
        for i in range(n_agents):
            print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        print(agents)
        # Print the maximum distance between all the agents
        print("Maximum distance between all the agents", max_distance)
        # Print the total amount of resource
        sum_as = sum_agent_stores()
        print("sum_agent_stores", sum_as)
        sum_e = sum_environment()
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))
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
        #create plots; save these as images in PNG format files;
        filename = 'data/output/images/image' + str(ite) + '.png'
        #filename = 'data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
    #images can be turned into an animated GIF format    
    imageio.mimsave('../../data/output/out.gif', images, fps=3)
    io.write_data('../../data/input/write.txt', environment)





