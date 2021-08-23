import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup
# #设置代理IP
# proxy = {'http':'1.196.177.243:9999','https':'115.221.242.61:9999'}
# #发送请求
# response = requests.get('https://www.baidu.com',proxies = proxy)
# print(response.content.decode('utf-8'))

#设置请求头
url = 'https://www.baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'}
#设置代理IP
proxy = {'http':'1.196.177.243:9999','https':'115.221.242.61:9999'}
try:
    response = requests.get(url,headers = headers,timeout=0.5)
    html = response.content
    # print(response.status_code)
    soup = BeautifulSoup(html,features='lxml')
    print(soup.find('title').text)
except ReadTimeout:
    print('超时')
except HTTPError:
    print('请求错误')
except RequestException:
    print('请求异常')