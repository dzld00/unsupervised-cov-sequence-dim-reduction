# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:16:42 2019

@author: dmy
"""
from ops import *
import os

class DimReduction(object):
    def __init__(self,args):
        self.covseqs_dir = args.covseqs_dir
        self.m = args.m
        self.output = args.output
        
        print("# target dimension : ", self.m)
        print("# file name of covariance sequences : ", self.covseqs_dir)
    
    def Optimize(self):
        covseqs = np.load(self.covseqs_dir + '.npy')
        n,n,T,L = covseqs.shape
        
        traj = np.zeros((self.m, self.m, T, L))
        B = np.zeros((n,self.m))
        
        for j in range(L):
            B = ManoptOptimization(covseqs[:,:,:,j],self.m)
            for i in range(T):
                traj[:,:,i,j] = reduce(np.dot, [B.T, covseqs[:,:,i,j], B])
                
        name = self.output
        
        np.save(name, traj)
                
        
        
        
        
    