import os
import pandas as pd
import numpy as np

# -------------------------------
# Create 'data' folder if it doesn't exist
# -------------------------------
os.makedirs("data", exist_ok=True)

# -------------------------------
# Random seed for reproducibility
# -------------------------------
np.random.seed(42)

# Number of telemetry records
rows = 10000

# -------------------------------
# Generate normal spacecraft telemetry data
# -------------------------------
data = {
    "Battery_Voltage": np.random.normal(26, 1.2, rows),
    "Battery_Current": np.random.normal(5, 1, rows),
    "Temperature": np.random.normal(28, 6, rows),
    "Solar_Power": np.random.normal(220, 35, rows),
    "Fuel_Level": np.linspace(100, 70, rows),
    "CPU_Load": np.random.normal(40, 12, rows),
    "Signal_Strength": np.random.normal(90, 5, rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Initially all spacecraft are healthy
df["Health"] = "Healthy"

# -------------------------------
# Introduce some faults
# -------------------------------
fault_indices = np.random.choice(df.index, 400, replace=False)

df.loc[fault_indices, "Temperature"] = np.random.uniform(70, 100, 400)
df.loc[fault_indices, "Battery_Voltage"] = np.random.uniform(18, 22, 400)
df.loc[fault_indices, "Signal_Strength"] = np.random.uniform(40, 65, 400)
df.loc[fault_indices, "Health"] = "Critical"

# -------------------------------
# Calculate Health Score
# -------------------------------
health_scores = []

for _, row in df.iterrows():

    score = 100

    if row["Temperature"] > 60:
        score -= 30

    if row["Battery_Voltage"] < 23:
        score -= 30

    if row["Signal_Strength"] < 70:
        score -= 20

    if row["CPU_Load"] > 80:
        score -= 10

    if row["Solar_Power"] < 120:
        score -= 10

    score = max(score, 0)

    health_scores.append(score)

df["Health_Score"] = health_scores

# -------------------------------
# Save dataset
# -------------------------------
file_path = "data/telemetry.csv"
df.to_csv(file_path, index=False)

# -------------------------------
# Display results
# -------------------------------
print("\nDataset Created Successfully!\n")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nHealth Distribution:")
print(df["Health"].value_counts())

print(f"\nDataset saved successfully at: {file_path}")