from pyquery import PyQuery as pQuery
import requests
import re

def download_mp3():
    pass


base_url = "http://www.qinzixuexi.com"
# html = requests.get(base_url+"/ys_kw_p25.html").content
# # print(pQuery(html)('li.gxbox ul li a'))
# for link in pQuery(html)('li.gxbox ul li.l1 a'):
#     print(link.attrib['href'] + " " + link.attrib['alt'])

# html = requests.get(base_url+"/ys_kw/a20107.html").content
# print(pQuery(html)('#vlink_1 ul li input'))
# for rid in (pQuery(html)('#vlink_1 ul li input')):
#     print(rid.attrib['value'])

html = requests.get(base_url+"/player.php?rid=189090").content
# {mp3:"http://p0124.iusheng.com/userUp/2018/03/23686/u07_lesson3_gt.mp3"}
pattern = re.compile(r'\{mp3:".+"\}')
match = pattern.match(html)
if match:
    print(match.group())
