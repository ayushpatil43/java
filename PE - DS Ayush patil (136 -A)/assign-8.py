import pandas as pd

df=pd.read_csv(r"C:\Users\sarvesh mahadik\Desktop\P.E. 5th sem\used_car_listings (version 1).xlsb.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head(5))

# Display last 5 rows
print("\nLast 5 rows:")
print(df.tail(5))

# Show column names
print("\nColumn names:")
print(df.columns)

# Check the shape of dataframe
print("\nShape of dataset:")
print(df.shape)

# Get info about dataset
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Count unique values in each column
print("\nUnique values in each column:")
print(df.nunique())

# Display random 5 rows
print("\nRandom 5 rows:")
print(df.sample(5))





# head() - First 5 rows
# tail() - Last 5 rows
# columns - Column names
# shape - Number of rows and columns
# info() - Data types and non-null counts
# isnull().sum() - Count missing values
# describe() - Basic statistics
# nunique() - Count unique values
# sample() - Random rows




#series:
# Create a series from a column
series = df['price']

# Display first 5 values
print("First 5 values:")
print(series.head(5))

# Display last 5 values
print("\nLast 5 values:")
print(series.tail(5))

# Check the shape of series
print("\nShape of series:")
print(series.shape)

# Get data type
print("\nData type:")
print(series.dtype)

# Check for missing  values
print("\nMissing values:")
print(series.isnull().sum())

# Count total values
print("\nTotal values:")
print(series.count())

# Basic statistics
print("\nBasic statistics:")
print(series.describe())

# Get unique values count
print("\nUnique values:")
print(series.nunique())

# Display random 5 values
print("\nRandom 5 values:")
print(series.sample(5))

# Get max value
print("\nMaximum value:")
print(series.max())

# Get min value
print("\nMinimum value:")
print(series.min())

# Get mean value
print("\nMean value:")
print(series.mean())