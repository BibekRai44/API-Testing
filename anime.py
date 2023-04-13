import requests
from requests.api import head
from PIL import Image
url="https://api.waifu.im/search/?excluded_files=4401" \
      "&excluded_files=3133" \
      "&gif=false" \
      "&excluded_tags=maid" \
      "&excluded_tags=oppai" \
      "&is_nsfw=false"

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}
response=requests.request("GET",url,headers=headers)
myjson=response.json()
image_url=myjson['images'][0]['url']
response=requests.get(image_url,stream=True)
with open('waifu.jpg','wb') as f:
    for chunk in response.iter_content(1024):
        f.write(chunk)

img=Image.open('waifu.jpg')
img.show()
