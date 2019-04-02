#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:34:36 2019

@author: jlmayfield
"""

#%%


import numpy as np
import pandas as pd
import openfermion as of 
from openfermionpsi4 import run_psi4
import matplotlib.pyplot as pyplot



#%%

bond_lengths = np.linspace(0.3,2.5,num=35)
multiplicity = 1
charge = 0 
basis = 'sto-3g'


#%%

cols = ['Hartree_fock','MP2','CISD','CCSD','FCI']
energies = pd.DataFrame(index=bond_lengths,columns=cols,dtype=np.float32)

for diatomic_bond_length in bond_lengths:    
    molecule = of.MolecularData([('H', (0., 0., 0.)),
                                 ('H', (0., 0., diatomic_bond_length))],
                                basis,multiplicity, charge)
    
    molecule = run_psi4(molecule,
                        run_scf=True, #scf "Self-Consistent Field" aka Hartree-Fock
                        run_mp2=True, #Møller–Plesset Perturbation Theory
                        run_cisd=True, #Configuration Interaction with Single Double Excitations
                        run_ccsd=True, # Couple-Cluster with Single Double Excitations 
                        run_fci=True) # Full Configuration Interaction --> EXACT RESULT
    
    energies.loc[diatomic_bond_length,'Hartree_fock'] = molecule.hf_energy
    energies.loc[diatomic_bond_length,'MP2'] = molecule.mp2_energy
    energies.loc[diatomic_bond_length,'CISD'] = molecule.cisd_energy
    energies.loc[diatomic_bond_length,'CCSD'] = molecule.ccsd_energy
    energies.loc[diatomic_bond_length,'FCI'] = molecule.fci_energy
    


#%%

fig = pyplot.figure(figsize=(10,7))
bkcolor = '#ffffff'
ax = fig.add_subplot(1, 1, 1)
pyplot.subplots_adjust(left=.2)
ax.set_xlabel('R (Angstroms)')
ax.set_ylabel(r'E Hartrees')
ax.set_title(r'H$_2$ bond dissociation curve')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
energies.plot(ax=ax)
ax.legend(frameon=False)
pyplot.show()






