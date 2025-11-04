import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Karan', 'Meena', 'Sara'],
    'Age': [23, 21, 25, 22, 24],
    'Marks': [85, 90, 78, 88, 95],
    'City': ['Mumbai', 'Delhi', 'Pune', 'Chennai', 'Delhi']
}

df = pd.DataFrame(data)
print("Original DataFrame")
print(df)
print("\n")

print("First 5 rows")
print(df.head())
print("\n")

print("Last 5 rows")
print(df.tail())
print("\n")

print("Selecting a single column (Name)")
print(df['Name'])
print("\n")

print("Selecting multiple columns (Name and Marks)")
print(df[['Name', 'Marks']])
print("\n")

print("Students with Marks greater than 85")
filtered = df[df['Marks'] > 85]
print(filtered)
print("\n")

print("Sorting by Marks (Descending Order)")
sorted_df = df.sort_values(by='Marks', ascending=False)
print(sorted_df)
print("\n")

print("Adding a new column Grade")
df['Grade'] = ['B', 'A', 'C', 'B', 'A']
print(df)
print("\n")

print("Updating Karan's Marks to 82")
df.loc[2, 'Marks'] = 82
print(df)
print("\n")

print("Average Marks by City")
grouped = df.groupby('City')['Marks'].mean()
print(grouped)
print("\n")

print("Handling Missing Values")
df.loc[4, 'Marks'] = None
print("DataFrame with Missing Value:")
print(df)
print("\n")

df['Marks'].fillna(df['Marks'].mean(), inplace=True)
print("After filling Missing Value:")
print(df)
print("\n")

print("Merging with another DataFrame")
df2 = pd.DataFrame({
    'City': ['Mumbai', 'Delhi', 'Pune', 'Chennai'],
    'State': ['Maharashtra', 'Delhi', 'Maharashtra', 'Tamil Nadu']
})
merged_df = pd.merge(df, df2, on='City')
print(merged_df)
print("\n")

print("End of Program")