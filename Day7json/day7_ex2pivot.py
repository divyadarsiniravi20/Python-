import pandas as pd
df=pd.read_csv("shop.csv")
pivot=df.pivot_table(index="Region",columns="Category",values="Sales",aggfunc="sum")
print(pivot)

table=df.pivot_table(index="SubCategory",columns="Segment",values="Sales")
print(table)

order_count=df.pivot_table(index="Returned",columns="Region",values="OrderID",aggfunc="count")
print(order_count)

avg_price=df.pivot_table(index="Category",values="UnitPrice",aggfunc="mean")
print(avg_price)
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["Month"]=df["OrderDate"].dt.month
total_quantity=df.pivot_table(index="Region",columns="Month",values="Quantity",aggfunc="sum")
print(total_quantity)



