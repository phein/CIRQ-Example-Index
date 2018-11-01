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

def p_bars_std(state):
    """
    Display the probability of measuring each of the four standard basis
    outcomes.
    """

    ax = plt.subplots()[1]
    ax.bar(np.arange(4), p_std(state), 0.25, color='b')
    ax.set_xlabel('Standard Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring the Standard Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('00', '01', '10', '11'))
    ax.set_ylim((0, 1.1))

    plt.show()

def p_bars_bell(state):
    """
    Display the probability of measuring each of the four Bell basis
    outcomes.
    """

    ax = plt.subplots()[1]
    ax.bar(np.arange(4), p_bell(state), 0.25, color='b')
    ax.set_xlabel('Bell Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring the Bell Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('++', '+-', '-+', '--'))
    ax.set_ylim((0, 1.1))

    plt.show()

def p_bars_sb(state):
    """
    Display the probability of measuring each of the four std/bell
    hybrid basis
    """

    ax = plt.subplots()[1]
    ax.bar(np.arange(4), p_sb(state), 0.25, color='b')
    ax.set_xlabel('Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring the Std/Bell Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('0+', '0-', '1+', '1-'))
    ax.set_ylim((0, 1.1))

    plt.show()

def p_bars_bs(state):
    """
    Display the probability of measuring each of the four std/bell
    hybrid basis
    """

    ax = plt.subplots()[1]
    ax.bar(np.arange(4), p_bs(state), 0.25, color='b')
    ax.set_xlabel('Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring the Bell/Std Basis')
    ax.set_xticks(np.arange(4))
    ax.set_xticklabels(('+0', '+1', '-0', '-1'))
    ax.set_ylim((0, 1.1))

    plt.show()

#%%

def p_bars_std_all(sim):
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each standard basis at each step.
    """

    states = np.vstack([s.state() for s in sim])
    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width


    for i, state in enumerate(states):
        ax.bar(index+(i*bar_width), p_std(state), bar_width,
               label="step " + str(i+1))

    ax.set_xlabel('Standard Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring the Standard Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('00', '01', '10', '11'))
    ax.set_ylim((0, 1.1))
    ax.legend()

    fig.tight_layout()
    plt.show()

def p_bars_bell_all(sim):
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each standard basis at each step.
    """

    states = np.vstack([s.state() for s in sim])


    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width

    for i, state in enumerate(states):
        ax.bar(index+(i*bar_width), p_bell(state), bar_width,
               label="step " + str(i+1))

    ax.set_xlabel('Bell Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring the Bell Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('++', '+-', '-+', '--'))
    ax.set_ylim((0, 1.1))
    ax.legend()

    fig.tight_layout()
    plt.show()

def p_bars_sb_all(sim):
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each ... std/bell hybrid basis
    """

    states = np.vstack([s.state() for s in sim])

    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width

    for i, state in enumerate(states):
        ax.bar(index+(i*bar_width), p_sb(state), bar_width,
               label="step " + str(i+1))

    ax.set_xlabel('Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring in a Std/Bell Hybrid Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('0+', '0-', '1+', '1-'))
    ax.set_ylim((0, 1.1))
    ax.legend()

    fig.tight_layout()
    plt.show()

def p_bars_bs_all(sim):
    """
    Take a moment step simulation generator and produce a graph showing
    the probability of each ... bell/std hybrid basis
    """

    states = np.vstack([s.state()for s in sim])

    fig, ax = plt.subplots()
    bar_width = .25
    index = np.arange(4)*(len(states)+1)*bar_width

    for i, state in enumerate(states):
        ax.bar(index+(i*bar_width), p_bs(state), bar_width,
               label="step " + str(i+1))

    ax.set_xlabel('Basis')
    ax.set_ylabel('Probability')
    ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_title('Probability of Measuring in a Bell/Std Hybrid Basis')
    ax.set_xticks(index+(len(states)*bar_width)/2)
    ax.set_xticklabels(('+0', '+1', '-0', '-1'))
    ax.set_ylim((0, 1.1))
    ax.legend()

    fig.tight_layout()
    plt.show()

#%%

def hq_grid(state, tofile=False, name=""):
    """
    Plot probability distributions for the two qubit measurment outcomes
    Grid for Hello Quantum
    """

    fig, ax = plt.subplots(2, 2)

     #North Bell
    ax[0][0].bar(np.arange(4), p_bell(state), 0.25, color='b')
    ax[0][0].set_xlabel('Bell Basis')
    ax[0][0].set_ylabel('Probability')
    ax[0][0].set_yticks([0, .25, .5, .75, 1])
    ax[0][0].set_title('Bell Measurement')
    ax[0][0].set_xticks(np.arange(4))
    ax[0][0].set_xticklabels(('++', '+-', '-+', '--'))
    ax[0][0].set_ylim((0, 1.1))

    #West BS
    ax[1][0].bar(np.arange(4), p_bs(state), 0.25, color='b')
    ax[1][0].set_xlabel('Basis')
    ax[1][0].set_ylabel('Probability')
    ax[1][0].set_yticks([0, .25, .5, .75, 1])
    ax[1][0].set_title('Bell/Std Measurement')
    ax[1][0].set_xticks(np.arange(4))
    ax[1][0].set_xticklabels(('+0', '+1', '-0', '-1'))
    ax[1][0].set_ylim((0, 1.1))

    #East SB
    ax[0][1].bar(np.arange(4), p_sb(state), 0.25, color='b')
    ax[0][1].set_xlabel('Basis')
    ax[0][1].set_ylabel('Probability')
    ax[0][1].set_yticks([0, .25, .5, .75, 1])
    ax[0][1].set_title('Std/Bell Measurement')
    ax[0][1].set_xticks(np.arange(4))
    ax[0][1].set_xticklabels(('0+', '0-', '1+', '1-'))
    ax[0][1].set_ylim((0, 1.1))

    #South Std
    ax[1][1].bar(np.arange(4), p_std(state), 0.25, color='b')
    ax[1][1].set_xlabel('Standard Basis')
    ax[1][1].set_ylabel('Probability')
    ax[1][1].set_yticks([0, .25, .5, .75, 1])
    ax[1][1].set_title('Standard Measurement')
    ax[1][1].set_xticks(np.arange(4))
    ax[1][1].set_xticklabels(('00', '01', '10', '11'))
    ax[1][1].set_ylim((0, 1.1))

    fig.tight_layout()
    if tofile:
        plt.savefig(name)
    plt.show()
