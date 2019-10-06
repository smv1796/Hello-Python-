import pandas as pd

df=pd.read_csv("C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/international-airline-passengers.csv",engine="python", skipfooter=3)

print(df.columns)
df.columns=["Month", "Passengers"]
print(df.columns)

#print(df["Month"])
#Alternative method to above when the column names are strings(won't work if the column name has spaces in it)
print(df.Month)

print(df.shape)

#Addition of a column having one

df['ones']=1
print(df.head)

# Usage of apply
from datetime import datetime

print(datetime.strptime("1949-05", "%Y-%m"))

df["dt"]=df.apply(lambda row: datetime.strptime(row["Month"], "%Y-%m"), axis=1)

print(df.head)
print(df.info())

# usage of JOINS
