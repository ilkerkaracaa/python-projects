from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, rainfalls = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        rainfall = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfalls.append(rainfall)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color="blue")
ax.set_title("Daily Rainfalls, 2021", fontsize=24)
ax.set_xlabel("Days", fontsize=16)
ax.set_ylabel("Rainfall (in)", fontsize=16)
ax.tick_params(labelsize=16)
fig.autofmt_xdate()
plt.show()
