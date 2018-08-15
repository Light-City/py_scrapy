import time
import requests
from bs4 import BeautifulSoup as bs

from selenium import webdriver


import matplotlib.pyplot as plt
import matplotlib.image as mping

driver = webdriver.Chrome()

URL = 'http://www.ngchina.com.cn/animals/'
driver.get(URL)

time.sleep(7)
html=driver.page_source
# print(html)
soup = bs(html,'lxml')
img_ul = soup.find_all('ul',{"class":"img_list"})
print(img_ul)


driver_cookie = driver.get_cookies()
cookies = [item["name"] + "=" + item["value"] for item in driver_cookie]
cookiesStr = ' '.join(cookies)
# print cookiesStr
with open('cookies.txt', 'w') as f:
    f.write(cookiesStr)

with open('cookies.txt') as f:
    str_cookies = f.read()
print("str_cookies..................."+str_cookies)
list_cookies = str_cookies.split(' ')  # 对字符串切片,返回分割后的字符串列表

cookies = {}
for cookie in list_cookies:
    '''
    robots=1
    cookie.split('=')
    变为
    ['robots', '1']
    key = cookie.split('=')[0]
    value = cookie.split('=')[-1]
    '''
    key = cookie.split('=')[0]
    value = cookie.split('=')[-1]
    '''
    dict.update(dict2)
    # 把字典dict2的键/值对更新到dict里
    '''
    cookies.update({key : value}) # 变为字典类型，如：{'robots': '1'}
print(cookies)
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

i=1
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']

        r = requests.get(url, headers=headers, cookies=cookies) # cookies与headers一起解决503错误
        print(r.status_code)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
        with open('./img/%s' % image_name, 'r') as f:
            _img = mping.imread('./img/%s' % image_name)
        if i==1:
            plt.figure()
        plt.subplot(2,3,i)
        plt.imshow(_img)
        plt.title(image_name)
        plt.axis('off')
        i=i+1
plt.show()
