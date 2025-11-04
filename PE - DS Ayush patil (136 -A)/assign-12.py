import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\sarvesh mahadik\Desktop\P.E. 5th sem\used_car_listings (version 1).xlsb.csv")

# Line plot
plt.figure(figsize=(8,6))
plt.plot(df['price'].head(20))
plt.title("Line Plot - Price")
plt.xlabel("Index")
plt.ylabel("Price")
plt.show()



# Bar plot
plt.figure(figsize=(8,6))
df['brand'].value_counts().head(10).plot(kind='bar')
plt.title("Bar Plot - Top 10 Brands")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.show()

# Histogram
plt.figure(figsize=(8,6))
plt.hist(df['price'], bins=20, color='green')
plt.title("Histogram - Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(df['year'], df['price'], alpha=0.5)
plt.title("Scatter Plot - Year vs Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()

# Pie chart
plt.figure(figsize=(8,6))
df['fuel_type'].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie Chart - Fuel Type Distribution")
plt.ylabel("")
plt.show()

# Horizontal bar plot
plt.figure(figsize=(8,6))
df['brand'].value_counts().head(10).plot(kind='barh', color='orange')
plt.title("Horizontal Bar Plot - Top 10 Brands")
plt.xlabel("Count")
plt.ylabel("Brand")
plt.show()

# Box plot
plt.figure(figsize=(8,6))
plt.boxplot(df['price'])
plt.title("Box Plot - Price")
plt.ylabel("Price")
plt.show()