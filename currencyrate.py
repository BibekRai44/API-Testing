import requests
from requests.api import head

url='https://www.freeforexapi.com/api/live?pairs=EURGBP,USDJPY,EURUSD,GBPUSD,AUDUSD,USDCHF,NZDUSD,USDCAD,USDZAR'

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}
response=requests.request("GET",url,headers=headers)
myjson=response.json()
print(myjson)