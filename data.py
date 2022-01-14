import pandas as pd
from datetime import date, datetime

# ! Remember to enter time in 24 hours format
df = pd.read_csv("D:\Coding\Python Projects\Zoom Meeting Automation\classes.csv")
lst = df.values.tolist()

to_remove = list()
date_today = datetime.today()

for l in lst:
    date = datetime(int(l[3][6:]), int(l[3][3:5]), int(l[3][:2]), 23, 59, 59, 696969)
    if (date-date_today).total_seconds()<0:
        to_remove.append(l)

for remove in to_remove:
    lst.remove(remove)

lst = sorted(lst, key=lambda x: x[1][0:2]) # Sorting according to start time
lst = sorted(lst, key=lambda x: x[3][0:2]) # Sorting according to day
lst = sorted(lst, key=lambda x: x[3][3:5]) # Sorting according to month
lst = sorted(lst, key=lambda x: x[3][6:])  # Sorting according to year

df = pd.DataFrame(lst)
df.columns = list("MSED")
df.to_csv("D:\Coding\Python Projects\Zoom Meeting Automation\classes.csv", index = False)
print(df)