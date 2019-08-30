# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:24:49 2019

@author: dmy
"""
import argparse
import numpy as np
from DimReduction import DimReduction
from sys import exit


def parse_args():
    desc = "Implementation of DimReduction"
    parser = argparse.ArgumentParser(description=desc)
    
    parser.add_argument('--covseqs_dir', type= str, default= 'data', help='Directory to covariance sequences')
    parser.add_argument('--m', type=int, default=3, help='The target dimension')
    parser.add_argument('--output', type=str, default='output', help='Name of saved results')
      
    return parser.parse_args()
    
def main():
    args = parse_args()
    if args is None:
        print('No input argument')
        exit()
        
    res = DimReduction(args)
    
    res.Optimize()
    print("Optimization finished!")
    
if __name__ == '__main__':
    main()
    
    
    
    
