from string import maketrans, join
import re
import urllib2
import pickle
import zipfile
import Image
import bz2
import ImageDraw


def task0():
    return 2 ** 38


def task1(input):
    alphabet = map(chr, range(97, 123))
    translation = map(chr, range(99, 123)) + ['a', 'b']
    trans = maketrans(join(alphabet), join(translation))
    return input.translate(trans)


def task2(txtFile):
    res = ""
    f = open(txtFile)
    for line in f:
        for i in line:
            if ord(i) >= 97 and ord(i) <= 122:
                res += i
    return res


def task3(txtFile):
    f = open(txtFile)
    re.findall
    text = f.read()
    matches = re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", text)
    return join(matches, '')


def task4(baseUrl, number):
    rx = re.compile("and the next nothing is ([0-9]+)")
    for i in range(401):
        req = urllib2.Request(baseUrl + str(number))
        response = urllib2.urlopen(req).read()
        res = re.findall(rx, response)
        if not res[0]:
            print response
            break
        else:
            number = res[0]
    return response


def task5(txtFile):
    res = ""
    f = open(txtFile)
    x = pickle.Unpickler(f)
    x = x.load()
    for i in x:
        for j in i:
            if j[0] == "#":
                res += j[1] * "#"
            else:
                res += j[1] * " "
        res += "\n"
    return res


def task6(path, number):
    comments = ""
    f = zipfile.ZipFile("channel.zip")
    rx = re.compile("Next nothing is ([0-9]+)")
    while number:
        tmp = f.getinfo(str(number) + ".txt").comment
        comments += tmp
        text = f.open(str(number) + ".txt").read()
        res = re.findall(rx, text)
        if res:
            number = res[0]
        else:
            number = None
    return comments


def task7(image):
    string = ""
    res = ""
    tmp = 0
    img = Image.open(image)
    for i in range(0, img.size[0], 7):
        # look at the value of every 7th pixel, since this is level 7
        tmp = img.getpixel((i, 43))[0]
        if tmp >= 32 and tmp <= 126:
            string += chr(tmp)
    for i in re.findall("([0-9]+)", string):
        res += chr(int(i))
    return res


def task8(string):
    return bz2.BZ2Decompressor().decompress(string)


def task9(image, dots):
    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    draw.line(dots, fill=128)
    img.show()


def task10(input):
    res = input
    for x in range(30):
        input = ""
        for i in re.findall("(1+|2+|3+)", res):
            input += str(len(i)) + str(i[0])
        res = input
    return len(res)


def task11(input):
    img = Image.open(input)
    img1 = Image.new("RGB", (img.size[0], img.size[1]))
    for x1 in range(0, img.size[0], 2):
        for x2 in range(0, img.size[1], 2):
            i = (x1, x2)
            img1.putpixel(i, img.getpixel(i))
    img1.show()


def task12():
    print ""


print "task0", task0()
print "task1", task1("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
print "task1", task1("map")
print "task2", task2("task2.txt")
print "task3", task3("task3.txt")
# print "task4", task4("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=", 12345)
# print "task4", task4("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=", 25357)
print "task5", task5("task5.txt")
print "task6", task6("channel/", 90052)
print "task7", task7("oxygen.png")
print "task8 username", task8("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
print "task8 password", task8("BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
# task9("good.jpg", [146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170, 355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290, 178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194, 307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346, 199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192, 389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402, 216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213, 365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311, 215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243, 290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287, 279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294, 291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341, 306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302, 393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328, 336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346, 259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295, 349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350, 234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137, 339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281, 122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137, 214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159, 134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108, 171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124, 115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121, 89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108, 132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111, 156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153, 366, 149, 379, 147, 394, 146, 399])
# task9("good.jpg", [156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146, 218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81, 162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157, 128, 156, 134, 157, 136, 156, 136])
print "task10", task10("1")
print "task11", task11("cave.jpg")  # try to use the image library to seperate two interlaced pictures
