import unittest
from estimate_pi import estimate_pi, PiFileWriter

class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

# question 3 -------------------------------------------------------------------
    def test_boundary(self): #Test1
        pi_actual = estimate_pi(1000000)
        self.assertGreater(pi_actual, 3.14)
        self.assertLess(pi_actual, 3.15)

    def test_returns_float(self): #Test2
        pi_actual = estimate_pi(1000000)
        self.assertIsInstance(pi_actual, float)
# -------------------------------------------------------------------------------

# question 4 --------------------------------------------------------------------

class FakePiFileWriter:
    """Fake test double: stores written content in memory instead of disk."""
    def init(self):
        self.written_content = None
        self.written_path = None

    @staticmethod
    def write(content, file_path):
        # writes to init variables so simulate a file
        FakePiFileWriter.written_content = content
        FakePiFileWriter.written_path = file_path

class TestPiFileWriter(unittest.TestCase):
    def test_fake_writer_stores_content(self):
        """Test that the writer receives the correct pi string."""
        pi_value = "3.1415"
        FakePiFileWriter.write(pi_value, "fake/path.txt")

        # below we use assert to check inside the init to verify 
        self.assertEqual(FakePiFileWriter.written_content, pi_value)
        self.assertEqual(FakePiFileWriter.written_path, "fake/path.txt")
#---------------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()