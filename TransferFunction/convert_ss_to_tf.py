"""
Conversion sample from state space model
to transfer function model

State equation example
x(t+1) = A * x(t) + B * u(t)
A: 3 x 3 matrix
B: 3 x 2 matrix

Output equation example
y(t) = C * x(t) + D * u(t)
C: 3 x 3 matrix
D: 0

Transfer function example
2-Input 3-Output

author: Shisato Yano (@4310sy)
"""

import numpy as np
from control.matlab import ss, ss2tf

def define_state_space_model(A, B, C, D):
    ss_model = ss(A, B, C, D)
    return ss_model

def convert_transfer_function_model(ss_model):
    tf_model = ss2tf(ss_model)
    return tf_model

def main():
    print("Run " + __file__)

    # define matrix
    A = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])

    B = np.array([[0.05, 0],
                  [0, 0],
                  [0, 0.05]])

    C = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])

    D = 0

    ss_model = define_state_space_model(A, B, C, D)

    tf_model = convert_transfer_function_model(ss_model)

    print('Converted transfer function model')

    print(tf_model)

if __name__ == '__main__':
    main()
