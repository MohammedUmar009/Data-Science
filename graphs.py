import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("excel.csv")

# Calculate Percentage
df["Percentage"] = (df["Total"] / 500) * 100

# Percentage Ranges
bins = [0, 60, 70, 80, 90, 95, 100]
labels = [
    "Below 60%",
    "60-69%",
    "70-79%",
    "80-89%",
    "90-94%",
    "95-100%"
]

df["Percentage Range"] = pd.cut(
    df["Percentage"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Count students in each range
counts = df["Percentage Range"].value_counts().sort_index()

print(counts)

# Plot Graph
plt.figure(figsize=(10,6))
plt.bar(counts.index, counts.values)

plt.title("Student Percentage Distribution")
plt.xlabel("Percentage Range")
plt.ylabel("Number of Students")

# Display count above each bar
for i, value in enumerate(counts.values):
    plt.text(i, value + 0.2, str(value), ha='center', fontsize=11)

plt.show()