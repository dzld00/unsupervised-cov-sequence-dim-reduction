# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:26:19 2019

@author: dmy
"""
import numpy as np
from functools import reduce
from pymanopt import Problem
from pymanopt.manifolds import Stiefel
from pymanopt.solvers import TrustRegions

def cost(A,x):
    T = A.shape[2]
    c = 0
    
    for i in range(T):
        c = c - (reduce(np.dot, [x.T, A[:,:,i], x, x.T, A[:,:,i], x])).trace()
    
    return c
    
def egrad(A,x):
    T = A.shape[2]
    gr = np.zeros(x.shape)
    
    for i in range(T):
        gr = gr - 4 * reduce(np.dot, [A[:,:,i], x, x.T, A[:,:,i], x])
    
    return gr

def ManoptOptimization(A,m):
    n = A.shape[0]
    T = A.shape[2]
    manifold = Stiefel(n,m,k=1)
    
    mycost = lambda x: cost(A,x)
    myegrad = lambda x: egrad(A,x)
    problem = Problem(manifold=manifold, cost=mycost, egrad=myegrad)
    
    solver = TrustRegions()
    print('# Start optimization using solver: trustregion')
    Xopt = solver.solve(problem)
    
    return Xopt
    
    
    