# url: http://www.pythonchallenge.com/pc/def/channel.html

# download: http://www.pythonchallenge.com/pc/def/channel.zip
import re
import zipfile

def readfile(num):
    with open("tmp/{}.txt".format(num)) as f:
        return f.read()

def getcomment(num):
    f = zipfile.ZipFile("channel.zip")
    return f.getinfo("{}.txt".format(num)).comment

regex = re.compile("nothing is (?P<num>\d+)")
num = 90052
comments = ""
while True:
    txt, comment = readfile(num), getcomment(num)
    comments += comment
    res = regex.search(txt)
    if res is None:
        break
    num = res.group('num')
print comments
