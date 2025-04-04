# htf_energy_dynamics.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Golden Ratio
phi = (1 + np.sqrt(5)) / 2

# Energy evolution function
def htf_energy(t, psi, nu, lam, eps):
    return -nu * psi - lam * psi**3 + eps * np.cos(phi * t)

# Solve ODE
t_span = [0, 20]
t_eval = np.linspace(*t_span, 500)
initial = [0.1]  # Initial energy state
sol = solve_ivp(htf_energy, t_span, initial, args=(0.1, 1.0, 0.618), t_eval=t_eval)

# Plot
plt.plot(sol.t, sol.y[0], 'r')
plt.title("HTF Energy Dynamics (ϕ-Resonance)")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.grid(True)
plt.tight_layout()
plt.show()
