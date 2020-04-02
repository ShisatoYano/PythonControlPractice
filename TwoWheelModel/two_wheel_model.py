"""
Two wheel motion model sample

author: Shisato Yano (@4310sy)
"""

from control.matlab import *
import numpy as np

class TwoWheelModel:

    def __init__(self, tr, td):
        """
        Initialize two wheel model

        tr: tire radius [m]
        td: tread [m]
        """

        self.tire_radius_m = tr
        self.tread_m = td

    def calculate_input(self, tsr, tsl):
        """
        tsr: tire speed right [m/s]
        tsl: tire speed left [m/s]
        """

        mat = np.ndarray([[self.tire_radius_m/2, self.tire_radius_m/2],
                         [self.tire_radius_m/self.tread_m, -self.tire_radius_m/self.tread_m]])

        vec = np.ndarray([[tsr], [tsl]])

        input_vec = np.dot(mat, vec)

        return input_vec

def main():
    print("Run " + __file__)

    # set parameters
    tire_radius_m = 0.08
    tread_m = 0.26

    # initialize
    two_wheel = TwoWheelModel(tire_radius_m, tread_m)

if __name__ == '__main__':
    main()