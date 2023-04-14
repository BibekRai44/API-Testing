import requests
from requests.api import head
import pandas as pd

url='https://www.freeforexapi.com/api/live?pairs=EURGBP,USDJPY,EURUSD,GBPUSD,AUDUSD,USDCHF,NZDUSD,USDCAD,USDZAR'

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}
response=requests.request("GET",url,headers=headers)
myjson=response.json()
currencyrate=[]
for pair in myjson['rates']:
    data={
        "Pair": pair,
        "Rate": myjson['rates'][pair]['rate'],
        "Timestamp": myjson['rates'][pair]['timestamp']
    }
    currencyrate.append(data)
df=pd.DataFrame(currencyrate)
df.to_csv('Currency Rate.csv',index=True)
print(myjson)