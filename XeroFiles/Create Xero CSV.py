import os
import pandas as pd
os.chdir(r'C:\Users\r.christianto\MyPython\XeroFiles')


def Type(Name):
    if Name in ('Assets','Liabilities','Equity'):
        x = 'BS'
    else:
        x = 'PNL'
    return x
    
def Bal(a,b):
    x = a - b
    return x

def Amt(a,b,type):
    if type == 'PNL':
        x = a
    else:
        x = b
    return x

def YTD(a,b,type):
    if type == 'PNL':
        x = b
    else:
        x = a
    return x



df = pd.read_csv('Xero.txt',sep=';',skiprows=[0],header=None)
df.columns = ['Date', 'XeroOrganisation' ,'SectionName', 'AccountCode', 'AccountName',
       'Debit', 'Credit', 'YTD Debit', 'YTD Credit']

df['Debit'].fillna(0,inplace=True)
df['Credit'].fillna(0,inplace=True)
df['YTD Debit'].fillna(0,inplace=True)
df['YTD Credit'].fillna(0,inplace=True)

df['Type'] = df.apply(lambda x:Type(x['SectionName']),axis=1)
df['Movement'] = df.apply(lambda x:Bal(x.Debit,x.Credit),axis=1)
df['Spot'] = df.apply(lambda x:Bal(x['YTD Debit'],x['YTD Credit']),axis=1)



df['Cube'] = 'LCA:XRO_Trial Balance'
df['Version'] = 'Actual'
df['Currency'] = 'Local'
df['Measure'] = 'Balance'
df['Amt'] = df.apply(lambda x:Amt(x['Movement'],x['Spot'],x['Type']),axis=1)
df['YTD'] = df['Spot']

# final results
df = df [['Date','SectionName','AccountName',
'Debit', 'Credit', 'YTD Debit', 'YTD Credit', 'Type', 'Movement',
'Spot', 'Cube', 'XeroOrganisation','Version', 'Currency', 'Measure', 'AccountCode', 'Amt','YTD']]
df.to_csv('Xero.csv',index=False)