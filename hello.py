print("Hello, world!")

name = "Danny"
age = 20

print("Name:", name)
print("Age:", age)

reactor_power = float(input("Enter the reactor thermal power in MW: "))
efficiency = 0.33
electrical_power = reactor_power * efficiency
	
if electrical_power > 3000:
    print("WARNING: Electrical power exceeds 3000 MW")

print("Electrical power:", electrical_power, "MW")
