"""
Two wheel motion model sample

author: Shisato Yano (@4310sy)
"""

import numpy as np
from math import cos, sin
import matplotlib.pyplot as plt
from PIL import Image
import os

show_plot = True

DELTA_TIME = 0.1 # time tick [s]
SIM_TIME = 10 # simulation time [s]

class TwoWheelModel:

    def __init__(self, tr, td):
        """
        Initialize two wheel model

        tr: tire radius [m]
        td: tread [m]
        """

        self.tire_radius_m = tr
        self.tread_m = td

    def calculate_input(self, tasr, tasl):
        """
        tasr: tire angular speed right [rad/s]
        tasl: tire angular speed left [rad/s]
        :return: speed input [m/s], yaw rate input [rad/s]
        """

        mat = np.array([[self.tire_radius_m/2, self.tire_radius_m/2],
                         [self.tire_radius_m/self.tread_m, -self.tire_radius_m/self.tread_m]])

        vec = np.array([[tasr], [tasl]])

        input_vec = np.dot(mat, vec)

        return input_vec

    def control_input(self, time):
        if time <= 5.0:
            tasr = 0.3 # [rad/s]
            tasl = 0.1 # [rad/s]
        else:
            tasr = 0.1 # [rad/s]
            tasl = 0.3 # [rad/s]

        input_vec = self.calculate_input(tasr, tasl)

        return input_vec

    def output_equation(self, state, input):
        out_mat = np.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1]])

        dirc_mat = np.array([[cos(state[2, 0]) * DELTA_TIME, 0],
                             [sin(state[2, 0]) * DELTA_TIME, 0],
                             [0, 1]])

        out_vec = np.dot(out_mat, state) + np.dot(dirc_mat, input)

        return out_vec

    def create_gif(self, im_num):
        images = []

        for num in range(im_num):
            im_name = str(num) + '.png'
            im = Image.open(im_name)
            images.append(im)
            os.remove(im_name)

        images[0].save('TwoWheelModel.gif', save_all=True, append_images=images[1:], loop=0, duration=60)

def main():
    print("Run " + __file__)

    # set parameters
    tire_radius_m = 0.08
    tread_m = 0.26

    # initialize
    two_wheel = TwoWheelModel(tire_radius_m, tread_m)

    # elapsed time
    time = 0.0

    # state vector: x, y, yaw
    st_vec = np.zeros((3, 1))

    # figure
    ax_xy = plt.subplot(1, 1, 1)
    plt_xy, = ax_xy.plot([], [], '.', c='b', ms=10)

    # image number
    im_num = 0

    # simulation
    st_x = []
    st_y = []
    st_yaw = []
    while SIM_TIME >= time:
        time += DELTA_TIME

        input_vec = two_wheel.control_input(time)

        st_vec = two_wheel.output_equation(st_vec, input_vec)

        st_x.append(st_vec[0, 0])
        st_y.append(st_vec[1, 0])
        st_yaw.append(st_vec[2, 0])

        if show_plot:
            plt_xy.set_data(st_x, st_y)
            ax_xy.set_xlim([-0.1, 0.1])
            ax_xy.set_ylim([0.0, 0.1])
            ax_xy.axis('equal')
            ax_xy.grid(True)
            plt.savefig(str(im_num) + '.png')
            im_num += 1
            plt.pause(0.001)

    two_wheel.create_gif(im_num)

    if show_plot:
        plt.plot(st_x, st_y, ".b")
        plt.grid(True)
        plt.axis("equal")
        plt.xlabel("X [m]")
        plt.ylabel("Y [m]")
        plt.show()

if __name__ == '__main__':
    main()
    