import day3
import unittest
from typing import List
import os


class Day3TestCase(unittest.TestCase):
    def test_load_routes(self):

        input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
        route1, route2 = day3.load_routes(input_file)

        self.assertIsInstance(route1, List)
        self.assertIsInstance(route2, List)

        self.assertGreater(len(route1), 0)
        self.assertGreater(len(route2), 0)

    def test_perform_move(self):

        current_position = (0, 0)
        move = "D1"

        new_position = day3.perform_move(current_position, move)

        self.assertEqual([(0, -1)], new_position)

    def test_perform_moves_for_route(self):
        locations = day3.perform_moves_for_route(["R1"])
        expected_locations = set([(1, 0)])

        self.assertEqual(locations, expected_locations)

    def test_convert_route_string(self):

        route_string = "R1,R2,R3,R4"
        route = day3.convert_route_string_to_list(route_string)

        self.assertEqual(["R1", "R2", "R3", "R4"], route)

    def test_calculate_distance_1(self):
        route1_string = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        route2_string = "U62,R66,U55,R34,D71,R55,D58,R83"

        route1 = day3.convert_route_string_to_list(route1_string)
        route2 = day3.convert_route_string_to_list(route2_string)

        distance = day3.calculate_distance(route1, route2)

        self.assertEqual(159, distance)

    def test_calculate_distance_2(self):
        route1_string = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        route2_string = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

        route1 = day3.convert_route_string_to_list(route1_string)
        route2 = day3.convert_route_string_to_list(route2_string)

        distance = day3.calculate_distance(route1, route2)

        self.assertEqual(135, distance)
