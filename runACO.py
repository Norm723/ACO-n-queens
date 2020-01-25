# -*- coding: utf-8 -*-
"""
@author: ofersh@telhai.ac.il
"""
from ACO import AntforTSP as ACO
import numpy as np
import os


if __name__ == "__main__" :
    Niter = 50
    Nant = 200
    n_queens = 4
    ant_colony = ACO(n_queens,Nant, Niter, rho=0.95, alpha=1, beta=3)
    shortest_path = ant_colony.run()
    print("shotest_path: {}".format(shortest_path))