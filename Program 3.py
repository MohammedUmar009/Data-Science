import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv("customer.csv")

# -----------------------------------
# i. Create Age Group Feature
# -----------------------------------
def age_group(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(age_group)

# -----------------------------------
# ii. One-Hot Encoding
# -----------------------------------
df = pd.get_dummies(df, columns=["Gender", "City", "Age_Group"])

# -----------------------------------
# iii. Min-Max Normalization
# -----------------------------------
scaler = MinMaxScaler()

numerical_columns = ["Age", "Income"]

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# -----------------------------------
# iv. Save the Transformed Data
# -----------------------------------
df.to_csv("customer_transformed.csv", index=False)

print("Transformation Completed Successfully!")
print("\nTransformed Dataset:")
print(df.head())