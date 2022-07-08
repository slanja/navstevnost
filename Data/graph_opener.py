import matplotlib.pyplot as plt
import csv
from time import sleep

# pripravené prázdné listi na zapsání dat z csv souborů
raw_current_time = []
current_time = []

visitors = []

raw_water_temperature = []
water_temperature = []

raw_temperature = []
temperature = []

# možnost vybrat vlastní název souboru, není specifické pro jeden
file = input("Zadej název souboru: ")
csv_file = "{}.csv".format(file)
  
# otevření souboru podle návzu, který se napsal nahoře a
# následné zapsání do listů
with open(csv_file,"r") as csvfile:
	lines = csv.reader(csvfile, delimiter=",")

	for row in lines:
		raw_current_time.append(row[0])
		visitors.append(int(row[1]))
		raw_water_temperature.append(row[2])
		raw_temperature.append(row[3])

# oříznutí času od datumu
for item in raw_current_time:
	sliced_item = item[-6:]
	current_time.append(sliced_item)

# useknutí a převedení listu teploty vody na int
for item in raw_water_temperature:
	sliced_item = item[0:-2]
	water_temperature.append(int(sliced_item))

# useknutí a převedení listu teploty na int
for item in raw_temperature:
	sliced_item = item[0:-3]
	temperature.append(int(sliced_item))

fig, axs = plt.subplots(2, sharex=True)

# nastavení barvy, tvaru a názvu os
axs[1].plot(current_time, water_temperature, color = "r", linestyle = "solid", label = "teplota vody")
axs[1].plot(current_time, temperature, color = "g", linestyle = "solid", label = "teplota vzduchu")
axs[0].plot(current_time, visitors, color = "b", linestyle = "solid", label = "návštěvníci")

# nastavení velikosti a barvy gridu
axs[0].grid(color="gray", linestyle="-", linewidth=0.2)
axs[1].grid(color="gray", linestyle="-", linewidth=0.2)

# název grafu
fig.suptitle('Návštěvnost plovárny')

fig.legend()

plt.show()
