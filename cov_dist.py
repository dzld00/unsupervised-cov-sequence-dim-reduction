# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:11:37 2019

@author: dmy
"""

import numpy as np
from numpy.linalg import inv, norm, det
from scipy.linalg import logm
from functools import reduce 

# distance between unit-determinant SPDMs
def cov_dist_unit(punit1, punit2):
    p12 = np.sqrt(reduce(np.dot, [inv(punit1), np.square(punit2), inv(punit1)]))
    
    A12 = logm(p12)
    
    return norm(A12)

# distance between any SPDMs
def cov_dist(p1, p2):
    n = p1.shape[0]
    
    pdet1 = det(p1)
    pdet2 = det(p2)
    
    punit1 = p1 / (np.power(pdet1, (1/n)))
    punit2 = p2 / (np.power(pdet2, (1/n)))
    
    square_d = np.square(cov_dist_unit(punit1, punit2)) + np.multiply((1 / n), np.square(np.log(pdet1) - np.log(pdet2)))
    
    return np.sqrt(square_d)
