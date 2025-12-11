import pandas as pd
df=pd.DataFrame()
df["days_left"] = (pd.to_datetime(df["expiry_date"]) - pd.Timestamp.today())