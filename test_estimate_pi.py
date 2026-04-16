import unittest
from estimate_pi import estimate_pi, PiFileWriter
import time

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01) #repeatable

    def test_boundary(self): #Test1
        pi_actual = estimate_pi(1000000)
        self.assertGreater(pi_actual, 3.13)
        self.assertLess(pi_actual, 3.15) 

    def test_fast(self): #Test2
        start_time = time.time()
        self.test_estimate_pi()
        end_time = time.time()
        # self.assertTrue((end_time - start_time) > 100)
        print("time: ", end_time - start_time)

if __name__ == '__main__':
    unittest.main()
