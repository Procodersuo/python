import pandas as pd
import os
data = [
    ['Ali', 21, 'Lahore'],
    ['Ahmed', 22, 'Karachi'],
    ["TALHA", 23, 'Islamabad']
    ]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
 # Access single column
print(df['Name'])
#READING A CSV FILE
df = pd.read_excel("E:\python\pythonl\pandas\data2.xlsx")
print(df)
