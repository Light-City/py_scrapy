from urllib.request import urlretrieve
import os
os.makedirs('./img/',exist_ok=True)

# 使用urlretrieve
IMAGE_URL = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
urlretrieve(IMAGE_URL,'./img/image1.png')
# 使用request
import requests
r = requests.get(IMAGE_URL)
with open('./img/image2.png','wb') as f:
    f.write(r.content)
with open('./img/image3.png','wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
