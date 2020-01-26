# -*- coding: utf-8 -*-
"""
@author: ofersh@telhai.ac.il
"""
from ACO import AntforTSP as ACO
import numpy as np
import os


if __name__ == "__main__" :
    Niter = 50
    Nant = 500
    n_queens = 32
    ant_colony = ACO(n_queens,Nant, Niter, rho=0.95, alpha=1, beta=10)
    shortest_path = ant_colony.run()
    for i in range(n_queens):
        for j in range(n_queens):
            if shortest_path[0][i] == j:
                print(1, end='')
            else:
                print(0, end='')
            print(" ", end='')
        print()
    print("shotest_path: {}".format(shortest_path))