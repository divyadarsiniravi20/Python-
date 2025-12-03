import pandas as pd
df = pd.read_csv("retail.csv")
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
#df["Date"]=pd.to_datetime(df["Date"])
#print(df.info())
#df["Year"]=df["Date"].dt.year
#df["Month"]=df["Date"].dt.month
#df["Day"]=df["Date"].dt.day
#print(df)

#high_elc=df[(df ["Category"] == ("Electronics")) & (df["TotalPrice"]>10000)]
#print(high_elc)

#sorted_df=df.sort_values("TotalPrice",ascending=False)
#print(sorted_df)

category_sales=df.groupby("Category")["TotalPrice"].sum()
print(category_sales)
'''
store_avg=df.groupby("Store")["TotalPrice"].mean()
print(store_avg)
city_orders=df.groupby("City")["OrderID"].count()
print(city_orders)'''