"""
Two wheel motion model sample

author: Shisato Yano (@4310sy)
"""

from control.matlab import *

sys2tf = tf([1, 0.5], [1, 5])
print(sys2tf)