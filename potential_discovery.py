'''
I'm writing this script to visualize how Electric Potential (V) 
drops as we move away from a point charge. 

This is my first step toward understanding the Poisson Equation 
practically for my GSoC project.
'''

import numpy as np

# Let's define the potential function
def get_v(q, r):
    k = 8.99e9 # Coulomb constant
    return k * q / r

# Physics constants
proton_charge = 1.602e-19 

# Let's create a range of distances (from 1 to 10 Angstroms)
# I used NumPy to make a simple list of 10 points
distances = np.linspace(1e-10, 1e-9, 10) 

print("--- Potential Study ---")
print("Distance (A) | Voltage (V)")

for r in distances:
    v = get_v(proton_charge, r)
    # Converting meters to Angstroms for easy reading
    r_angstrom = r * 1e10
    print(f"{r_angstrom:.1f} A        | {v:.4f} V")

print("\nAs distance increases, the potential drops – exactly what I expected!")
