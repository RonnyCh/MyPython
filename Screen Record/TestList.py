
import pandas as pd

df = pd.read_csv(r"C:\Users\r.christianto\MyPython\Screen Record\record.csv")
list = df.values.tolist()

def test():
    a = 100
    print (a)

for i in range(len(list)):
    row = list[i]
    if list[i][1]=='shift':
        # assign next value, e.g shift 2 (@)
        list[i+1][0] = 'shift'
      




print (i)

