import requests
import webbrowser

# param = {'wd':'莫烦python'}
# r = requests.get('http://www.baidu.com/s',params=param)
# print(r.url)
# webbrowser.open(r.url)

# data={'firstname':'z','lastname':'x'}
# r = requests.post('http://pythonscraping.com/pages/files/processing.php',data=data)
# print(r.text)


# file = {'uploadFile': open('./image.png', 'rb')}
# r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
# print(r.text)


# payload = {'username': 'z', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# print(r.text)

session = requests.Session()
payload = {'username': 'a', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)
