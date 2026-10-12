import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

atoms_initial = 100
half_life = 10.0
dt = 1.0
duration = 50.0
rng = np.random.default_rng(7)
decay_constant = np.log(2) / half_life

decay_probability = 1 - np.exp(-decay_constant * dt)

print(f"Probability of decay in one step: {decay_probability:.2%}")
time = np.arange(0, duration + dt, dt)

atoms = np.zeros(len(time), dtype=int)
atoms[0] = atoms_initial

for i in range(len(time) - 1):
    decayed = rng.binomial(atoms[i], decay_probability)
    atoms[i + 1] = atoms[i] - decayed

print("Atoms remaining after 50 days:", atoms[-1])
print("Atoms that decayed:", decayed)
print("Atoms remaining after 50 days:", atoms[-1])
expected_atoms = atoms_initial * np.exp(-decay_constant * time)

plt.plot(time, expected_atoms, label="Analytical expectation")
plt.step(time, atoms, where="post", label="Monte Carlo")
plt.xlabel("Time (days)")
plt.ylabel("Atoms remaining")
plt.legend()
plt.tight_layout()
plt.savefig("monte_carlo_decay.png")
plt.close()
