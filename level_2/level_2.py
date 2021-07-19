#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup


url = "http://158.69.76.135/level2.php"
id = 2835
repeat = 1024
head = {'Referer': url, 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64;\
 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
 Safari/537.36 Edg/87.0.664.75"}

for i in range(repeat):
    print("voting time {}".format(i))
    s = requests.session()
    r = s.get(url)
    doc = r.content

    soup = BeautifulSoup(doc, 'html.parser')

    key = soup.find("input", {"name": "key"})
    key_value = key.get("value")

    s.post(url, headers=head,
           data={"id": id, "holdthedoor": 1, "key": key_value})
