# Elevator test
This repo is for a python example which demonstrates a simple elevator class. The basic api takes in information about the elevator, including the starting floor and the total number of floors, and it will output the current floor, the distance between the current floor and a given floor, and the time it would take for the elevator to reach the given floor.

There's a command line API to access the elevator class and input a list of requested floors. This can be run by using the following command:
```
python3 main.py
```

There are also unittests for the elevator class. These unittests can be run with: 
```
python3 elevatortest.py
```

## Algorithm for determining floor order
The elevator class provides a simple algorithm for determining floor order. This is accessed with `get_floor_order_nearest` function. This method sorts the given floor list by the distance from the current floor. In the case where you're getting a list of floors from the beginning for one elevator, this will be the most efficient way of moving the elevator. 
