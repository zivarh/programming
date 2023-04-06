import imageio.v2 as imageio
import os
import random
import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import operator
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry as geometry
import requests
import bs4

#max distance calculation
def max_distance(agents):
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+1, len(agents)):
            b = agents[j]
            distance = geometry.get_distance(a.x, a.y, b.x, b.y)
            max_distance = max(max_distance, distance)
    return (max_distance)
    

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

# For storing images
images = []



def plot():
        fig.clear()
        plt.ylim(y_min, y_max)
        plt.xlim(x_min, x_max)
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
            global ite
            filename = '../../data/output/images/image' + str(ite) + '.png'
            plt.savefig(filename)
            images.append(imageio.imread(filename))
            plt.show
        imageio.mimsave('../../data/output/out.gif', images, fps=3)
def update(frames):
        # Model loop
        global carry_on
        #for ite in range(1, n_iterations + 1):
        print("Iteration", frames)
        # Move agents
        print("Move and eat")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
        print("Share")
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store_shares to store and set store_shares back to zero
        for i in range(n_agents):
            #print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        #print(agents)
        # Print the maximum distance between all the agents
        print("Maximum distance between all the agents", max_distance)
        # Print the total amount of resource
        sum_as = sum_agent_stores()
        print("sum_agent_stores", sum_as)
        sum_e = sum_environment()
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))

        # Stopping condition
        # Random
        if random.random() < 0.1:
            if sum_as / n_agents > 80:
                carry_on = False
                print("stopping condition")

        # Plot
        global ite
        plot()
        ite = ite+1


def gen_function():
    global ite
    global carry_on
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Set the Write data menu to normal.
        menu_0.entryconfig("Write data", state="normal")
        data_written = True
def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()

def output():
    # Write data
    print("write data")
    io.write_data('../../data/output/out.txt', environment)
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)    
if __name__ == '__main__':
    environment, n_rows, n_cols = io.read_data()
    random.seed(0)
    n_agents = 10
    n_iterations = 100
    

    url = 'https://agdturner.github.io/resources/abm9/data.html'
    r = requests.get(url, verify=False)
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)
    agents = []
    for i in range(n_agents):
        # Create an agent
        y = int(td_ys[i].text) + 99
        x = int(td_xs[i].text) + 99
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols, x, y))
        print(agents[i].agents[i])
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

    fig = matplotlib.pyplot.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    # GUI
    root = tk.Tk()
    root.wm_title("Agent Based Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    menu_0 = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=menu_0)
    menu_0.add_command(label="Run model", command=lambda: run(canvas))
    menu_0.add_command(label="Write data", command=lambda: output())
    menu_0.add_command(label="Exit", command=lambda: exiting())
    menu_0.entryconfig("Write data", state="disabled")
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    tk.mainloop()
    plt.show()






