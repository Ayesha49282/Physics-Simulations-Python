import numpy as np
from scipy.integrate import simpson  # changed from simps to simpson

def calculate_total_charge(rho, x):
    # Using Simpson's rule for numerical integration
    total_charge = simpson(rho, x=x)
    return total_charge

# 1D grid setup
x = np.linspace(-5, 5, 100)
# Example: Gaussian charge distribution
rho = np.exp(-x**2) 

total_q = calculate_total_charge(rho, x)
print(f"Total Integrated Charge: {total_q:.4f}")
