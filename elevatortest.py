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
    


if __name__=="__main__":
    unittest.main()