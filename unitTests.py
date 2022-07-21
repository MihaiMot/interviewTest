import unittest
import interviewTestLSG_part1 as lsg
 


class TestCountLight(unittest.TestCase):

    def test_count_lights_part1(self):
        self.assertEqual(lsg.create_matrix(1000, 1000), 998004)


if __name__ == '__main__':
    unittest.main()