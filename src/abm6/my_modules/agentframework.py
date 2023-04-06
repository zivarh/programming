import random
import my_modules.geometry as geometry
class Agent:
    def __init__(self, agents, i, environment, n_rows, n_cols):
        """
        The constructor method.

        Parameters
        ----------
        agents : List
            A list of Agent instances.
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.

        Returns
        -------
        None.

        """
        # Initialize instance variables
        self.agents = agents
        self.i = i
        self.environment = environment
        # Set initial x and y positions randomly within the environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        # Set initial store and store_shares values
        self.store = random.randint(0, 99)
        self.store_shares = 0

    def __str__(self):
        """
        String representation of the Agent instance.

        Returns
        -------
        str
            String representation of the Agent instance.

        """
        return "Agent {}: ({}, {})".format(self.i, self.x, self.y)
    def __repr__(self):
        """
        Representation of the Agent instance.

        Returns
        -------
        str
            Representation of the Agent instance.

        """
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        """
        Moves the Agent instance randomly in the x and y directions.

        Parameters
        ----------
        x_min : Integer
            The minimum x value of the environment.
        y_min : Integer
            The minimum y value of the environment.
        x_max : Integer
            The maximum x value of the environment.
        y_max : Integer
            The maximum y value of the environment.

        Returns
        -------
        None.

        """
        # Move the Agent instance randomly in the x direction
        rn = random.randint(0,99)
        if rn< 55:
            self.x += 2
        else:
            self.x -= 2
        # Move the Agent instance randomly in the y direction
        rn = random.randint(0,99)
        if rn< 55:
            self.y += 1
        else:
            self.y -= 1  
        # Check if the Agent instance has moved outside the boundaries of the environment    
        if self.x < x_min:
            self.x = x_min
        if self.x > x_max:
            self.x = x_max
        if self.y < y_min:
            self.y = y_min
        if self.y > y_max:
            self.y = y_max
    def eat(self):
        """
        The Agent instance eats food from the environment.

        Returns
        -------
        None.

        """
        # If there is more than 10 food at the current position, eat 10 and add to store
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        # Otherwise, eat all remaining food and add to store    
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            
    def share(self, neighbourhood):
        # Create a list of agents in neighbourhood
        neighbours = []
        
        print(self.agents[self.i])
        for a in self.agents:
            distance = geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares        
          