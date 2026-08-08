import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# --- 1. Constants & Initial Conditions ---
G = 6.67430e-11        # Gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30       # Mass of the Sun (kg)

# Initial position of Earth (approx. 1 AU from Sun on X-axis)
x0 = 1.496e11          # meters
y0 = 0.0               # meters

# Initial velocity of Earth (approx. 29.78 km/s along Y-axis)
vx0 = 0.0              # m/s
vy0 = 29780.0          # m/s

# Time span for simulation (1 Earth year in seconds)
one_year = 365.25 * 24 * 3600
t_span = (0, one_year)
t_eval = np.linspace(0, one_year, 500)

# State vector: [x, y, vx, vy]
initial_state = [x0, y0, vx0, vy0]

# --- 2. Differential Equations (Newton's Law of Gravitation) ---
def gravitational_equations(t, state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    
    # Acceleration components: a = - (G * M / r^2) * (position / r)
    ax = -G * M_sun * x / r**3
    ay = -G * M_sun * y / r**3
    
    return [vx, vy, ax, ay]

# --- 3. Solve the ODE ---
solution = solve_ivp(
    gravitational_equations, 
    t_span, 
    initial_state, 
    t_eval=t_eval, 
    method='RK45'
)

# Extract trajectory
x_orbit = solution.y[0] / 1e11  # Scaled for plotting
y_orbit = solution.y[1] / 1e11

# --- 4. Plotting & Animation ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect('equal')
ax.set_title("Planetary Orbit Simulation (Kepler & Newton)")
ax.set_xlabel("X Position ($10^{11}$ m)")
ax.set_ylabel("Y Position ($10^{11}$ m)")
ax.grid(True, linestyle='--', alpha=0.6)

# Plot Sun at origin
ax.plot(0, 0, 'yo', markersize=12, label='Sun')

# Plot elements for orbit trajectory and planet
orbit_line, = ax.plot([], [], 'b--', alpha=0.5, label='Orbit Path')
planet, = ax.plot([], [], 'ro', markersize=8, label='Planet')

def update(frame):
    orbit_line.set_data(x_orbit[:frame], y_orbit[:frame])
    planet.set_data([x_orbit[frame]], [y_orbit[frame]])
    return orbit_line, planet

anim = FuncAnimation(fig, update, frames=len(t_eval), interval=30, blit=True)

ax.legend(loc="upper right")
plt.show()
