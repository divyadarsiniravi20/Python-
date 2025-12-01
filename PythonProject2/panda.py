'''import pandas as pd
s=pd.Series([10,20,30,40])#SEries
print(s)
data={#dataframe
    "Name":["Alisha","Rahul","John"],
    "Marks":[85,92,78]
}
df=pd.DataFrame(data)
print(df)'''

import pandas as pd
data={
    "Name":["Alisha","Rahul","John"],
    "Marks":[85,92,78],
    "Age":[10,22,20]
}
df=pd.DataFrame(data)
df.to_csv("student.csv",index=False)
print("CSV is created")

import pandas as pd
f=pd.read_csv("student.csv")
print("csv read successfully")
print(f)

import pandas as pd
df=pd.DataFrame({
    "Name":["Alisha","Rahul","John"],
    "Marks":[85,92,78],
    "Age":[10,22,10],
    "City" :["Chennai","Goa","Jaipur"]
})

'''
print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.describe())
print(df.columns)

print(df["Name"])
print(df[["Name","Marks"]])
#filter
high_scorers=df[df["Marks"]>70]
print(high_scorers)

filtered=df[(df["Marks"]>70) & (df["Age"]>22)]
print(filtered)'''

'''df["Result"]=df["Marks"].apply(lambda x:"pass" if x>70 else "fail")
print(df)

sorted_df=df.sort_values(by="Marks",ascending=True)
print(sorted_df)'''


'''
df2=df.copy()
df2.loc[2,"City"]=None
print(df2)
print(df2.isnull().sum())
df2_filled=df2.fillna("Unknown")
print(df2_filled)
'''
city_count=df.groupby("City")["Name"].count()
print(city_count)
avg_marks = df.groupby("City")["Marks"].mean()
print(avg_marks)