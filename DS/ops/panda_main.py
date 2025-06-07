import pandas as pd
import numpy as np

# Series | one-dimensional labeled array
a = pd.Series([1, 2, 3, 4, 5])
print(a)

# DataFrame | two-dimensional labeled data structure /w columns of potentially different types
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)
print(df)

# Read & Write
df = pd.read_csv('file.csv')                                    # CSV   (Read)
df.to_csv('output.csv', index=False)                            # CSV   (Write)
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')            # Excel (Read)
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)    # Excel (Write)
import sqlite3                                                  # SQL   (Read)
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table_name', conn)
conn = sqlite3.connect('database.db')                           # SQL   (Write)
df.to_sql('table_name', conn, if_exists='replace')
df = pd.read_json('file.json')                                  # JSON  (Read)
df.to_json('output.json')                                       # JSON  (Write)

# Data Inspection
df.head()               # First 5 rows
df.tail()               # Last 5 rows
df.shape                # DataFrame dimensions
df.describe()           # Summary statistics
df.info()               # Column information
df.columns              # Column names
df.index                # Index
