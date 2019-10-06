import pandas as pd

t1=pd.read_csv("C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/table1.csv")
t2=pd.read_csv("C:/Users/Lenovo/PycharmProjects/HelloPython/Resources/table2.csv")

print(t1)
print(t2)

#Merging two tables on the basis of "user-id"

m=pd.merge(t1,t2,on="user_id")
print(m)
#or we can use this(below)
print(t1.merge(t2,on="user_id"))
