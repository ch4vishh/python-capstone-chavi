# CAMPUS ENERGY DASHBOARD
# CHAVI JAISWAL
# 2501410011

import pandas as pd
import matplotlib.pyplot as plt
import os

print("WELCOME TO CAMPUS ENERGY MONITORING SYSTEM")

# =====================================================================
# OOP CLASSES
# =====================================================================

class MeterReading:
    """Stores one meter reading"""

    def __init__(self, time, units):
        self.time = time
        self.units = units

    def __repr__(self):
        return f"[{self.time} -> {self.units} kWh]"


class Building:
    """Represents a building on campus"""

    def __init__(self, name):
        self.name = name
        self.records = []

    def add(self, time, units):
        reading = MeterReading(time, units)
        self.records.append(reading)

    def total(self):
        return sum(r.units for r in self.records)

    def avg(self):
        return self.total() / len(self.records) if self.records else 0

    def mmin(self):
        return min(r.units for r in self.records) if self.records else 0

    def mmax(self):
        return max(r.units for r in self.records) if self.records else 0

    def report(self):
        text = f"\nREPORT: {self.name}\n"
        text += f" • Entries: {len(self.records)}\n"
        text += f" • Total: {self.total():.2f} kWh\n"
        text += f" • Average: {self.avg():.2f} kWh\n"
        text += f" • Min: {self.mmin():.2f} kWh\n"
        text += f" • Max: {self.mmax():.2f} kWh\n"
        return text


class CampusManager:
    """Handles all buildings"""

    def __init__(self):
        self.all = {}

    def add_building(self, name):
        if name not in self.all:
            self.all[name] = Building(name)

    def add_reading(self, name, time, units):
        self.add_building(name)
        self.all[name].add(time, units)

    def total_campus(self):
        return sum(b.total() for b in self.all.values())

    def highest(self):
        if not self.all:
            return None, 0
        top = max(self.all, key=lambda x: self.all[x].total())
        return top, self.all[top].total()


# =====================================================================
# TASK 1: LOAD CSV FILES
# =====================================================================

print("\nTASK 1: Checking data folder...")

data_folder = "data"
manager = CampusManager()
frames = []

if not os.path.exists(data_folder):
    print("⚠ 'data' folder not found. Create it and add CSV files.")
    exit()

csvs = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

if len(csvs) == 0:
    print("⚠ No CSV files found in data folder.")
    exit()

print(f"✓ Found {len(csvs)} CSV file(s)\n")

for csv in csvs:
    path = os.path.join(data_folder, csv)
    name = csv.replace(".csv", "")

    print(f"➡ Loading '{csv}' ...")

    try:
        df = pd.read_csv(path)

        if "Date" not in df or "kWh" not in df:
            print("   ⚠ Missing required columns (Date, kWh). Skipped.")
            continue

        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Building"] = name

        # Add readings
        for _, row in df.iterrows():
            if not pd.isna(row["Date"]) and not pd.isna(row["kWh"]):
                manager.add_reading(name, row["Date"], row["kWh"])

        frames.append(df)
        print(f"   ✓ Loaded {len(df)} rows from {name}")

    except Exception as e:
        print(f"   ✗ Error reading file: {e}")

# Combine all data
if frames:
    combined = pd.concat(frames, ignore_index=True)
    print("\n✓ Combined dataset size:", len(combined))
else:
    print("⚠ No valid data found.")
    exit()


# =====================================================================
# TASK 2: BASIC ANALYSIS
# =====================================================================

print("\nTASK 2: Performing analysis...")

def daily(df):
    df["Date"] = pd.to_datetime(df["Date"])
    return df.groupby(df["Date"].dt.date)["kWh"].sum().reset_index()

def weekly(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df2 = df.set_index("Date")
    return df2["kWh"].resample("W").sum().reset_index()

daily_table = daily(combined)
weekly_table = weekly(combined)

print("✓ Daily and weekly tables ready")


# =====================================================================
# TASK 4: PLOTTING DASHBOARD
# =====================================================================

print("\nTASK 4: Creating graphs...")

fig, axes = plt.subplots(3, 1, figsize=(12, 14))
fig.suptitle("Campus Energy Dashboard", fontsize=16)

# Daily Line Plot
axes[0].plot(daily_table["Date"], daily_table["kWh"], marker="o")
axes[0].set_title("Daily Energy Usage")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("kWh")

# Building Averages Bar Chart
names = list(manager.all.keys())
avg_values = [manager.all[b].avg() for b in names]
axes[1].bar(names, avg_values)
axes[1].set_title("Average Usage per Building")
axes[1].set_ylabel("kWh")

# Scatter Plot
axes[2].scatter(combined["Date"], combined["kWh"], alpha=0.6)
axes[2].set_title("Peak Load Scatter Plot")
axes[2].set_xlabel("Date")
axes[2].set_ylabel("kWh")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.close()

print("✓ Saved: dashboard.png")


# =====================================================================
# TASK 5: EXPORT FILES
# =====================================================================

print("\nTASK 5: Exporting results...")

if not os.path.exists("output"):
    os.mkdir("output")

combined.to_csv("output/cleaned_energy_data.csv", index=False)
daily_table.to_csv("output/daily_totals.csv", index=False)
weekly_table.to_csv("output/weekly_totals.csv", index=False)

summary_txt = "\n================= EXECUTIVE SUMMARY =================\n"
summary_txt += f"Total Campus Consumption: {manager.total_campus():.2f} kWh\n"

hb, hc = manager.highest()
summary_txt += f"Highest Consuming Building: {hb} ({hc:.2f} kWh)\n"

for b in manager.all.values():
    summary_txt += b.report()

summary_txt += "\n=====================================================\n"

with open("output/summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_txt)

print("✓ Saved: output/summary.txt")

print("\nAnalysis completed.")
print("All files created in the 'output' folder.")
