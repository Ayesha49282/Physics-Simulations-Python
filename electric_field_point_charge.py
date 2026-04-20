'''
This script calculates the Electric Field (E) at a distance r 
from a point charge.
Formula: E = k * q / r^2
Understanding the field distribution is a key step toward 
solving the Poisson equation in physical systems.
'''

import numpy as np

def calculate_electric_field(q, r):
    """
    Calculates the magnitude of the electric field.
    q : Charge in Coulombs
    r : Distance in meters (can be a numpy array)
    """
    k = 8.987e9  # Coulomb's constant
    
    # Formula: E = k * q / r^2
    # Using np.where to handle potential division by zero
    e_field = k * q / np.where(r == 0, np.nan, r**2)
    return e_field

# --- Simulation for a Proton ---
q_proton = 1.602e-19 
r_values = np.linspace(1e-10, 5e-10, 5) # Distances in meters

fields = calculate_electric_field(q_proton, r_values)

print("Distance (m) | Electric Field (N/C)")
print("-" * 35)
for r, e in zip(r_values, fields):
    print(f"{r:.1e}     | {e:.2e}")
