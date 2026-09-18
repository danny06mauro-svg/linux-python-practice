import numpy as np
import matplotlib.pyplot as plt
thermal_power = np.linspace(1000, 4000, 7)
efficiency = 0.33
electrical_power = thermal_power * efficiency

print(electrical_power)
plt.xlabel("Thermal Power (MW)")

plt.ylabel("Electrical Power (MW)")
plt.plot(thermal_power, electrical_power, marker="o")
