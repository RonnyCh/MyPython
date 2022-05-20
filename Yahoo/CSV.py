# create a py file using below code and name it test. py

import pandas as pd

df = pd.DataFrame({'Name':[1,2,34]})
df.to_csv('Tinker.csv')

print ('Done')