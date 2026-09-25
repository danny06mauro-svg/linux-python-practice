import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python analyze_results.py <threshold>")
    sys.exit()

threshold = float(sys.argv[1])

threshold = float(sys.argv[1])

with open("reactor_results.csv", "r") as file:
	reader = csv.DictReader(file)

	for row in reader:
		thermal = float(row["thermal_MW"])
		output_33 = float(row["electrical_33_MW"])
		output_40 = float(row["electrical_40_MW"])
		if output_40 > threshold:
			print(thermal, output_33, output_40)
