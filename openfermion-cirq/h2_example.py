# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 11/14/2018

Calculation of the ground state energy of H2 using Open-Fermion and CIRQ
This is mostly just pulled from the OpenFermion, OpenFermion-CIRQ, and CIRQ papers and 
documentation.
"""
# pylint: disable=C0103


import openfermion as of
import cirq as cq
import openfermioncirq as ofcq
from openfermioncirq.optimization import COBYLA, OptimizationParams
import matplotlib.pyplot as pyplot
from openfermionpsi4 import run_psi4


#%%

class MyAnsatz(ofcq.VariationalAnsatz):
    
    def params(self):
        """The parameters of the ansatz."""
        return [cq.Symbol('theta_0')]
    
    def operations(self, qubits):
        """Produce the operations of the ansatz circuit."""
        q0, q1, q2, q3 = qubits
        yield cq.H(q0), cq.H(q1), cq.H(q2)
        yield (cq.X**0.5).on(q3)
        
        yield cq.CNOT(q0, q1), cq.CNOT(q1, q2), cq.CNOT(q2, q3)
        yield (cq.Z._with_exponent(cq.Symbol('theta_0'))).on(q3)
        yield cq.CNOT(q2, q3), cq.CNOT(q1, q2), cq.CNOT(q0, q1)
        
        yield cq.H(q0), cq.H(q1), cq.H(q2)
        yield (cq.X**0.5).on(q3)

    def _generate_qubits(self):
        """Produce qubits that can be used by the ansatz circuit."""
        return cq.LineQubit.range(4)


#%%

diatomic_bond_length = .7414
geometry = [('H', (0., 0., 0.)), 
            ('H', (0., 0., diatomic_bond_length))]
basis = 'sto-3g'
multiplicity = 1
charge = 0
description = format(diatomic_bond_length)

molecule = of.MolecularData(
    geometry,
    basis,
    multiplicity,
    description=description)
# H2 comes for free..  no psi4 needed. 
molecule.load()

hamiltonian = molecule.get_molecular_hamiltonian()
print("Bond Length in Angstroms: {}".format(diatomic_bond_length))
print("Hartree Fock (mean-field) energy in Hartrees: {}".format(molecule.hf_energy))
print("FCI (Exact) energy in Hartrees: {}".format(molecule.fci_energy))

#%%

## Transform into Qubit Hamiltonian
ansatz = MyAnsatz()
objective = ofcq.HamiltonianObjective(hamiltonian)
q0, q1, _, _ = ansatz.qubits
preparation_circuit = cq.Circuit.from_ops(
    cq.X(q0),
    cq.X(q1))
study = ofcq.VariationalStudy(
    name='my_hydrogen_study',
    ansatz=ansatz,
    objective=objective,
    preparation_circuit=preparation_circuit)
print(study.circuit)

#%% 

optimization_params = OptimizationParams(
    algorithm=COBYLA,
    initial_guess=[0.01])
result = study.optimize(optimization_params)
print("Initial state energy in Hartrees: {}".format(molecule.hf_energy))
print("Optimized energy result in Hartree: {}".format(result.optimal_value))
print("Exact energy result in Hartees for reference: {}".format(molecule.fci_energy))


#%%

## Run the same study on multiple bond lengths

bond_lengths = [float('{0:.1f}'.format(0.3 + 0.1 * x)) for x in range(23)]
hartree_fock_energies = []
optimized_energies = []
exact_energies = []

for diatomic_bond_length in bond_lengths:
    geometry = [('H', (0., 0., 0.)), 
                ('H', (0., 0., diatomic_bond_length))]

    description = format(diatomic_bond_length)

    molecule = of.MolecularData(geometry, 
                                basis,
                                multiplicity, 
                                charge,
                                description=description)
    molecule = run_psi4(molecule,
                        run_mp2=True,
                        run_cisd=True,
                        run_ccsd=True,
                        run_fci=True)
    hamiltonian = molecule.get_molecular_hamiltonian()
    
    study = ofcq.VariationalStudy(
        name='my_hydrogen_study',
        ansatz=ansatz,
        objective=ofcq.HamiltonianObjective(hamiltonian),
        preparation_circuit=preparation_circuit)
    
    result = study.optimize(optimization_params)
    hartree_fock_energies.append(molecule.hf_energy)
    optimized_energies.append(result.optimal_value)
    exact_energies.append(molecule.fci_energy)
    
    print("R={}\t Optimized Energy: {}".format(diatomic_bond_length, result.optimal_value))
    
#%%
    
# Graph that bad boy
    

# Plot the energy mean and std Dev
fig = pyplot.figure(figsize=(10,7))
bkcolor = '#ffffff'
ax = fig.add_subplot(1, 1, 1)
pyplot.subplots_adjust(left=.2)
ax.set_xlabel('R (Angstroms)')
ax.set_ylabel(r'E Hartrees')
ax.set_title(r'H$_2$ bond dissociation curve')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#bond_lengths = [float(x) for x in bond_lengths]
ax.plot(bond_lengths, hartree_fock_energies, label='Hartree-Fock')
ax.plot(bond_lengths, optimized_energies, '*', label='Optimized')
ax.plot(bond_lengths, exact_energies, '--', label='Exact')

ax.legend(frameon=False)
pyplot.show()
