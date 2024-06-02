import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into DataFrame
file_path = 'titanic.csv'
df = pd.read_csv(file_path)

# Data Preparation
# Bar Chart Data: Count of passengers by class
passenger_counts = df['Pclass'].value_counts().sort_index()

# Line Chart Data: Average fare by age group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80])
average_fare_by_age = df.groupby('AgeGroup')['Fare'].mean()

# Create a Bar Chart
plt.figure(figsize=(10, 6))
passenger_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Passengers by Class')
plt.xlabel('Class')
plt.ylabel('Number of Passengers')
plt.xticks(rotation=0)
plt.show()

# Create a Line Chart
plt.figure(figsize=(10, 6))
average_fare_by_age.plot(kind='line', marker='o', color='green')
plt.title('Average Fare by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Fare')
plt.grid(True)
plt.show()
