# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 10/24/2018

Implementation of Hello Quantum Level 1, Puzzle 1 and it's solution.
This script also demonstrates a few different ways of simulating and
analyzing the circuit
"""

import cirq as cq;
import numpy as np;
import hqAnalysis.hqhelp as hh;

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

#%% 

# simulate the run and gain access to state information

s_res = sim.simulate(circuit,qubit_order=[qubits[0],qubits[1]])

# see results 
print(s_res)
# See the final state --> [a b c d] for a00+b01+c10+d11
print(np.around(s_res.final_state,3))

## the probability of measuring a state with amplitude a is 
##  abs(a)**2

p = abs(s_res.final_state)**2
print(p)


#%%

# Step through moments and print out the state after each moment.
for i, step in enumerate(sim.simulate_moment_steps(circuit)):
    print('state at step %d: %s' % (i+1, np.around(step.state(), 3)))
    print('prob(%d) at step %d: %s' % (i+1,i+1, np.around(abs(step.state())**2,3)))
    hh.p_bars_std(np.around(step.state(), 3))
    hh.p_bars_bell(np.around(step.state(), 3))

#%%
    
hh.p_bars_std_all(sim.simulate_moment_steps(circuit))
hh.p_bars_bell_all(sim.simulate_moment_steps(circuit))



