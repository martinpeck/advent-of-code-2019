from day2 import parse_instructions, run_program
import unittest


class Day1TestCase(unittest.TestCase):
    def test_parse_instructions(self):
        self.assertEqual([1, 0, 0, 0, 99], parse_instructions("1,0,0,0,99"))
        self.assertEqual([2, 3, 0, 3, 99], parse_instructions("2,3,0,3,99"))
        self.assertEqual([2, 4, 4, 5, 99, 0], parse_instructions("2,4,4,5,99,0"))
        self.assertEqual(
            [1, 1, 1, 4, 99, 5, 6, 0, 99], parse_instructions("1,1,1,4,99,5,6,0,99")
        )

    def test_run_program_1(self):
        instructions = [1, 0, 0, 0, 99]
        expected = [2, 0, 0, 0, 99]
        self.assertEqual(expected, run_program(instructions))

    def test_run_program_2(self):
        instructions = [2, 3, 0, 3, 99]
        expected = [2, 3, 0, 6, 99]
        self.assertEqual(expected, run_program(instructions))

    def test_run_program_3(self):
        instructions = [2, 4, 4, 5, 99, 0]
        expected = [2, 4, 4, 5, 99, 9801]
        self.assertEqual(expected, run_program(instructions))

    def test_run_program_4(self):
        instructions = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(expected, run_program(instructions))

    def test_run_program_5(self):
        instructions = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected, run_program(instructions))
