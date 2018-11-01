    # -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 10/24/2018

Some useful functions for analyzing Hello Quantum Puzzles
"""

import numpy as np;
import matplotlib.pyplot as plt

#%%

def toBell( st ):
    H = np.array([[1,1],[1,-1]])
    T = (0.5)*np.kron(H,H)    
    
    return T.dot(st)

def toSB( st ):
    H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
    T = np.kron(np.eye(2),H)    

    return T.dot(st)

def toBS( st ):
    H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
    T = np.kron(H,np.eye(2))    

    return T.dot(st)
    

#%%

def pStd( st ):
    """
    Compute the measurement probabilities for a std/std measurement.
    This gets at the southern circle of the center 4.
    """    
    return abs(st)**2    

def pBell( st ):
    """
    Compute the measurement probabilities for a bell/bell measurement.
    This gets at the northern circle of the center 4.
    """    
        
    return abs(toBell(st))**2    

def pSB( st ):
    """
    Compute the measurement probabilities for a std/bell measurement.
    This gets at the eastern circle of the center 4.
    """    
    
    return abs(toSB(st))**2    

def pBS( st ):
    """
    Compute the measurement probabilities for a bell/std measurement.
    This gets at the northern circle of the center 4.
    """    
        
    return abs(toBS(st))**2        


#%%

def pBarsStd( st ) :
    """
    Display the probability of measuring each of the four standard basis
    outcomes. 
    """       
    
    fig, ax = plt.subplots()
    ax.bar(np.arange(4), pStd(st) , 0.25, color='b')
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
    
    fig, ax = plt.subplots()
    ax.bar(np.arange(4), pBell(st) , 0.25, color='b')
    ax.set_xlabel('Bell Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])
    ax.set_title('Probability of Measuring the Bell Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('++', '+-', '-+', '--'))
    ax.set_ylim((0,1.1))
        
    plt.show()
    
def pBarsSB( st ) :
    """
    Display the probability of measuring each of the four std/bell 
    hybrid basis
    """
        
    fig, ax = plt.subplots()
    ax.bar(np.arange(4), pSB(st) , 0.25, color='b')
    ax.set_xlabel('Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])
    ax.set_title('Probability of Measuring the Std/Bell Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('0+', '0-', '1+', '1-'))
    ax.set_ylim((0,1.1))
        
    plt.show()    
    
def pBarsBS( st ) :
    """
    Display the probability of measuring each of the four std/bell 
    hybrid basis
    """
        
    fig, ax = plt.subplots()
    ax.bar(np.arange(4), pBS(st) , 0.25, color='b')
    ax.set_xlabel('Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])
    ax.set_title('Probability of Measuring the Bell/Std Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('+0', '+1', '-0', '-1'))
    ax.set_ylim((0,1.1))
        
    plt.show()    

#%%

def pBarsStdAll( sim ) :
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each standard basis at each step.
    """
    
    states = np.vstack( [s.state()for s in sim ]  )
    
    fig, ax = plt.subplots()    
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width
    
    
    for i,st in enumerate(states):        
        ax.bar(index+(i*bar_width) , pStd(st), bar_width,
               label="step " + str(i+1))
        
    ax.set_xlabel('Standard Basis')        
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring the Standard Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
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
    
    states = np.vstack( [s.state()for s in sim ]  )
       
    
    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width
    
    for i,st in enumerate(states):        
        ax.bar(index+(i*bar_width) , pBell(st) , bar_width,
               label="step " + str(i+1))
        
    ax.set_xlabel('Bell Basis')        
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring the Bell Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('++', '+-', '-+', '--'))
    ax.set_ylim((0,1.1))
    ax.legend()
    
    fig.tight_layout()
    plt.show()

def pBarsSBAll( sim ) :
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each ... std/bell hybrid basis
    """
    
    states = np.vstack( [s.state()for s in sim ]  )    
    
    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width
    
    for i,st in enumerate(states):        
        ax.bar(index+(i*bar_width) , pSB(st) , bar_width,
               label="step " + str(i+1))
        
    ax.set_xlabel('Basis')        
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring in a Std/Bell Hybrid Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('0+', '0-', '1+', '1-'))
    ax.set_ylim((0,1.1))
    ax.legend()
    
    fig.tight_layout()
    plt.show()

def pBarsBSAll( sim ) :
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each ... bell/std hybrid basis
    """
    
    states = np.vstack( [s.state()for s in sim ]  )
    
    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width
    
    for i,st in enumerate(states):        
        ax.bar(index+(i*bar_width) , pBS(st) , bar_width,
               label="step " + str(i+1))
        
    ax.set_xlabel('Basis')        
    ax.set_ylabel('Probability')
    ax.set_yticks([0,.25,.5,.75,1])    
    ax.set_title('Probability of Measuring in a Bell/Std Hybrid Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('+0', '+1', '-0', '-1'))
    ax.set_ylim((0,1.1))
    ax.legend()
    
    fig.tight_layout()
    plt.show()        

#%%
    

def hqGrid( st , tofile=False,name=""):
    """
    Plot probability distributions for the two qubit measurment outcomes
    Grid for Hello Quantum
    """
    
    fig,ax = plt.subplots(2,2)
    
     #North Bell
    ax[0][0].bar(np.arange(4), pBell(st) , 0.25, color='b')
    ax[0][0].set_xlabel('Bell Basis')
    ax[0][0].set_ylabel('Probability')
    ax[0][0].set_yticks([0,.25,.5,.75,1])
    ax[0][0].set_title('Bell Measurement')
    ax[0][0].set_xticks(np.arange(4))
    ax[0][0].set_xticklabels(('++', '+-', '-+', '--'))
    ax[0][0].set_ylim((0,1.1))
    
    #West BS
    ax[1][0].bar(np.arange(4), pBS(st) , 0.25, color='b')
    ax[1][0].set_xlabel('Basis')
    ax[1][0].set_ylabel('Probability')
    ax[1][0].set_yticks([0,.25,.5,.75,1])
    ax[1][0].set_title('Bell/Std Measurement')
    ax[1][0].set_xticks(np.arange(4))
    ax[1][0].set_xticklabels(('+0', '+1', '-0', '-1'))
    ax[1][0].set_ylim((0,1.1))
    
    #East SB
    ax[0][1].bar(np.arange(4), pSB(st) , 0.25, color='b')
    ax[0][1].set_xlabel('Basis')
    ax[0][1].set_ylabel('Probability')
    ax[0][1].set_yticks([0,.25,.5,.75,1])
    ax[0][1].set_title('Std/Bell Measurement')
    ax[0][1].set_xticks(np.arange(4))
    ax[0][1].set_xticklabels(('0+', '0-', '1+', '1-'))
    ax[0][1].set_ylim((0,1.1))
    
    #South Std
    ax[1][1].bar(np.arange(4), pStd(st) , 0.25, color='b')
    ax[1][1].set_xlabel('Standard Basis')
    ax[1][1].set_ylabel('Probability')
    ax[1][1].set_yticks([0,.25,.5,.75,1])    
    ax[1][1].set_title('Standard Measurement')
    ax[1][1].set_xticks(np.arange(4))
    ax[1][1].set_xticklabels(('00', '01', '10', '11'))
    ax[1][1].set_ylim((0,1.1))
    
    
    fig.tight_layout()
    if tofile :
        plt.savefig(name)
    plt.show()