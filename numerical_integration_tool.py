import math

def physics_function(x):
    # Example: A simple parabolic function representing a physical curve
    return x**2

def trapezoidal_rule(a, b, n):
    """
    Solves a definite integral using the Trapezoidal Rule.
    Essential for solving Poisson solvers in computational physics.
    """
    h = (b - a) / n
    integral = 0.5 * (physics_function(a) + physics_function(b))
    
    for i in range(1, n):
        integral += physics_function(a + i * h)
        
    return integral * h

if __name__ == "__main__":
    result = trapezoidal_rule(0, 1, 100)
    print(f"The numerical integral of x^2 from 0 to 1 is: {result:.6f}")
