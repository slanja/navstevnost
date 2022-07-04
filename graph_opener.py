import matplotlib.pyplot as plt
import csv
from time import sleep


raw_current_time = []
current_time = []

visitors = []

raw_water_temperature = []
water_temperature = []

raw_temperature = []
temperature = []

file = input("Zadej název souboru: ")
csv_file = "{}.csv".format(file)
  
with open(csv_file,"r") as csvfile:
	lines = csv.reader(csvfile, delimiter=",")

	for row in lines:
		raw_current_time.append(row[0])
		visitors.append(int(row[1]))
		raw_water_temperature.append(row[2])
		raw_temperature.append(row[3])

# Oříznutí času od datumu
for item in raw_current_time:
	sliced_item = item[-6:]
	current_time.append(sliced_item)

# Převedení listu teploty vody na int
for item in raw_water_temperature:
	sliced_item = item[0:-2]
	water_temperature.append(int(sliced_item))

# Převedení listu teploty na int
for item in raw_temperature:
	sliced_item = item[0:-3]
	temperature.append(int(sliced_item))

fig, axs = plt.subplots(2, sharex=True)

axs[1].plot(current_time, water_temperature, color = "r", linestyle = "solid", label = "teplota vody")
axs[1].plot(current_time, temperature, color = "g", linestyle = "solid", label = "teplota")
axs[0].plot(current_time, visitors, color = "b", linestyle = "solid", label = "návštěvníci")

axs[0].grid(color="gray", linestyle="-", linewidth=0.2)
axs[1].grid(color="gray", linestyle="-", linewidth=0.2)

fig.suptitle('Návštěvnost plovárny')

fig.legend()

plt.show()
