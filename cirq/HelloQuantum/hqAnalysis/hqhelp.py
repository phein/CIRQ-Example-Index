    # -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 10/24/2018

Some useful functions for analyzing Hello Quantum Puzzles
"""

import numpy as np
import matplotlib.pyplot as plt

#%%

def to_bell(state):
    """
    Convert standard basis state to bell basis state
    """

    h_gate = np.array([[1, 1], [1, -1]])
    b_change = (0.5)*np.kron(h_gate, h_gate)

    return b_change.dot(state)

def to_sb(state):
    """
    Convert standard basis state to Std/Bell basis
    """

    h_gate = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]])
    b_change = np.kron(np.eye(2), h_gate)

    return b_change.dot(state)

def to_bs(state):
    """
    Convert standard basis state to Bell/Std basis
    """

    h_gate = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]])
    b_change = np.kron(h_gate, np.eye(2))

    return b_change.dot(state)

#%%

def density_matrix(state):
    """
    Given a quantum state compute it's density matrix w.r.t. the current basis
    for the state.
    """

    return np.outer(state, np.conj(state))

def trace_upper(d_op):
    """
    Trace out the upper bit, leaving the density operator for the lower
    order bit
    """

    return np.array([[d_op[0, 0]+d_op[2, 2], d_op[0, 1]+d_op[2, 3]],
                     [d_op[1, 0]+d_op[3, 2], d_op[1, 1]+d_op[3, 3]]])

def trace_lower(d_op):
    """
    Trace out the lower bit, leaving the density operator for the high
    order bit
    """

    return np.array([[d_op[0, 0]+d_op[1, 1], d_op[0, 2]+d_op[1, 3]],
                     [d_op[2, 0]+d_op[3, 1], d_op[2, 2]+d_op[3, 3]]])

#%%

def p_std_lower(state):
    """
    Compute measurement probabilities for the lower bit of the system w.r.t
    the standard basis
    """

    d_op = trace_upper(density_matrix(state))
    return np.real(np.array([d_op[0, 0], d_op[1, 1]]))

def p_std_upper(state):
    """
    Compute measurement probabilities for the lower bit of the system w.r.t
    the standard basis
    """

    d_op = trace_lower(density_matrix(state))
    return np.real(np.array([d_op[0, 0], d_op[1, 1]]))

def p_bell_lower(state):
    """
    Compute measurement probabilities for the lower bit of the system w.r.t
    the bell basis
    """
    h_gate = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]]);
    d_op_std = trace_upper(density_matrix(state))
    d_op = np.matmul(np.matmul(h_gate, d_op_std), h_gate)

    return np.real(np.array([d_op[0, 0], d_op[1, 1]]))

def p_bell_upper(state):
    """
    Compute measurement probabilities for the lower bit of the system w.r.t
    the bell basis
    """
    h_gate = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]]);
    d_op_std = trace_lower(density_matrix(state))
    d_op = np.matmul(np.matmul(h_gate, d_op_std), h_gate)

    return np.real(np.array([d_op[0, 0], d_op[1, 1]]))

#%%

def p_std(state):
    """
    Compute the measurement probabilities for a std/std measurement.
    This gets at the southern circle of the center 4.
    """

    return abs(state)**2

def p_bell(state):
    """
    Compute the measurement probabilities for a bell/bell measurement.
    This gets at the northern circle of the center 4.
    """

    return abs(to_bell(state))**2

def p_sb(state):
    """
    Compute the measurement probabilities for a std/bell measurement.
    This gets at the eastern circle of the center 4.
    """

    return abs(to_sb(state))**2

def p_bs(state):
    """
    Compute the measurement probabilities for a bell/std measurement.
    This gets at the northern circle of the center 4.
    """

    return abs(to_bs(state))**2

#%%

def hq_grid(state, to_file=False, name=""):
    """
    Plot probability distributions for the two qubit measurment outcomes
    Grid for Hello Quantum
    """

    fig, ax = plt.subplots(2, 4, sharey=True, figsize=(10, 5))
    plt.subplots_adjust(right=1, left=.25)

    #Upper Bell
    ax[0][0].bar(np.arange(2), p_bell_upper(state), 0.25, color='b')    
    ax[0][0].set_yticks([0, .25, .5, .75, 1])
    ax[0][0].set_title('High Bit')
    ax[0][0].set_xticks(np.arange(2))
    ax[0][0].set_xticklabels(('+', '-'))
    ax[0][0].set_ylim((0, 1.1))

    #Upper std
    ax[1][0].bar(np.arange(2), p_std_upper(state), 0.25, color='b')    
    ax[1][0].set_yticks([0, .25, .5, .75, 1])    
    ax[1][0].set_xticks(np.arange(2))
    ax[1][0].set_xticklabels(('0', '1'))
    ax[1][0].set_ylim((0, 1.1))

     #North Bell
    ax[0][1].bar(np.arange(4), p_bell(state), 0.25, color='b')    
    ax[0][1].set_xticks(np.arange(4))
    ax[0][1].set_xticklabels(('++', '+-', '-+', '--'))
    ax[0][1].set_ylim((0, 1.1))

    #West BS
    ax[1][1].bar(np.arange(4), p_bs(state), 0.25, color='b')    
    ax[1][1].set_xticks(np.arange(4))
    ax[1][1].set_xticklabels(('+0', '+1', '-0', '-1'))
    ax[1][1].set_ylim((0, 1.1))

    #East SB
    ax[0][2].bar(np.arange(4), p_sb(state), 0.25, color='b')
    ax[0][2].set_xticks(np.arange(4))
    ax[0][2].set_xticklabels(('0+', '0-', '1+', '1-'))
    ax[0][2].set_ylim((0, 1.1))

    #South Std
    ax[1][2].bar(np.arange(4), p_std(state), 0.25, color='b')
    ax[1][2].set_xticks(np.arange(4))
    ax[1][2].set_xticklabels(('00', '01', '10', '11'))
    ax[1][2].set_ylim((0, 1.1))
    
    #Lower Bell
    ax[0][3].bar(np.arange(2), p_bell_lower(state), 0.25, color='b')
    ax[0][3].set_title('Low Bit')
    ax[0][3].set_xticks(np.arange(2))
    ax[0][3].set_xticklabels(('+', '-'))
    ax[0][3].set_ylim((0, 1.1))

    #Lower std
    ax[1][3].bar(np.arange(2), p_std_lower(state), 0.25, color='b')
    ax[1][3].set_xticks(np.arange(2))
    ax[1][3].set_xticklabels(('0', '1'))
    ax[1][3].set_ylim((0, 1.1))

    
    fig.tight_layout()
    if to_file:
        plt.savefig(name)
    plt.show()

