class Elevator:
    '''
    A class for representing a simple elevator.
    Attributes:
        start_floor (int): the starting floor for the elevator
        current_floor (int): the current floor for the elevator
        max_floors (int): the maximum number of floors in the elevator
        seconds_per_floor (int): the number of seconds it takes for the elevator to move one floor.
    '''
   
    def __init__(self, start_floor, max_floors, seconds_per_floor):
        '''The constructor for the elevator. It sets all the starting values for the elevator.
        
        Parameters:
            start_floor (int): the starting floor for the elevator
            max_floors (int): the maximum number of floors in the elevator
            seconds_per_floor (int): the number of seconds it takes for the elevator to move one floor.
        '''
        self.start_floor = start_floor
        self.current_floor = start_floor
        self.max_floors = max_floors
        self.seconds_per_floor = seconds_per_floor

    def get_distance_to_floor(self, floor):
        ''' Function for getting the difference between the current floor and the given floor. 
        
        The returned value is positive if the elevator is moving up and negative if the elevator is moving down.

        Parameters:
            floor (int): the goal floor to find the distance to

        Returns:
            The difference between the current floor in the elevator and the given floor. 
        '''
        return floor - self.current_floor

    def get_time_to_floor(self, floor):
        '''Function for getting the time to get to the given floor from the current floor. It uses the `seconds_per_floor` parameter to calculate this. 

        Parameters:
            floor (int): the goal floor to find the time to

        Returns:
            The time it would take for the elevator to go between the current floor and the given floor.
        '''
        return abs(self.seconds_per_floor*self.get_distance_to_floor(floor))

    def update_floor(self, new_floor):
        '''Updates the current floor of the elevator. 

        Parameters:
            floor (int): the new current floor of the elevator.
        '''
        self.current_floor = new_floor

    def get_floor_info(self, floor):
        '''This function returns the current floor, the distance to the given floor, and the time to the given floor. 

        Parameters:
            floor (int): the goal floor
        
        Returns:
            An array of length 3 containing the current floor, the distance between the given floor and the current floor, 
            and the time it would take to go from the given floor to the current floor, in that order.
        '''
        if(floor>self.max_floors):
            floor = self.max_floors
        distance = self.get_distance_to_floor(floor)
        time = self.get_time_to_floor(floor)
        return [self.current_floor, distance, time]

    def get_floor_order_nearest(self, floor_list):
        '''Given a list of floors, return a list of floors sorted by the closest distance to the previous floor.

        Parameters:
            floor_list (array of ints): An array of floors
        
        Returns:
            The floor_list array, sorted by distance to current_floor. 
        '''
        sorted_indices = sorted(range(len(floor_list)), key=lambda i: abs(floor_list[i]-self.start_floor))
        return [floor_list[x] for x in sorted_indices]
