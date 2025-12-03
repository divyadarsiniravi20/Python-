import pandas as pd
df=pd.DataFrame({
    "Name ":["Aisha","Rahul","John"],
    "Marks ":[87,92,78],
    "City":["Mumbai","Delhi","Chennai"]
})
df.to_json("students.json",orient="records",index=4)
print("JSON created")
df=pd.read_json("students.json")
print("JSON read")
print(df)