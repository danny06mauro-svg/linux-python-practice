import numpy as np
import matplotlib.pyplot as plt


def forward_euler(time, initial_value, decay_constant):
    result = np.zeros_like(time)
    result[0] = initial_value
    dt = time[1] - time[0]

    for i in range(len(time) - 1):
        result[i + 1] = (
            result[i] + dt * (-decay_constant * result[i])
        )

    return result


# Physical parameters
atoms_initial = 1_000_000
half_life = 8.02
decay_constant = np.log(2) / half_life

# Main analytical and Euler solutions
time = np.linspace(0, 40, 200)

atoms = atoms_initial * np.exp(-decay_constant * time)
atoms_euler = forward_euler(
    time,
    atoms_initial,
    decay_constant
)

# Convergence study
point_counts = [10, 20, 50, 100, 200]
time_steps = []
errors = []

for points in point_counts:
    test_time = np.linspace(0, 40, points)

    test_euler = forward_euler(
        test_time,
        atoms_initial,
        decay_constant
    )

    exact_final = (
        atoms_initial
        * np.exp(-decay_constant * test_time[-1])
    )

    percent_error = (
        abs(test_euler[-1] - exact_final)
        / exact_final
        * 100
    )

    time_steps.append(test_time[1] - test_time[0])
    errors.append(percent_error)

    print(f"{points} points: {percent_error:.4f}% error")

# Calculate convergence order after collecting all results
order = np.polyfit(
    np.log(time_steps),
    np.log(errors),
    1
)[0]

print(f"Observed convergence order: {order:.3f}")
print(f"Decay constant: {decay_constant:.5f} per day")

# Decay comparison plot
plt.figure()
plt.plot(time, atoms, label="Analytical")
plt.plot(time, atoms_euler, "--", label="Euler")
plt.xlabel("Time (days)")
plt.ylabel("Number of atoms")
plt.title("I-131 Radioactive Decay")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("decay_curve.png")
plt.close()

# Convergence plot
plt.figure()
plt.loglog(time_steps, errors, marker="o")
plt.xlabel("Time-step size (days)")
plt.ylabel("Final percent error")
plt.title("Forward Euler Convergence")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("euler_convergence.png")
plt.close()
