# url: http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"

def nextnothing(num):
    while True:
        response = requests.get(url.format(num))
        print response.text
        res = re.search("next nothing is (?P<num>\d+)", response.text)
        if res is None:
            break
        num = res.group('num')

nextnothing(12345)
nextnothing(16044/2)
