# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 10/24/2018

Some useful functions for analyzing Hello Quantum Puzzles
"""

import numpy as np;
import matplotlib.pyplot as plt

#%%

def pBarsStd( st ) :
    """
    Display the probability of measuring each of the four standard basis
    outcomes. 
    """   
    
    
    fig, ax = plt.subplots()
    ax.bar(np.arange(4), abs(st)**2 , 0.25, color='b')
    ax.set_xlabel('Standard Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring the Standard Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('00', '01', '10', '11'))
    ax.set_ylim((0,1.1))
        
    plt.show()
    
def pBarsBell( st ) :
    """
    Display the probability of measuring each of the four Bell basis
    outcomes. 
    """
    H = np.array([[1,1],[1,-1]])
    b_st=np.flip((1/2)*( np.kron(H,H).dot(np.flip(st)) ))
    
    fig, ax = plt.subplots()
    ax.bar(np.arange(4), abs(b_st)**2 , 0.25, color='b')
    ax.set_xlabel('Bell Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])
    ax.set_title('Probability of Measuring the Bell Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('++', '+-', '-+', '--'))
    ax.set_ylim((0,1.1))
        
    plt.show()

#%%


    
    
