#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 11/5/2018

Implementation of Hello Quantum Level 2, Puzzle 4 and it's solution.
This script also demonstrates a few different ways of simulating and
analyzing the circuit
"""

import cirq as cq
import numpy as np
import hqAnalysis.hqhelp as hh

#%%


# Create a 2 qubit register 
qubits = cq.LineQubit(0).range(2)

# create an empty circuit
circuit = cq.Circuit()

# construct a simulator to run the circuit 
sim = cq.google.XmonSimulator()

#%%

## The indexing of lineQubits is such that the high-order bit (top wire) is
## index 0.

## initialize starting state to |11>
circuit.append([cq.X(qubits[0]),cq.X(qubits[1])])
circuit.append(cq.H(qubits[1]))

# solution to puzzle 2-4
circuit.append([cq.H(qubits[0]),cq.H(qubits[1])])
circuit.append(cq.CZ(qubits[0], qubits[1]))
circuit.append([cq.H(qubits[0]),cq.H(qubits[1])])


# finish with standard measurement on both bits
circuit.append( [ cq.MeasurementGate(key="q" + str(1-i))(qubits[i]) for i in range(2) ])  

print(circuit)


#%%

# "Run" the computation 20 times. 
result = sim.run(circuit,repetitions=20)

# view results  
print(result)
# get histogram counts of each result
print(result.histogram(key="q0"))
print(result.histogram(key="q1"))

#%%

# trace the puzzle
print(circuit[:-2])
puz = sim.simulate_moment_steps(circuit[:-2])
## get to the initial puzzle state, look at probabilities
next(puz)
next(puz)

init = next(puz)
hh.hq_grid(init.state())

s1 = next(puz)
hh.hq_grid(s1.state())

s2 = next(puz)
hh.hq_grid(s2.state())


#%%

# step through everything but the measurement
for i, step in enumerate(sim.simulate_moment_steps(circuit[:-2])):
    print("step %d : std state %s" %
          (i+1, np.around(step.state(), 3)))
    print("step %d : bell state %s" %
          (i+1, np.around(hh.to_bell(step.state()), 3)))
    print("step %d : BS state %s" %
          (i+1, np.around(hh.to_bs(step.state()), 3)))
    print("step %d : SB state %s" %
          (i+1, np.around(hh.to_bs(step.state()), 3)))
    print("\n")