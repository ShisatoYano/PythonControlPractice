import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__) + "..")
try:
    from TransferFunction import convert_ss_to_tf as m
except:
    raise

class Test(unittest.TestCase):

    def test1(self):
        m.main()

if __name__ == '__main__':
    unittest.main()
