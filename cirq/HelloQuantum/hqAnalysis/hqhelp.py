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

def pBarsStdAll( sim ) :
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each standard basis at each step.
    """
    
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = .25
    n_steps = 0
    
    for i, step in enumerate(sim):
        n_steps = i
        st = np.around(step.state(), 3)
        ax.bar(index+(i*bar_width) , abs(st)**2, bar_width,
               label="step " + str(i+1))
        
    ax.set_xlabel('Standard Basis')        
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring the Standard Basis')
    ax.set_xticks(np.arange(4)+(n_steps*bar_width)/2)
    ax.set_xticklabels(('00', '01', '10', '11'))
    ax.set_ylim((0,1.1))
    ax.legend()
    
    fig.tight_layout()
    plt.show()

def pBarsBellAll( sim ) :
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each standard basis at each step.
    """
    
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = .25
    n_steps = 0
    
    H = np.array([[1,1],[1,-1]])
    T = np.kron(H,H)    
    
    for i, step in enumerate(sim):
        n_steps = i
        st_std = np.around(step.state(), 3)
        st_bell = np.flip((1/2)*T.dot(np.flip(st_std)))
        ax.bar(index+(i*bar_width) , abs(st_bell)**2, bar_width,
               label="step " + str(i+1))
        
    ax.set_xlabel('Bell Basis')        
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring the Bell Basis')
    ax.set_xticks(np.arange(4)+(n_steps*bar_width)/2)
    ax.set_xticklabels(('++', '+-', '-+', '--'))
    ax.set_ylim((0,1.1))
    ax.legend()
    
    fig.tight_layout()
    plt.show()

        

