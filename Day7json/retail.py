
import pandas as pd

data = {
    "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,
                1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,
                1041,1042,1043,1044,1045,1046,1047,1048,1049,1050],
    "Date": ["2024-01-05","2024-01-05","2024-01-06","2024-01-06","2024-01-07","2024-01-07","2024-01-08","2024-01-08","2024-01-09","2024-01-09",
             "2024-01-10","2024-01-10","2024-01-11","2024-01-11","2024-01-12","2024-01-12","2024-01-12","2024-01-13","2024-01-13","2024-01-13",
             "2024-01-14","2024-01-14","2024-01-14","2024-01-15","2024-01-15","2024-01-15","2024-01-16","2024-01-16","2024-01-16","2024-01-17",
             "2024-01-17","2024-01-17","2024-01-18","2024-01-18","2024-01-18","2024-01-19","2024-01-19","2024-01-19","2024-01-20","2024-01-20",
             "2024-01-20","2024-01-21","2024-01-21","2024-01-21","2024-01-22","2024-01-22","2024-01-22","2024-01-23","2024-01-23","2024-01-23"],
    "Store": ["Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A",
              "Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B",
              "Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C",
              "Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A",
              "Store B","Store C","Store A","Store B","Store C","Store A","Store B","Store C","Store A","Store B"],
    "City": ["Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai",
             "Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi",
             "Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore",
             "Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai",
             "Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi","Bangalore","Mumbai","Delhi"],
    "Product": ["Laptop","Shampoo","Jeans","Smartphone","Bread","T-Shirt","Milk","Perfume","Headphones","Rice",
                "Shoes","Milk","Charger","Notebook","Smartwatch","Biscuits","Jacket","Soap","Keyboard","Shirt",
                "Flour","Watch","Socks","Bag","Pen","Notebook","Charger","Soap","Laptop","Jeans",
                "Biscuits","Milk","Smartphone","Rice","Shampoo","T-Shirt","Headphones","Perfume","Bread","Notebook",
                "Shoes","Bag","Shirt","Keyboard","Biscuits","Milk","Smartwatch","Charger","T-Shirt","Soap"],
    "Category": ["Electronics","Personal Care","Apparel","Electronics","Grocery","Apparel","Grocery","Personal Care","Electronics","Grocery",
                 "Apparel","Grocery","Electronics","Stationery","Electronics","Grocery","Apparel","Personal Care","Electronics","Apparel",
                 "Grocery","Accessories","Apparel","Accessories","Stationery","Stationery","Electronics","Personal Care","Electronics","Apparel",
                 "Grocery","Grocery","Electronics","Grocery","Personal Care","Apparel","Electronics","Personal Care","Grocery","Stationery",
                 "Apparel","Accessories","Apparel","Electronics","Grocery","Grocery","Electronics","Electronics","Apparel","Personal Care"],
    "Quantity": [1,3,2,1,5,4,10,1,2,3,1,12,2,10,1,6,1,4,1,2,5,1,3,1,10,6,3,5,1,1,4,9,1,2,3,2,1,1,6,4,1,1,1,2,7,13,1,2,2,3],
    "UnitPrice": [55000,120,1500,25000,40,800,50,2500,1500,90,3000,48,600,35,8000,25,4500,45,1200,1100,55,2500,150,1800,12,35,600,45,52000,1500,
                  25,50,26000,90,120,800,1500,2800,40,35,3000,2000,1100,1200,25,50,8200,600,800,45],
    "TotalPrice": [55000,360,3000,25000,200,3200,500,2500,3000,270,3000,576,1200,350,8000,150,4500,180,1200,2200,275,2500,450,1800,120,210,1800,225,52000,1500,
                   100,450,26000,180,360,1600,1500,2800,240,140,3000,2000,1100,2400,175,650,8200,1200,1600,135],
    "PaymentMethod": ["Credit Card","Cash","Credit Card","UPI","Cash","Credit Card","UPI","Credit Card","Cash","Credit Card","UPI","Cash","Credit Card","Cash","UPI","Credit Card","UPI","Cash","UPI","Credit Card",
                      "UPI","Cash","UPI","Credit Card","Cash","UPI","Cash","UPI","Credit Card","Cash","Credit Card","UPI","Cash","UPI","Credit Card","UPI","Credit Card","Cash","UPI","Cash","UPI","Credit Card","Cash","UPI","Cash","Credit Card","UPI","Cash","UPI","Credit Card"],
    "CustomerType": ["New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning",
                     "New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning","New","Returning"]
}

# Create DataFrame
df = pd.DataFrame(data)

df.to_csv("retail.csv",index=False) # Show first 5 rows
