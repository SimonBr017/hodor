#!/usr/bin/python3
import os
import sys
import pytesseract
import requests
from bs4 import BeautifulSoup
from PIL import Image
#from io import BytesIO
from pytesseract import image_to_string


url = "http://158.69.76.135/level3.php"
ip = "http://158.69.76.135"
id = 2835
repeat = 0
i = 0
head = {'Referer': url, 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64;\
 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141\
 Safari/537.36 Edg/87.0.664.75"}
#url_captcha = 'http://158.69.76.135/captcha.php'

while repeat < 1024:
    print("trying {} times ".format(i))
    print("voting time {}\n".format(repeat))
    
    
    s = requests.session()
    r = s.get(url)
    doc = r.content
    
    soup = BeautifulSoup(doc, 'html.parser')

    key = soup.find("input", {"name": "key"})
    key_value = key.get("value")
    
    #captcha = Image.open(BytesIO(requests.get(url_captcha).content))
    #captcha_data = image_to_string(captcha).strip()
    #print(captcha_data)

    url_captcha = soup.find("form", {"method": "post"}).find("img")
    url_captcha = ip + url_captcha["src"]
    captcha_img = open("captcha.png", "wb")
    captcha_img.write(s.get(url_captcha).content)
    captcha_img.close()
    captcha_data = pytesseract.image_to_string("captcha.png").strip()
    os.remove("captcha.png")
    #print(captcha_data)
    
    result = s.post(url, headers=head, data={"id": id, "key": key_value, "captcha": captcha_data, "holdthedoor": 1})
    i += 1
    if str(result.content) != "b'See you later hacker! [11]'":
        repeat += 1
