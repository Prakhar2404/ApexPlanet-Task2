import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned_Dataset.xlsx")

print("========== DATASET INFORMATION ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== COLUMN NAMES ==========")
print(df.columns)

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

plt.figure(figsize=(7,5))
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("Age_Distribution.png")
plt.show()

category_sales = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Sales_by_Category.png")
plt.show()

gender_count = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender_count, labels=gender_count.index, autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.savefig("Gender_Distribution.png")
plt.show()

city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Sales_by_City.png")
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(df["Quantity"], df["Total_Sales"])
plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("Quantity_vs_TotalSales.png")
plt.show()

plt.figure(figsize=(6,5))
plt.boxplot(df["Total_Sales"])
plt.title("Box Plot of Total Sales")
plt.ylabel("Total Sales")
plt.savefig("Sales_Boxplot.png")
plt.show()

