# -*- coding: utf-8 -*-
"""
Author: Logan Mayfield
Date: 11/14/2018

Calculation of the ground state energy of H2 using Open-Fermion and CIRQ
This is mostly just pulled from the OpenFermion and CIRQ papers and 
documentation.
"""
# pylint: disable=C0103


import openfermion as of
from openfermionpsi4 import run_psi4



#%%

# Specify the Molecule
geometry = [['H', [0, 0, 0]],
            ['H', [0, 0, 0.74]]]
basis = 'sto-3g'
multiplicity = 1
charge = 0
h2_molecule = of.MolecularData(geometry, basis, multiplicity, charge)

#%%

# Generate the Integrals (using psi4)
h2_molecule = run_psi4(h2_molecule,
                       run_mp2=True,
                       run_cisd=True,
                       run_ccsd=True,
                       run_fci=True)
two_electron_integrals = h2_molecule.two_body_integrals
one_electron_integrals = h2_molecule.one_body_integrals
orbitals = h2_molecule.canonical_orbitals

