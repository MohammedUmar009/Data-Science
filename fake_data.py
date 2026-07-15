from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

students = []

for i in range(1, 51):
    students.append({
        "Roll No": f"CS{i:03}",
        "Name": fake.name(),
        "Gender": random.choice(["Male", "Female"]),
        "Age": random.randint(18, 23),
        "Department": "Computer Science",
        "Semester": random.randint(1, 8),

        "Subject1": random.randint(35, 100),
        "Subject2": random.randint(35, 100),
        "Subject3": random.randint(35, 100),
        "Subject4": random.randint(35, 100),
        "Subject5": random.randint(35, 100),

        "Attendance (%)": random.randint(60, 100)
    })

df = pd.DataFrame(students)

# Calculate Total
df["Total"] = (
    df["Subject1"] +
    df["Subject2"] +
    df["Subject3"] +
    df["Subject4"] +
    df["Subject5"]
)

# Calculate Average
df["Average"] = (df["Total"] / 5).round(2)

# Grade
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Result (Pass only if every subject >= 35)
subjects = ["Subject1", "Subject2", "Subject3", "Subject4", "Subject5"]
df["Result"] = df[subjects].apply(
    lambda x: "Pass" if all(mark >= 35 for mark in x) else "Fail",
    axis=1
)

# Save as CSV
df.to_csv("excel.csv", index=False)

print("excel.csv created successfully!")