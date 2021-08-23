import requests
from bs4 import BeautifulSoup
import re

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'}
url = 'https://movie.douban.com/chart'
response = requests.get(url,headers = head)
soup = BeautifulSoup(response.content,features='lxml')
# print(soup.prettify())
# title_list = soup.find_all('title')
# # pattens = r'(\u4e00-\u9fa5)+'
# print(title_list)

list = soup.find_all(class_='pl2')
titles = []
patten = r'[\u4e00-\u9fa5]+'
for i in list:
    title = i.a.get_text()
    titles.append(title)
    titles_tr = str(titles)
    titles_list = re.findall(pattern=patten,string=titles_tr)





