import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("students.csv")

# -------------------------------
# i. Histogram of Numerical Features
# -------------------------------
plt.figure(figsize=(8,5))
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Numerical Features")
plt.show()

# -------------------------------
# ii. Box Plot to Detect Outliers
# -------------------------------
plt.figure(figsize=(8,5))
sns.boxplot(data=df.select_dtypes(include='number'))
plt.title("Box Plot of Numerical Features")
plt.show()