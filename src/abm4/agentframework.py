import random

class Agent:
    def __init__(self, i):
        """
        The constructor method.

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
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
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
         # Move the Agent instance randomly in the x direction
        rn = random.random()
        if rn< 0.5:
            self.x += 1
        else:
            self.x -= 1
        # Move the Agent instance randomly in the y direction
        rn = random.random()
        if rn< 0.5:
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