from pyquery import PyQuery as pQuery
import requests
import re
import logging
import os

base_url = 'http://www.qinzixuexi.com'
base_path = 'g:\\PEP\\'


def download_res(res):
    pattern = re.compile(r'\{mp3:"(.+)"\}')
    for name, rid in res:
        html = requests.get(base_url+"/player.php?rid={0}".format(rid)).text
        # {mp3:"http://p0124.iusheng.com/userUp/2018/03/23686/u07_lesson3_gt.mp3"}
        match = pattern.search(html)
        if match:
            url = match.group(1)
            logging.info('download {0}'.format(url))
            data = requests.get(match.group(1)).content
            path = os.path.join(os.path.sep, base_path, name)
            if not os.path.exists(path):
                os.makedirs(path)
            filename = os.path.basename(url)
            filename = os.path.join(os.path.sep, path, filename)
            f = open(filename, 'wb')
            f.write(data)
            f.close()


def get_resource_id(course):
    data = []
    for name, url in course:
        logging.info('process {0}, {1}'.format(name, url))
        html = requests.get(base_url + url).content
        for rid in (pQuery(html)('#vlink_1 ul li input')):
            data.append((name, rid.attrib['value']))
    return data


def find_page_resource(pattern, page):
    data = []
    for link in pQuery(page)('li.gxbox ul li.l1 a'):
        # print(link.attrib['href'] + " " + link.attrib['alt'])
        name = link.attrib['alt']
        if pattern.search(name):
            logging.info('find course {0}'.format(name))
            data.append((name, link.attrib['href']))
    return data


def find_resource(key):
    data = []
    pattern = re.compile(r'{0}'.format(key), re.IGNORECASE)
    for i in range(1, 20):
        url = base_url + "/ys_kw_p{0}.html".format(i)
        logging.info('get {0}'.format(url))
        r = requests.get(url)
        if r.status_code == 404:
            continue
        ret = find_page_resource(pattern, r.content)
        if len(ret) > 0:
            data.extend(ret)
    return data


logging.basicConfig(level=logging.INFO)
download_res(get_resource_id(find_resource('PEP')))


# html = requests.get(base_url+"/ys_kw_p25.html").content
# # print(pQuery(html)('li.gxbox ul li a'))
# for link in pQuery(html)('li.gxbox ul li.l1 a'):
#     print(link.attrib['href'] + " " + link.attrib['alt'])

# html = requests.get(base_url+"/ys_kw/a20107.html").content
# print(pQuery(html)('#vlink_1 ul li input'))
# for rid in (pQuery(html)('#vlink_1 ul li input')):
#     print(rid.attrib['value'])

# html = requests.get(base_url+"/player.php?rid=189090").text
# # {mp3:"http://p0124.iusheng.com/userUp/2018/03/23686/u07_lesson3_gt.mp3"}
# pattern = re.compile(r'\{mp3:"(.+)"\}')
# match = pattern.search(html)
# if match:
#     print(match.group(1))
