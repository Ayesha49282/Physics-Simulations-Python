'''
A simple script to calculate the electrostatic force between two 
point charges using Coulomb's Law. 
Fundamental for understanding charge interactions in Poisson's equation.
'''

def calculate_coulomb_force(q1, q2, r):
    # k is Coulomb's constant (approx. 8.99 * 10^9 N m^2/C^2)
    k = 8.987e9
    
    # Formula: F = k * |q1 * q2| / r^2
    force = k * abs(q1 * q2) / (r**2)
    return force

# Example: Force between two electrons separated by 1 Angstrom
q_electron = -1.602e-19 
distance = 1e-10 

f = calculate_coulomb_force(q_electron, q_electron, distance)

print(f"The electrostatic repulsion force is: {f:.2e} Newtons")
