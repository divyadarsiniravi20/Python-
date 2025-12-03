
import pandas as pd

data = {
    "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,
                1021,1022,1023,1024,1025,1026,1027,1028,1029,1030],
    "OrderDate": ["2024-01-02","2024-01-02","2024-01-03","2024-01-03","2024-01-04","2024-01-04","2024-01-05","2024-01-05","2024-01-06","2024-01-06",
                  "2024-01-07","2024-01-07","2024-01-08","2024-01-08","2024-01-09","2024-01-09","2024-01-10","2024-01-10","2024-01-11","2024-01-11",
                  "2024-01-12","2024-01-12","2024-01-13","2024-01-13","2024-01-14","2024-01-14","2024-01-15","2024-01-15","2024-01-16","2024-01-16"],
    "ShipDate": ["2024-01-05","2024-01-06","2024-01-07","2024-01-08","2024-01-09","2024-01-08","2024-01-10","2024-01-11","2024-01-12","2024-01-13",
                 "2024-01-14","2024-01-15","2024-01-16","2024-01-17","2024-01-18","2024-01-19","2024-01-20","2024-01-21","2024-01-22","2024-01-23",
                 "2024-01-24","2024-01-25","2024-01-26","2024-01-27","2024-01-28","2024-01-29","2024-01-30","2024-01-31","2024-02-01","2024-02-02"],
    "Region": ["West","Central","East","South","West","Central","East","South","West","Central","East","South","West","Central","East","South","West","Central","East","South",
               "West","Central","East","South","West","Central","East","South","West","Central"],
    "City": ["Los Angeles","Chicago","New York","Miami","Seattle","Denver","Boston","Atlanta","Portland","St. Louis","Philadelphia","Orlando","San Diego","Minneapolis","Newark","Charlotte","Las Vegas","Columbus","Baltimore","Nashville",
             "Sacramento","Kansas City","Pittsburgh","San Antonio","Fresno","Indianapolis","Cleveland","Dallas","San Jose","Detroit"],
    "CustomerID": ["C001","C002","C003","C004","C005","C006","C007","C008","C009","C010","C011","C012","C013","C014","C015","C016","C017","C018","C019","C020",
                   "C021","C022","C023","C024","C025","C026","C027","C028","C029","C030"],
    "CustomerName": ["David Miller","Sarah Johnson","John Lee","Ana Gomez","Karen Black","Robert Brown","Emily Davis","Kyle Young","Sophia Hill","Tom Harris",
                     "Olivia Adams","Ethan Clark","Isabella Scott","George Wilson","Abigail Perez","Noah Walker","Michael Green","Chloe Ramirez","Lucas Cook","Ava Howard",
                     "Daniel Ward","Harper Reed","Benjamin Brooks","Grace Bennett","Elijah Rivera","Mia Mitchell","Henry Price","Lily Torres","Owen Jenkins","Aiden Lewis"],
    "Segment": ["Consumer","Corporate","Home Office","Consumer","Consumer","Corporate","Consumer","Home Office","Consumer","Corporate","Home Office","Consumer","Consumer","Corporate","Consumer","Home Office","Consumer","Corporate","Consumer","Home Office",
                "Consumer","Corporate","Consumer","Home Office","Consumer","Corporate","Consumer","Home Office","Consumer","Corporate"],
    "Category": ["Technology","Furniture","Office Supplies","Technology","Furniture","Office Supplies","Technology","Furniture","Technology","Office Supplies","Furniture","Technology","Furniture","Office Supplies","Technology","Furniture","Technology","Office Supplies","Technology","Furniture",
                 "Furniture","Office Supplies","Technology","Furniture","Technology","Office Supplies","Furniture","Technology","Office Supplies","Technology"],
    "SubCategory": ["Laptops","Chairs","Binders","Phones","Tables","Pens","Accessories","Chairs","Phones","Paper","Tables","Accessories","Sofas","Markers","Tablets","Desks","TVs","Notebooks","Accessories","Chairs",
                    "Bed","Envelopes","Accessories","Shelves","Laptops","Stapler","Tables","Printers","Binders","Accessories"],
    "ProductName": ["HP Pavilion 15","ErgoMax Pro Chair","Premium Binder Pack","Samsung Galaxy A54","Oak Wooden Table","Blue Pen Pack (20)","Wireless Mouse","ComfortMesh Chair","iPhone SE","A4 Copier Paper (500)",
                    "Adjustable Standing Desk","USB-C Cable","Modern Sofa 3-Seater","Color Marker Set","iPad 10th Gen","Compact Writing Desk","Sony 43-inch LED","Hardcover Notebook","Laptop Stand","Executive Leather Chair",
                    "Queen Bed Frame","White Envelope Pack","Keyboard","Wooden Shelf Unit","Dell Inspiron 14","Premium Stapler","Round Dining Table","HP LaserJet Pro","Premium Binders (12)","Webcam"],
    "Quantity": [1,2,5,1,1,3,4,1,2,10,1,6,1,4,1,1,1,8,2,1,1,6,3,1,1,2,1,1,2,1],
    "UnitPrice": [720,140,12,399,450,8,18,160,429,5,320,9,850,7,450,210,540,4,24,260,600,3,22,180,640,14,520,290,11,45],
    "Discount": [0,0.1,0,0.05,0,0,0,0.15,0,0,0.1,0,0.2,0,0.05,0,0.1,0,0,0.05,0.1,0,0.1,0,0,0,0.05,0,0,0],
    "Sales": [720,252,60,379.05,450,24,72,136,858,50,288,54,680,28,427.5,210,486,32,48,247,540,18,59.4,180,640,28,494,290,22,45],
    "Profit": [95,30,11,48,52,5,14,19,115,6,35,12,88,4,60,27,62,6,12,28,72,3,9,24,85,5,58,34,4,9],
    "Returned": ["No","No","No","No","Yes","No","No","No","No","No","No","No","Yes","No","No","No","No","No","No","No","Yes","No","No","No","No","No","No","No","No","No"]
}

df = pd.DataFrame(data)
df.to_csv("shop.csv",index=False)
