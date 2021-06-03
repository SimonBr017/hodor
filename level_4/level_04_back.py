#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
from itertools import cycle

from requests.models import Response

def get_proxies():

    url = 'https://free-proxy-list.net/'
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

def get_vote():
    url = 'http://158.69.76.135/level4.php'
    content= requests.get(url).text
    parser = fromstring(content)

    for i in parser.xpath('//table/tr'):
        if i.xpath('.//td[1][contains(text(),"2835")]'):
            vote = i.xpath('./td[2]/text()')[0]

    return int(vote)

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
    
    
    
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        vote = get_vote()
        print("vote:{}".format(repeat))
        print("vote reel: {}".format(vote))
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
        
        new_vote = get_vote()
        print("vote normalement reel {}".format(vote))
        print("new_vote: {}".format(new_vote))
       
        if new_vote == vote + 1:
            repeat += 1
            print("Sucsess !!!\n")
        i += 1
        print("Fail to vote\n")
        s.cookies.clear()
        
    except:
        i += 1
        s.cookies.clear()
        print("Ip Error : fail\n")
