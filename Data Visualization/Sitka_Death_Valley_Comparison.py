from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


def reader(path):
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    return reader


def get_index(reader):
    for index, column_header in enumerate(reader):
        print(index, column_header)


readerStika = reader(Path("weather_data/sitka_weather_2021_full.csv"))
readerDeathValley = reader(Path("weather_data/death_valley_2021_full.csv"))

get_index(readerStika)

get_index(readerDeathValley)

StikaDates, StikaHighs = [], []
DeathValleyDates, DeathValleyHighs = [], []
for row in readerStika:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[7])
    StikaDates.append(current_date)
    StikaHighs.append(high)

for row in readerDeathValley:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[6])
    DeathValleyDates.append(current_date)
    DeathValleyHighs.append(high)
# Extract high temperatures.

# print(highs)
dates = []
highs = []
if StikaDates > DeathValleyDates:
    dates = StikaDates
else:
    dates = DeathValleyDates

# Plot the high temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(StikaDates, StikaHighs, color="red", alpha=0.5)
ax.plot(DeathValleyDates, DeathValleyHighs, color="blue", alpha=0.5)
ax.fill_between(dates, StikaHighs, DeathValleyHighs, facecolor="red", alpha=0.1)

# ax.plot(highs, color="red")
# ax.plot(dates, highs, color="red")
# ax.plot(dates, lows, color="blue")
# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel("Days", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
