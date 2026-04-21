import unittest
from estimate_pi import estimate_pi, PiFileWriter
import time

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01) #repeatable

# question 2 and 3 --------------------------------------------------------
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
# --------------------------------------------------------


# question 4 --------------------------------------------------------------------

class FakePiFileWriter:
    """Fake test double: stores written content in memory instead of disk."""
    def init(self):
        self.written_content = None
        self.written_path = None

    @staticmethod
    def write(content, file_path):
        # We capture via a class-level store for static method compatibility
        FakePiFileWriter.written_content = content
        FakePiFileWriter.written_path = file_path


class TestPiFileWriter(unittest.TestCase):
    def test_fake_writer_stores_content(self):
        """Test that the writer receives the correct pi string."""
        pi_value = "3.1415" # gör egna 
        FakePiFileWriter.write(pi_value, "fake/path.txt")
        self.assertEqual(FakePiFileWriter.written_content, pi_value)
        self.assertEqual(FakePiFileWriter.written_path, "fake/path.txt")
        # print(FakePiFileWriter.written_content)
        # 2.643s
#--------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()