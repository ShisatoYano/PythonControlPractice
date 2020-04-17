import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__) + "..")
try:
    from Observability import check_observability as m
except:
    raise

class Test(unittest.TestCase):

    def test1(self):
        m.main()

if __name__ == '__main__':
    unittest.main()
