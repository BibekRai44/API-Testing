import requests
import pandas as pd
import csv
from requests.api import head

url='https://web-series-quotes-api.deta.dev/quote/?series=breaking_bad&count=100'
params={'series':'breaking_bad','count':100}

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}

response=requests.request('GET',url,headers=headers,params=params)
myjson=response.json()

quotes=[]
for i in range(len(myjson)):
    data={
        "ID":myjson[i]['id'],
        "Quote":myjson[i]['quote']
    }
    quotes.append(data)
df=pd.DataFrame(quotes)
df.to_csv('Quotes.csv',index=True)
print(myjson)


