import random

class Agent:
    def __init__(self, i, environment, n_rows, n_cols):
        """
        he constructor method.

        Parameters
        ----------
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
        self.i = i
        self.environment = environment
        # Set initial x and y positions randomly within the environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        # Set initial store 
        self.store = 0
        pass
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
        rn = random.randint(0,99)
        # Move the Agent instance randomly in the x direction
        if rn< 55:
            self.x += 2
        else:
            self.x -= 2

        rn = random.randint(0,99)
        # Move the Agent instance randomly in the y direction
        if rn< 55:
            self.y += 2
        else:
            self.y -= 2 
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
        # If there is more than 10 food at the current position, eat 10 and add to store
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10  
        # Otherwise, eat all remaining food and add to store   
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
       
            
          