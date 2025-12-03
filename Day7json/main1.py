import pandas as pd
df=pd.DataFrame({
    "Name ":["Aisha","Rahul","John"],
    "Marks ":[87,None,78],
    "City":["Mumbai","Delhi",None],
    "Age":[22,None,18]
})
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.replace("",None).isnull().sum())
