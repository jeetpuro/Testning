import unittest
from estimate_pi import estimate_pi, PiFileWriter

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01) #repeatable
        
        self.assertGreater(pi_actual, 3.14) # our
        self.assertLess(pi_actual, 3.15) # our


if __name__ == '__main__':
    unittest.main()
