import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__) + "..")
try:
    from Controllability import check_controllability as m
except:
    raise

class Test(unittest.TestCase):

    def test1(self):
        m.show_result = False
        m.main()

if __name__ == '__main__':
    unittest.main()
