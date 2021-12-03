import unittest
import solution

class TestDay03(unittest.TestCase):
    TEST_INPUT = [
      '00100',
      '11110',
      '10110',
      '10111',
      '10101',
      '01111',
      '00111',
      '11100',
      '10000',
      '11001',
      '00010',
      '01010'
    ]

    def test_part1(self):
        self.assertEqual(solution.part1(self.TEST_INPUT), 198)

    def test_part2(self):
        self.assertEqual(solution.part2(self.TEST_INPUT), 230)

if __name__ == '__main__':
    unittest.main()