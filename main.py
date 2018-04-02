from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.qinzixuexi.com/ys_kw_p11.html").content
# soup = BeautifulSoup(html, "lxml", from_encoding='utf-8')
# print(soup.prettify())
print(pq(html)('li.gxbox ul li.l1'))
