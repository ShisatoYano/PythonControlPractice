import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__) + "..")
try:
    from TwoWheelModel import two_wheel_model as m
except:
    raise

class Test(unittest.TestCase):

    def test1(self):
        m.show_plot = False
        m.main()

if __name__ == '__main__':
    unittest.main()
