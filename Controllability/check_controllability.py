"""
Controllability check sample

State equation example
x(t+1) = A * x(t) + B * u(t)
A: 3 x 3 matrix
B: 3 x 2 matrix

Output equation example
y(t) = C * x(t) + D * u(t)
C: 3 x 3 matrix
D: 0

author: Shisato Yano (@4310sy)
"""

import numpy as np
from control.matlab import ss, ctrb

def define_state_space_model(A, B, C, D):
    ss_model = ss(A, B, C, D)
    print('State space model')
    print(ss_model)

def check_controllability(A, B):
    cntrb_mat = ctrb(A, B)
    rank = np.linalg.matrix_rank(cntrb_mat)
    print('Controllability matrix')
    print(cntrb_mat)
    print('')
    print('Rank is', rank)
    print('')
    if rank != A.shape[0]:
        print('This system is not controllability\n')
    else:
        print('This system is controllability\n')

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

    define_state_space_model(A, B, C, D)

    check_controllability(A, B)

if __name__ == '__main__':
    main()
