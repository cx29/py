#!/usr/bin/python3

import csv
# 重命名一下免得打太多字 https://www.runoob.com/pandas/pandas-csv-file.html pandas学习链接
import pandas as pd

# 使用reader读取文件
# with open('titanic.csv','r') as f:
#     reader =csv.reader(f)
#     print(type(reader))
#     result=list(reader)
#     print(result[0])

# 使用pandas读取文件
data=pd.read_csv('titanic.csv')
for x in data.index:
    if data.loc[x,"sex"] =="male":
        data.loc[x,"sex"] = 0
    if data.loc[x,"sex"] =="female":
        data.loc[x,"sex"]=1
data.set_index("survived",inplace=True)
data.to_csv("./a.csv")
print(data.to_string())
