import pandas as pd
import matplotlib.pyplot as plt


# ============================================
# Pandas + Matplotlib Data Visualization
# ============================================

# Read employee data from Excel
df = pd.read_excel("Employee.xlsx")

print("Employee Data:")
print(df)

print("\n" + "=" * 50)


# ============================================
# 1. Line Chart
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    df["Name"],
    df["Age"],
    marker="*"
)

plt.title("Employee Ages by Name")
plt.xlabel("Name")
plt.ylabel("Age")

plt.xticks(rotation=50)
plt.tight_layout()
plt.show()


# ============================================
# 2. Bar Chart
# ============================================

plt.figure(figsize=(10, 5))

plt.bar(
    df["Name"],
    df["Age"]
)

plt.title("Employee Ages by Name")
plt.xlabel("Name")
plt.ylabel("Age")

plt.xticks(rotation=50)
plt.tight_layout()
plt.show()


# ============================================
# 3. Scatter Plot
# ============================================

plt.figure(figsize=(10, 5))

plt.scatter(
    df["Name"],
    df["Age"]
)

plt.title("Employee Ages by Name")
plt.xlabel("Name")
plt.ylabel("Age")

plt.xticks(rotation=50)
plt.tight_layout()
plt.show()


# ============================================
# 4. Pie Chart
# ============================================

department_count = df["Department"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)

plt.title("Employee Distribution by Department")
plt.show()