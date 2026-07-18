import pandas as pd
import numpy as np

# Number of telemetry records
rows = 1000

# Make results repeatable
np.random.seed(42)

# Generate spacecraft telemetry
data = {
    "Battery_Voltage": np.random.uniform(22, 30, rows),
    "Battery_Current": np.random.uniform(1, 8, rows),
    "Temperature": np.random.uniform(15, 80, rows),
    "CPU_Load": np.random.uniform(10, 100, rows),
    "Signal_Strength": np.random.uniform(40, 100, rows),
    "Fuel_Level": np.random.uniform(20, 100, rows)
}

df = pd.DataFrame(data)

# Create Health Status
health = []

for _, row in df.iterrows():
    if (
        row["Temperature"] > 65
        or row["Battery_Voltage"] < 23
        or row["Signal_Strength"] < 50
    ):
        health.append("Critical")
    elif (
        row["Temperature"] > 50
        or row["CPU_Load"] > 80
    ):
        health.append("Warning")
    else:
        health.append("Healthy")

df["Health"] = health

# Save dataset
df.to_csv("telemetry.csv", index=False)

print("✅ Dataset created successfully!")
print(df.head())