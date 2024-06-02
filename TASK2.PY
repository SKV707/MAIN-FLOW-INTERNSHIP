import pandas as pd

# Load CSV file into DataFrame
file_path = 'titanic.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Filter rows where 'Age' is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nRows where Age is greater than 30:")
print(filtered_df)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped.head())

# Fill missing values with 0
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled.head())

# Fill missing values with the mean of the column
df_filled_mean = df.fillna(df.mean())
print("\nDataFrame after filling missing values with column mean:")
print(df_filled_mean.head())

# Summary statistics for numerical columns
summary_stats = df.describe()
print("\nSummary statistics for numerical columns:")
print(summary_stats)

# Additional statistics
mean_age = df['Age'].mean()
median_fare = df['Fare'].median()
max_fare = df['Fare'].max()

print(f"\nMean Age: {mean_age}")
print(f"Median Fare: {median_fare}")
print(f"Max Fare: {max_fare}")
