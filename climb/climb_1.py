
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
url = 'http://www.ehappy.tw/demo.htm'
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.text)


# In[7]:


import requests
payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.text)


# In[9]:


import requests
payload = {'key1':'value1','key2':'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)


# In[13]:


import requests
from bs4 import BeautifulSoup
url = 'http://ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text,'lxml')
print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)


# In[15]:


import requests
from bs4 import BeautifulSoup
html = '''
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>我是標題網頁</title>
        </head>
        <body>
            <div>
                <p id='p1'>我是第一段</p>
                <p id='p2' class='red'>我是第二段</p>
            </div>
        </body>
    </html>
'''

sp = BeautifulSoup(html,'lxml')
print(sp.find('p')) #找第一個
print(sp.find_all('p')) #找全部
print(sp.find('p',{'id':'p2','class':'red'}))
print(sp.find('p',id='p2',class_ = 'red')) #效果與上一行相同, class為關鍵字 所以補上底線才可認定為變數


# In[19]:


import requests
from bs4 import BeautifulSoup
html = '''
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>我是標題網頁</title>
        </head>
        <body>
            <div>
                <p id='p1'>我是第一段</p>
                <p id='p2' class='red'>我是第二段</p>
            </div>
        </body>
    </html>
'''

sp = BeautifulSoup(html,'lxml')
print(sp.select('title')) 
print(sp.select('p')) 
print(sp.select('#p1'))
print(sp.select('.red'))


# In[20]:


import requests
from bs4 import BeautifulSoup
html = '''
<html>
<head>
<meta charset="UTF-8">
<title>我是網頁標題</title>
</head>
<body>
<img src="http://www.ehappy.tw/python.png">
<a href="http://www.e-happy.com.tw">超連結</a>
</body>
</html>
'''

sp = BeautifulSoup(html,'lxml')
print(sp.select('img')[0].get('src')) 
print(sp.select('a')[0].get('href')) 
print(sp.select('img')[0]['src']) 
print(sp.select('a')[0]['href']) 


# In[65]:


import requests
from bs4 import BeautifulSoup
url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text,'lxml')
print( '威力彩林俊佑期數:' +sp.select('.contents_mine_tx02')[0].select('span')[0].text)
s = ''
for i in range(3,9):
    s += ' ' + sp.select('.contents_box02')[0].select('div')[i].text
print( '開出順序:' + s)
s = ''
for i in range(9,15):
    s += ' ' + sp.select('.contents_box02')[0].select('div')[i].text
print( '大小順序:' + s)
print('第二區:' + sp.select('.contents_box02')[0].select('div')[15].text)

# In[2]:


from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=pkSjkse6j-o')
yt.streams.first().download()


# In[ ]:





# In[ ]:




