# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 11/12/2018

A demonstration of a few instances of Deutsch-Jozsa.  The resultant
measurement is all 0 if the function is constant and not all 0 when it
is balanced.
"""
# pylint: disable=C0103

import cirq as cq


#%%

def make_dj_circuit(length, unitary_f):
    """ Given an iterable/generator of the circuit for the unitary operator
    (unitary_f) of the boolean function f which operators on length bits,
    construct and return the complete circuit for the Deutsch-Jozsa
    algorithm """
    # initialize the work space to H|1>
    yield cq.X(cq.LineQubit(length))
    yield cq.H(cq.LineQubit(length))

    # H on 'input' space
    for i in range(length):
        yield cq.H(cq.LineQubit(i))
    # Apply U_f
    yield unitary_f
    # H on 'input space
    for i in range(length):
        yield cq.H(cq.LineQubit(i))

    # measure input space: all 0 = constant , !(all 0) = balanced
    for i in range(length):
        yield cq.MeasurementGate(key="q" + str(length-i))(cq.LineQubit(i))

#%%


# apply U_f: Here f is the balanced function f(x1_x_0) = x_1 = x_0.
uf_bal = [cq.CCX(cq.LineQubit(0), cq.LineQubit(1), cq.LineQubit(2))]
uf_bal.extend([cq.X(cq.LineQubit(i)) for i in range(2)])
uf_bal.append(cq.CCX(cq.LineQubit(0), cq.LineQubit(1), cq.LineQubit(2)))
uf_bal.extend([cq.X(cq.LineQubit(i)) for i in range(2)])

circuit_bal = cq.Circuit()
circuit_bal.append(make_dj_circuit(2, uf_bal))



print(circuit_bal)

#%%

# "Run" the computation 20 times.
sim = cq.google.XmonSimulator()
result = sim.run(circuit_bal, repetitions=20)

# view results..  should  be !(all zeros) because f is balanced
print(result)

#%%

circuit_con = cq.Circuit()
circuit_con.append(make_dj_circuit(2, [cq.X(cq.LineQubit(2))]),
                   strategy=cq.InsertStrategy.NEW_THEN_INLINE)

print(circuit_con)

#%%

result = sim.run(circuit_con, repetitions=20)
print(result)


#%%

# let f(x) = (x_5 == 1) (balanced 8-bit function)

uf = [cq.CNOT(cq.LineQubit(3), cq.LineQubit(8))]
cir = cq.Circuit()
cir.append(make_dj_circuit(8, uf))
print(cir)

sim = cq.google.XmonSimulator()
result = sim.run(cir, repetitions=20)
# view results..  should  be !(all zeros) because f is balanced
print(result)
