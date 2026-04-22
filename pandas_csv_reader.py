'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 12 Assignment 2
Code Helper - Gemini Google Ai
'''
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Print the contents of the DataFrame
print(df)

#Print the number of rows and columns in the DataFrame
# df.shape returns a tuple (number of rows, number of columns)
rows = df.shape[0]
cols = df.shape[1]

print(f"Rows:{rows}")
print(f"Columns:{cols}")