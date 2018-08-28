#coding=utf-8
import requests
from lxml import etree


url = 'https://www.zhihu.com/people/zr9558/activities'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
rsp = requests.get(url, headers=headers)
rsp.encoding = 'utf-8'
html = etree.HTML(rsp.text)
name = html.xpath('.//*[@class="ProfileHeader-contentHead"]/h1/span/text()')[0]
expirence = html.xpath('.//*[@class="ProfileHeader-contentHead"]/h1/span/text()')[1]
print(name)
print(expirence)

