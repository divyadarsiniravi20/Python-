import pandas as pd
df=pd.read_csv("shop.csv")
#print(df.head(10))
#print(df)
print(df.info())
print(df.columns[df.isnull().any()])
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
print(df.info())

#cleaning and transformation
df["ShippingDays"]=(df["ShipDate"]-df["OrderDate"]).dt.days
print(df.info())
df["ProfitMargin"]=df["Profit"]/df["Sales"]
print(df["ProfitMargin"])

df["CustomerName"]=df["CustomerName"].str.title()
print(df["CustomerName"])

df=df[df["Sales"]>0]
print(df)
df["Discount"]=(df["Discount"] *100).astype(str)+"%"
print(df["Discount"])

new_ord=df[df["Region"]=="West"]
print(new_ord)

tech_sale=df[(df["Category"]== "Technology")&(df["Sales"]>400)]
print(tech_sale)

all_pr=df[df["Returned"]=="Yes"]["ProductName"]
print(all_pr)

date=df[(df["Category"]=="Furniture") & (df["ShipDate"] > "2024-01-20")]
print(date)

new_profit=df[df["Profit"]<20]
print(new_profit)

so_sales=df.sort_values(by="Sales",ascending=False)
print(so_sales)

sort_Margin=df.sort_values(by="ProfitMargin",ascending=False)
print(sort_Margin)

sort_region=df.sort_values(by="Region",ascending=True)
print(sort_region)

sort_city=df.sort_values(by="City",ascending=True)
print(sort_city)

sort_days=df.sort_values(by="ShipDate",ascending=False)
print(sort_days)

sort_custname=df.sort_values(by="CustomerName",ascending=True)
print(sort_custname)

total=df.groupby("Region")["Sales"].sum()
print(total)

avg_profit=df.groupby("Category")["Profit"].mean()
print(avg_profit)

order_c=df.groupby("CustomerID")["OrderID"].count()
print(order_c)

sale_sum=df.groupby("Segment")["Sales"].sum()
print(sale_sum)

sold=df.groupby("SubCategory")["Quantity"].sum()
print(sold)

ship_mean=df.groupby("Category")["ShipDate"].mean()
print(ship_mean)