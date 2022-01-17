import unittest
from elevator import Elevator

class TestElevator(unittest.TestCase):
    test_elevator = Elevator(2, 10, 1)

    def test_distance_calc(self):
        positive_check = self.test_elevator.get_distance_to_floor(3)
        negative_check = self.test_elevator.get_distance_to_floor(1)
        equals_check = self.test_elevator.get_distance_to_floor(2)

        self.assertEqual(positive_check, 1)
        self.assertEqual(negative_check, -1)
        self.assertEqual(equals_check, 0)

    def test_time_calc(self):
        self.test_elevator = Elevator(2, 10, 1)
        positive_check = self.test_elevator.get_time_to_floor(3)
        negative_check = self.test_elevator.get_time_to_floor(1)
        equals_check = self.test_elevator.get_time_to_floor(2)
        multiple_floors = self.test_elevator.get_time_to_floor(10)

        self.assertEqual(positive_check, 1)
        self.assertEqual(negative_check, 1)
        self.assertEqual(equals_check, 0)
        self.assertEqual(multiple_floors, 8)

    def test_update_floor(self):
        self.test_elevator.update_floor(4)
        self.assertEqual(self.test_elevator.current_floor, 4)
        self.test_elevator.update_floor(2)

    def test_get_floor_info(self):
        floor_info = self.test_elevator.get_floor_info(1)
        self.assertEqual(floor_info, [2, -1, 1])

    def test_get_floor_order_nearest(self):
        floor_list_up = [7, 3, 9]
        ordered_list_up = self.test_elevator.get_floor_order_nearest(floor_list_up)
        self.assertEqual(ordered_list_up, [3, 7, 9])

        floor_list_down = [1, 7, 3]
        ordered_list_down = self.test_elevator.get_floor_order_nearest(floor_list_down)
        self.assertEqual(ordered_list_down, [1, 3, 7])

if __name__=="__main__":
    unittest.main()