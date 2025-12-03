'''import pandas as pd
df=pd.read_csv("retail_sales.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.shape)'''

import pandas as pd
df=pd.read_csv("retail_sales.csv")
print("Store:")
print(df.groupby('Store A')['Total Price'].sum())
print("City")
print(df.groupby('City')['Total Price:'].sum())
print("Category:")
print(df.groupby('Category')['Total Price'].sum())

