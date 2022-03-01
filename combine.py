from pickle import TRUE
import pandas as pd
import glob

csv_files = glob.glob("data/*.csv")

list = []
for file in csv_files:
    list.append(pd.read_csv(file))

print(list)

df = pd.concat(list,sort=False)
df.to_csv("total.csv",index=TRUE)