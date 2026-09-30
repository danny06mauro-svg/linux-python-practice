import numpy as np
import matplotlib.pyplot as plt

# Foward Euler method
def forward_euler(time, initial_value, decay_constant):
    result = np.zeros_like(time)
    result[0] = initial_value
    dt = time[1] - time[0]

    for i in range(len(time) - 1):
        result[i + 1] = (result[i] + dt * (-decay_constant * result[i]))

    return result

# Improved Euler method
def improved_euler(time, initial_value, decay_constant):
    result = np.zeros_like(time)
    result[0] = initial_value
    dt = time[1] - time[0]

    for i in range(len(time) - 1):
        k1 = (-decay_constant * result[i])

        predicted = result[i] + (dt * k1)

        k2 = (-decay_constant * predicted)

        result[i + 1] = result[i] + ((0.5 * dt) * (k1+k2))

    return result

# Initial values
atoms_initial = 1_000_000
half_life = 8.02
decay_constant = np.log(2) / half_life

# Main and Euler solutions
time = np.linspace(0, 40, 200)

atoms = atoms_initial * np.exp(-decay_constant * time)
atoms_euler = forward_euler(time,atoms_initial,decay_constant)
atoms_improved_euler = improved_euler(time, atoms_initial, decay_constant)
# Convergence
point_counts = [10, 20, 50, 100, 200]
time_steps = []
forward_errors = []
improved_errors = []

for points in point_counts:
    test_time = np.linspace(0, 40, points)

    test_euler = forward_euler(test_time, atoms_initial, decay_constant)

    improved_test_euler = improved_euler(test_time, atoms_initial, decay_constant)

    exact_final = (atoms_initial * np.exp(-decay_constant * test_time[-1]))

    forward_error = (abs(test_euler[-1] - exact_final) / exact_final * 100)


    improved_error = (abs(improved_test_euler[-1] - exact_final) / exact_final * 100)

    time_steps.append(test_time[1] - test_time[0])
    forward_errors.append(forward_error)
    improved_errors.append(improved_error)

print(f"{points} points: "f"Forward = {forward_error:.4f}%, "f"Improved = {improved_error:.4f}%")
# Calculate convergence order after collecting all results
forward_order = np.polyfit(np.log(time_steps),np.log(forward_errors), 1)[0]
improved_order = np.polyfit(np.log(time_steps), np.log(improved_errors), 1)[0]
print(f"Forward Euler order: {forward_order:.3f}")
print(f"Improved Euler order: {improved_order:.3f}")
print(f"Decay constant: {decay_constant:.5f} per day")

# Decay plot(s)
plt.figure()
plt.plot(time, atoms, label="Analytical")
plt.plot(time, atoms_euler, "--", label="Euler")
plt.plot(time, atoms_improved_euler, ":", label="Improved Euler")
plt.xlabel("Time (days)")
plt.ylabel("Number of atoms")
plt.title("I-131 Radioactive Decay")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("decay_curve.png")
plt.close()

# Convergence plot(s)
plt.figure()
plt.loglog(time_steps, forward_errors, marker="o", label="Forward Euler")
plt.loglog(time_steps, improved_errors, marker="s", label="Improved Euler")
plt.legend()
plt.xlabel("Time-step size (days)")
plt.ylabel("Final percent error")
plt.title("Euler Method Convergence Comparison")
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("euler_convergence.png")
plt.close()
