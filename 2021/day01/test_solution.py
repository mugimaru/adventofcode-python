import unittest
import solution

class TestDay01(unittest.TestCase):
    TEST_INPUT = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']

    def test_part1(self):
        self.assertEqual(solution.part1(self.TEST_INPUT), 7)

    def test_part2(self):
        self.assertEqual(solution.part2(self.TEST_INPUT), 5)

if __name__ == '__main__':
    unittest.main()