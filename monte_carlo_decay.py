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

def simulate_decay(time, initial_atoms, decay_probability, rng):
    atoms = np.zeros(len(time), dtype=int)
    atoms[0] = initial_atoms

    for i in range(len(time) - 1):
        decayed = rng.binomial(atoms[i], decay_probability)
        atoms[i + 1] = atoms[i] - decayed

    return atoms

atoms = simulate_decay(time, atoms_initial, decay_probability, rng)
print("Atoms remaining after 50 days:", atoms[-1])
print("Total atoms that decayed:", atoms_initial - atoms[-1])
number_runs = 1000
all_runs = []

for run in range(number_runs):
    result = simulate_decay(time, atoms_initial, decay_probability, rng)
    all_runs.append(result)

mean_atoms = np.mean(all_runs, axis=0)
print("Average final population:", mean_atoms[-1])
expected_atoms = atoms_initial * np.exp(-decay_constant * time)

plt.plot(time, expected_atoms, label="Analytical expectation")
plt.step(time, atoms, where="post", label="Monte Carlo")
plt.xlabel("Time (days)")
plt.ylabel("Atoms remaining")
plt.plot(time, mean_atoms, "--", label="Mean of 1,000 runs")
plt.legend()
plt.tight_layout()
plt.savefig("monte_carlo_decay.png")
plt.close()
