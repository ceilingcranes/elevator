from math import floor
from elevator import Elevator

def get_floor_list_input(max_floor):
    is_error = True
    while(is_error):
        try:
            floor_list = input("Please enter a comma seperated list of requested floors (or nothing to end program):\n")
            # check to see if the input was an empty string
            if(floor_list): 
                floor_list = [int(x) for x in floor_list.split(",")]

                if (sum([x>max_floor for x in floor_list]) or min(floor_list)<=0):
                    raise IndexError
            
            is_error = False
        except KeyboardInterrupt:
            # Allow program to be ended with ctrl+c
            return []
        except:
            print("Invalid floor request. Please enter a comma seperated list of positive integers that are less than the max floor.")

    return floor_list

def main():
    floor_format_string = "Requested floor: {}, current floor: {}, number of floors until requested floor: {}, time until floor: {} seconds"
    seconds_per_floor = 10
    try:
        start_floor = int(input("Please enter a starting floor for the elevator (default 1):\n") or 1)
        max_floor = int(input("Please enter the maximum number of elevator floors (default 10)\n") or 10)

        if(start_floor < 0 or max_floor<0 or start_floor>max_floor):
            raise ValueError

    except ValueError:
        print("Invalid value. Please enter one positive integer for start and max floors, and a comma-seperated list of integers for the floor list.")
    
    floor_list = get_floor_list_input(max_floor)

    while(floor_list):
        elevator_info = Elevator(start_floor, max_floor, seconds_per_floor)
        total_time = 0
        print("===========")
        for floor in elevator_info.get_floor_order_nearest(floor_list):
            floor_info = elevator_info.get_floor_info(floor)
            print(floor_format_string.format(floor, floor_info[0], floor_info[1], floor_info[2]))
            total_time += floor_info[2]
            elevator_info.update_floor(floor)

        print("Total time: {} seconds".format(total_time))
        floor_list = get_floor_list_input(max_floor)


if __name__=="__main__":
    main()