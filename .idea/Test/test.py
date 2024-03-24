import unittest

import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('Employees.csv')

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove decimal places in the Age column
df['Age'] = df['Age'].astype(int)

# 3. Convert USD salary to EGP (assuming 1 USD = 15 EGP)
df['Salary(USD)'] = df['Salary(USD)'] * 55

# 4. Print statistics
print("Average age:", df['Age'].mean())
print("Median salary:", df['Salary(USD)'].median())
gender_ratio = df['Gender'].value_counts(normalize=True)
print("Ratio between males and female employees:")
print("Male:", gender_ratio['M'])
print("Female:", gender_ratio['F'])


# 5. Write data to a new CSV file
df.to_csv('Filtered_data.csv', index=False)
