import numpy as np
import matplotlib.pyplot as plt
def electrical_output(thermal_power, efficiency):
	return thermal_power * efficiency
thermal_power = np.linspace(1000, 4000, 7)
efficiency = 0.33
electrical_power = electrical_output(thermal_power, efficiency)
electrical_power_40 = electrical_output(thermal_power, 0.40)
print(electrical_power)
print(electrical_output(3000, 0.4))

plt.plot(thermal_power, electrical_power, marker="o", label="33% efficiency")
plt.plot(thermal_power, electrical_power_40, marker="o", label="40% efficiency")
plt.xlabel("Thermal Power (MW)")
plt.ylabel("Electrical Power (MW)")
plt.legend()
plt.savefig("reactor_power.png")
