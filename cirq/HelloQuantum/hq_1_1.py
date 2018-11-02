# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 10/24/2018

Implementation of Hello Quantum Level 1, Puzzle 1 and it's solution.
This script also demonstrates a few different ways of simulating and
analyzing the circuit
"""

import cirq as cq;

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

## initialize starting state to |10>
circuit.append(cq.X(qubits[0]))

# solution to puzzle 1-1
circuit.append(cq.X(qubits[0]))

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

